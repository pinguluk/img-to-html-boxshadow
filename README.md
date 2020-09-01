# img-to-html-boxshadow

img-to-html=boxshadow is a Python script that converts every pixel from an image, to a box-shadow pixel.

## Installation

Download the imgtohtmlboxshadow.py script and install PIL

```
pip install pillow
```

## Usage

```
imgtohtmlboxshadow.py -img IMAGE_DOT_EXTENSION -output FILENAME.html
```

## Example

```
imgtohtmlboxshadow.py -img cat.jpg -output cat.html
imgtohtmlboxshadow.py -img fish.png -output fish.html
```

## Preview

![Cat](https://i.postimg.cc/fWrJByhS/cat.png)
![Fish](https://i.postimg.cc/zfCgQrkZ/Screenshot-105.png)

## TODO

- ~~Convert rgba(r, g, b, a) to hex value, to reduce the file size~~
- Improve the width (and height) of a pixel, when the adjacent pixels are the same, in order to remove repetitive pixels and improve file size 

## Checkout the other method I've made, using HTML elements
[img-to-html](https://github.com/pinguluk/img-to-html)
