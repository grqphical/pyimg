# pyimg - Extendable Command line image editor

I made this to help with the workflow of quickly cropping and enhancing images

## How to use

pyimg has two built in submodules **Transform** and **Filters**. To use the transform submodule just run the command:
```bash
$ python -m pyimg IMAGE_FILE transform METHOD 
```

```IMAGE_FILE``` being the image you wish to change and ```METHOD``` being the method you want to use. To view avalible methods read the docs

You can do the same thing above for the Filters submodule

### Arguments for methods

Some methods you will see require arguments, you can pass these in after the method just seperated by a space
```bash
$ python -m pyimg IMAGE_FILE transform METHOD foo bar
```

## Docs

WIP. There is some help messages in the app currently you can use --help on any command to learn more

## Plugins

You can create plugins just create a new ```.py``` file in the ```plugins``` folder.

In that file first import the plugins API
```python
from plugins import BasePlugin
```

next create a class and have it inherit from ```BasePlugin``` with a blank constructor
```python
class Foobar(BasePlugin):
    def __init__(self):
        pass
```

now you are free to add any method you want just make sure: it has the decorator ```@staticmethod```, the first argument is the image being edited (a PIL Image class) and, returns the image at the end

Example:
```python
@staticmethod
def print_width(image):
    print(image.width)
    return image
```