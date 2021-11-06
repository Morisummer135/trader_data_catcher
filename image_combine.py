# coding: utf8
"""
两边5像素间隔，图片中间10像素间隔
5 + 148 + 10 + 226 + 10 + 76 + 5 = 480 预留10像素buffer=490

最高的item29 + 间隔5 = 一个item的高度34
"""
from PIL import Image
from datetime import datetime

def combine_image(item_count):
	new_img = Image.new("RGB", (490, item_count * 34))
	x = 5
	y = 5
	for idx in range(1, item_count + 1):
		img = Image.open("images/title%s.png" % idx)
		new_img.paste(img, (x, y))
		x += 148 + 10
		img = Image.open("images/skill%s.png" % idx)
		new_img.paste(img, (x, y))
		x += 226 + 10
		img = Image.open("images/cost%s.png" % idx)
		new_img.paste(img, (x, y))
		x = 0
		y += 34
	new_img.save(u"../images/其他/符文价格.png")
	f = open(u"../messages/符文价格.txt", "w")
	f.write(("%s" % datetime.now())[:19])
	f.close()

if __name__ == "__main__":
	combine_image(564)