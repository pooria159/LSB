import sys
import numpy as np
from PIL import Image
from colorama import Fore

def add_alpha_layer(image, transparency):
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            image.putpixel((x, y), (r, g, b, int(a * transparency)))
    return image


print(Fore.BLUE +"Enter Source Image Path :" + Fore.BLACK)
SourcePath = input()
print(Fore.BLUE +"Enter Watermark Image Path :" + Fore.BLACK)
WatermarkPath = input()
print(Fore.BLUE +"Enter Destination Image Path :" + Fore.BLACK)
resultPath = input()

try:
    Source = Image.open(SourcePath)
    watermark = Image.open(WatermarkPath)
    watermark = add_alpha_layer(watermark, 0.5)
    watermark = watermark.resize(Source.size)
    Source.paste(watermark, (0, 0), watermark)
    Source.save(resultPath)
    print(Fore.GREEN + "Watermarking operation was done successfully!!!" + Fore.BLACK)
except Exception as e:
    print(Fore.RED + "Watermarking operation encountered an error", str(e) + Fore.BLACK)
