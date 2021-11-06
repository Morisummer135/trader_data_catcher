#coding: utf8
from PIL import Image
import time
from consts import (
	item_mouse_pointers, next_page_pointer,
	item_count_cords, default_pages, item_cords,
)
from ocr import get_image_by_cords
from ocr import get_ocr_from_image
from string_utils import filter_non_digits
from mouse_utils import mouse_move, mouse_click
from image_combine import combine_image

class Trader(object):

	def __init__(self):
		self.page = 1
		self.item = 1
		self.cnt = 0

	def get_page_limit(self):
		image = get_image_by_cords(item_count_cords, "page_limit")
		image = Image.open("images/page_limit.png")
		ocr = filter_non_digits(get_ocr_from_image(image))
		print(ocr)
		return int(ocr) or default_pages

	def get_item_info_images(self):
		self.cnt += 1
		list_idx = (self.cnt - 1) % 6
		item_pointer = item_mouse_pointers[list_idx]
		mouse_move(*item_pointer)
		time.sleep(0.1)
		title_cords = item_cords["title"][list_idx]
		skill_cords = item_cords["skill"][list_idx]
		cost_cords = item_cords["cost"][list_idx]
		get_image_by_cords(title_cords, "title", self.cnt)
		get_image_by_cords(skill_cords, "skill", self.cnt)
		get_image_by_cords(cost_cords, "cost", self.cnt)


	def get_items_info_images(self):
		for page in range(self.page_limit):
			for item_idx in range(6):
				self.get_item_info_images()
			mouse_click(*next_page_pointer)
			time.sleep(0.5)

	def combine_images(self):
		combine_image(self.cnt)

	def fetch_item_list(self):
		# self.page_limit = (self.get_page_limit() + 5) / 6
		self.page_limit = 94
		self.get_items_info_images()
		self.combine_images()
		'''
		self.extract_items_info()
		self.save_items_info_to_csv()
		'''

if __name__ == "__main__":
	time.sleep(5)
	trader = Trader()
	trader.fetch_item_list()