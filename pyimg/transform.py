"""Functions related to transforming images"""
from PIL import Image

class Transform:
    @staticmethod
    def rotate(image, angle):
        """Rotates an image"""
        return image.rotate(int(angle))
    
    @staticmethod
    def merge(im1, im2):
        """Pastes another image ontop of the current image"""
        w = max(im1.size[0], im2.size[1])
        h = max(im1.size[1], im2.size[1])
        image = Image.new("RGBA", (w, h))

        image.paste(im1)
        image.paste(im2, mask=im2.convert("RGBA"))

        return image
    
    @staticmethod
    def resize(image, left, upper, right, bottom):
        """Resizes an image"""
        return image.resize((left, upper, right, bottom))
    
    @staticmethod
    def flip(image, flip_mode):
        """Flips an image"""
        if flip_mode.lower() == "horizontal":
            return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif flip_mode.lower() == "vertical":
            return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        else:
            print("ERROR: Invalid 'flip_mode' can be 'horizontal' or 'vertical'")
            return image