import sys
from PIL import Image


max_brightness = 255*3
colors="S&~!c^"

def char_from_px(pixel):
    (r, g, b) = pixel
    if(r+g+b > max_brightness/1.5): return ' '
    if(g+b > max_brightness/2): return ' '
    if(r+g+b > max_brightness/2): return ','
    if(r+g+b > max_brightness/2.5): return ':'
    if(r+g+b > max_brightness/3): return '_'
    if(r+g+b < max_brightness/10): return '@'
    if(r+g+b < max_brightness/8): return '#'
    color = [2*r,2*g,2*b,r+g,r+b,g+b]
    return colors[color.index(max(color))]

width = 256
new_height = 72

N=0
while(N<1970):
    image_path = "temp/video."+str(N)+".jpg"
    img = Image.open(image_path)
    img = img.resize((width, new_height))

    ascii_art = ""
    for y in range(0, int(new_height) - 1):
        line = ""
        for x in range(0, width - 1):
            px = img.getpixel((x, y))
            line += char_from_px(px)
        ascii_art += line+'\n'

    # write to a text file.
    with open("ascii_stills/"+str(N)+".txt", "w") as f:
        f.write(ascii_art)
    N += 10