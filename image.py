import os
from PIL import Image

os.chdir(r'/home/franks/Documents/Applications/Quanlin PR Card Renewal 2025')

img = Image.open('photo_back.jpg')
img = img.resize((1267, 1689), Image.LANCZOS)
img.save("output.jpg", quality=95)