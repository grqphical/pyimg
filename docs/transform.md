# Transform

The transform class contains all actions realted to transformations of the image such as rotation or scale

## Methods

### Rotate

Rotates an image based on a given angle

*The example below rotates an image by 45 degrees*
```bash
$ python -m pyimg example.png transform rotate 45
```

### Merge

Adds an image ontop of the first image with a given position as X, Y. The position is based from the images upper-left hand corner

*The example below merges an image on top of another at coordinate (100, 100)*
```bash
$ python -m pyimg example.png transform merge example2.png 100 100
```

### Resize

Scales an image based on a given width and height

*The example below scales an image to 1024 by 1024 pixels*
```bash
$ python -m pyimg example.png transform resize 1024 1024
```

### Flips

Flips an image on either the *horizontal* or *vertical* axes

*The example below flips an image on the vertical axis*
```bash
$ python -m pyimg example.png transform flip vertical
```