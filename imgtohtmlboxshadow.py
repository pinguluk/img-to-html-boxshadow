from PIL import Image
import argparse, sys

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
file.write(f'<body><div class="container" style="position:relative;display:inline-block;width:{str(width) + "px"};height:{str(height) + "px"}"><div id="img" style="background:transparent;width:1px;height:1px;position:absolute;top:0;left:-1px;box-shadow:')

# box shadow that will apply to the div
boxShadow = ''

# counter for the number of iterated pixels
pixelCount = 0

# loop rows
for y in range(height):
    # loop columns
    for x in range(width):
        # if current pixel is transparent => box shadow pixel will be transparent
        if pixeldata[x, y][3] == 0:
            boxShadow += str(x + 1) + "px " + str(y) + "px " + "0 " + "#f000" # we add +1, otherwise, the div will overlap the boxshadow pixel
            
        # else write the current pixel to rgb value
        else:
            # rgbaValue = (r, g, b, a), where a = a / 255 (we need value between 0 and 1) & format to 2 decimals
            r = str(pixeldata[x,y][0])
            g = str(pixeldata[x,y][1])
            b = str(pixeldata[x,y][2])
            a = str(format(pixeldata[x,y][3]/255, '.2f'))

            # if a == 0.00, set it to 0 so we minify the output
            if a == '0.00':
                a = '0'
            # else if a == 1.00, set it to 0 so we minify the output as well
            elif a == '1.00':
                a = '1'

            # add box shadow pixel
            boxShadow += str(x + 1) + "px " + str(y) + "px " + "0 " + f'rgba({r}, {g}, {b}, {a})'

        # if the pixelCount isn't the last pixel from the image
        # we will add comma to each box shadow pixel
        if pixelCount != (width * height) - 1:
            boxShadow += ','
            pixelCount += 1

# add the boxshadow style to the div and close it
file.write(boxShadow + '">')

# close "image" div
file.write('</div>')

# close "container" div
file.write('</div>')

# close body & html tags
file.write('</body></html>')


