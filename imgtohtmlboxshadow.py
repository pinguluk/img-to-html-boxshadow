from PIL import Image
import argparse, sys

def RGBAtoHex(tuple):
    r = format(tuple[0], 'x')
    g = format(tuple[1], 'x')
    b = format(tuple[2], 'x')
    a = format(tuple[3], 'x')

    # if value is <= 9, aka 1 char length, we add 0 before it
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    if len(a) == 1:
        a = "0" + a

    # if a is not 255
    if a != "255":
        return "#" + str(r) + str(g) + str(b) + str(a)

    # else if a is 255
    # we will hide it, because it's ignored from browser and will reduce file size
    # ex: #c45959ff is the same as #c45959; 255 = ff
    else:
        return "#" + str(r) + str(g) + str(b)


# arguments parser
parser=argparse.ArgumentParser()
parser.add_argument('-image', '--image', '-img' , '--img', help='Image filename + extension', required=True)
parser.add_argument('-output', '--output', help='Output filename + extension (should be .html)', required=True)
args=parser.parse_args()

# image name + extension
imageFileName = args.image

# load image + convert to RGBA
image = Image.open(imageFileName).convert('RGBA')

# load pixels
pixeldata = image.load()

#image height & width
width, height = image.size

# open / create html file
# take argument output file name if sety
if (args.output):
    file = open(args.output, 'w')
# else use default 'index.html'
else:
    file = open('index.html', 'w')


# write basic stuff for the html file
file.write('<!DOCTYPE html><html><head></head>')

# write the body: a container for the image width the width and height of the image & a 1x1 pixels div, that will contain the image as a box-shadow
file.write(f'<body><div class="container" style="display:inline-block;width:{str(width) + "px"};height:{str(height) + "px"}"><div id="img" style="background:transparent;width:1px;height:1px;margin-left:-1px;box-shadow:')

# box shadow that will apply to the div
boxShadow = ''

# loop rows
for y in range(height):
    # loop columns
    for x in range(width):
        # if current pixel is not transparent
        if pixeldata[x, y][3] != 0:
            # add box shadow pixel
            boxShadow += str(x + 1) + "px " + str(y) + "px " + RGBAtoHex(pixeldata[x,y]) + ","

# remove the last extra comma
boxShadow = boxShadow[:-1]

# add the boxshadow style to the div and close it
file.write(boxShadow + '">')

# close "image" div
file.write('</div>')

# close "container" div
file.write('</div>')

# close body & html tags
file.write('</body></html>')


