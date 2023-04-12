"""Built in filters to pyimg"""
from PIL import ImageFilter, ImageEnhance

class Filters:
    @staticmethod
    def greyscale(image):
        return image.convert("LA")
    
    @staticmethod
    def blur(image):
        return image.filter(ImageFilter.BLUR)
    
    @staticmethod
    def contour(img):
        return img.filter(ImageFilter.CONTOUR)
    
    @staticmethod
    def detail(img):
        return img.filter(ImageFilter.DETAIL)
    
    @staticmethod
    def edge_enhance(img):
        return img.filter(ImageFilter.EDGE_ENHANCE)
    
    @staticmethod
    def edge_enhance_more(img):
        return img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    
    @staticmethod
    def emboss(img):
        return img.filter(ImageFilter.EMBOSS)
    
    @staticmethod
    def find_edges(img):
        return img.filter(ImageFilter.FIND_EDGES)
    
    @staticmethod
    def sharpen(img):
        return img.filter(ImageFilter.SHARPEN)
    
    @staticmethod
    def smooth(img):
        return img.filter(ImageFilter.SMOOTH)
    
    @staticmethod
    def smooth_more(img):
        return img.filter(ImageFilter.SMOOTH_MORE)
    
    @staticmethod
    def brightness(img, value):
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(value)