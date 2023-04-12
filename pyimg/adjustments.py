from PIL import Image, ImageEnhance

class Adjustments:
    @staticmethod
    def brightness(img, value):
        print(f"Adjusted Brightness of '{img.filename} by {float(value) * 100}%")
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(float(value))
    
    @staticmethod
    def colour_balance(img, value):
        print(f"Adjusted Colour Balance of '{img.filename} by {float(value) * 100}%")
        enhancer = ImageEnhance.Color(img)
        return enhancer.enhance(float(value))
    
    @staticmethod
    def contrast(img, value):
        print(f"Adjusted Contrast of '{img.filename} by {float(value) * 100}%")
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(float(value))
    
    @staticmethod
    def sharpness(img, value):
        print(f"Adjusted Sharpness of '{img.filename} by {float(value) * 100}%")
        enhancer = ImageEnhance.Sharpness(img)
        return enhancer.enhance(float(value))