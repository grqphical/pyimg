# Operations

These are more sophisticated operations that can be done on images

### Auto Contrast

Normalizes the contrast of an image

#### Parameters
- **cutoff(int)** - The percent to cut off from the histogram on the low and high ends
- **ignore(int, None)** - The background pixel value (use None for no background)
- **preserve_tone(bool)** - Preserve image tone in Photoshop-like style autocontrast.

```bash
$ python -m pyimg example.png operations auto_contrast CUTOFF IGNORE PRESERVE_TONE
```

### Invert

Inverts an image's colours

```bash
$ python -m pyimg example.png operations invert
```

### Posterize

Reduces the amount of bits in an image

*The example below reduces an image to 2 bits per channel*
```bash
$ python -m pyimg example.png operations posterize 2
```

### Solarize
Solarizes an image

*The example below solarizes an image with a threshold of 50*
```bash
$ python -m pyimg example.png operations solarize 50
```