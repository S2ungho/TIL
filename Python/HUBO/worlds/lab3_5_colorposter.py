from cs1media import *
white = (255, 255, 255)
black = (0, 0, 0)

def luma(p):
 r, g, b = p
 return int(0.213 * r + 0.715 * g + 0.072 * b)

def colorposter(img, threshold_light,threshold_dark):
 w, h = img.size()
 for y in range(h):
  for x in range(w):
    r, g, b = img.get(x, y)
    v = (r + g + b) // 3 # average of r,g,b
    if v>threshold_light:
      img.set(x, y, (255,255,0))
    elif v<threshold_dark:
      img.set(x, y, (0,0,255))
    else:
      img.set(x, y, (0,255,0))

img_file_name = input("Enter an image file name> ")
threshold_light = input("Threshold for lightness --> ")
threshold_dark = input("Threshold for darkness --> ")

pict = load_picture(img_file_name)
pict.show()
colorposter(pict, int(threshold_light), int(threshold_dark))
pict.show()

