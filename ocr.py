# coding: utf8
from PIL import ImageGrab
import pytesseract

def get_image_by_cords(cords, name="", idx="", save=1):
  bbox = (cords[0][0], cords[0][1], cords[1][0], cords[1][1])
  print(bbox)
  im = ImageGrab.grab(bbox)
  if save:
    im.save("images/%s%s.png" % (name, idx))
  else:
    return im

def get_ocr_from_image(im):
  text = pytesseract.image_to_string(im, lang='chi_sim')
  return text