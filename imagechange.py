from re import S
from turtle import left
import PIL
from PIL import Image
from PIL import ImageDraw, ImageFont
import sys

with Image.open("duck.png").convert("RGBA") as image:
    images = []
    lables = []
    for i in range(3):
        for j in (0.1, 0.5, 0.9):
            source = image.split()
            mid = source[i].point(lambda x: x*j)
            source[i].paste(mid)
            im = Image.merge(image.mode, source)
            lables.append('channel {} intensity {}'.format(i, j))
            images.append(im)
    font = ImageFont.truetype("Fanwood.ttf", 25)

    first_image = images[0]
    contact_sheet = PIL.Image.new(
        first_image.mode, (first_image.width*3, first_image.height*3+3*85))
    x = 0
    y = 0
    draw = ImageDraw.Draw(contact_sheet)
    for i, img in enumerate(images):
        contact_sheet.paste(img, (x, y))
        draw.text((x, y+first_image.height + 5), lables[i], font=font)
        if x+first_image.width == contact_sheet.width:
            x = 0
            y = y+first_image.height+85
        else:
            x = x+first_image.width
    contact_sheet.show()
