# coding: utf8
"""
5 + 148 + 10 + 226 + 10 + 76 + 5

480

29 + 5
"""
from PIL import Image

item_count = 562
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