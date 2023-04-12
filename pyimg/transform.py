"""Functions related to transforming images"""
from PIL import Image

class Transform:
    @staticmethod
    def rotate(image, angle):
        """Rotates an image"""
        print(f"Rotated '{image.filename}'")
        return image.rotate(int(angle))
    
    @staticmethod
    def merge(im1, im2, x, y):
        """Pastes another image ontop of the current image"""
        w = max(im1.size[0], im2.size[1])
        h = max(im1.size[1], im2.size[1])
        image = Image.new("RGBA", (w, h))

        image.paste(im1)
        image.paste(im2, mask=im2.convert("RGBA"), box=(x, y))

        print(f"Merged '{im1.filename}' and '{im2.filename}")
        return image
    
    @staticmethod
    def resize(image, x, y):
        """Resizes an image"""
        print(f"Resized '{image.filename}' -> ({x}, {y})")
        return image.resize(size=(x, y))
    
    @staticmethod
    def flip(image, flip_mode):
        """Flips an image"""
        if flip_mode.lower() == "horizontal":
            print(f"Fliped '{image.filename}' horizontally")
            return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif flip_mode.lower() == "vertical":
            print(f"Fliped '{image.filename}' vertically")
            return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        else:
            print("ERROR: Invalid 'flip_mode' can be 'horizontal' or 'vertical'")
            return image