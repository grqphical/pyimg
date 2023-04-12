"""Built in filters to pyimg"""
from PIL import ImageFilter

class Filters:
    @staticmethod
    def greyscale(image):
        print(f"Converted '{image.filename} to greyscale")
        return image.convert("LA")
    
    @staticmethod
    def blur(image):
        print(f"Blurred '{image.filename}")
        return image.filter(ImageFilter.BLUR)
    
    @staticmethod
    def contour(image):
        print(f"Added contour to '{image.filename}")
        return image.filter(ImageFilter.CONTOUR)
    
    @staticmethod
    def detail(image):
        print(f"Increased detail of '{image.filename}")
        return image.filter(ImageFilter.DETAIL)
    
    @staticmethod
    def edge_enhance(image):
        print(f"Enhanced edges on'{image.filename}")
        return image.filter(ImageFilter.EDGE_ENHANCE)
    
    @staticmethod
    def edge_enhance_more(image):
        print(f"Enhanced edges more on '{image.filename}")
        return image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    
    @staticmethod
    def emboss(image):
        print(f"Added emboss to '{image.filename}")
        return image.filter(ImageFilter.EMBOSS)
    
    @staticmethod
    def find_edges(image):
        print(f"Found edges of '{image.filename}")
        return image.filter(ImageFilter.FIND_EDGES)
    
    @staticmethod
    def sharpen(image):
        print(f"Sharpened '{image.filename}")
        return image.filter(ImageFilter.SHARPEN)
    
    @staticmethod
    def smooth(image):
        print(f"Smoothed '{image.filename}")
        return image.filter(ImageFilter.SMOOTH)
    
    @staticmethod
    def smooth_more(image):
        print(f"Smoothed More'{image.filename}")
        return image.filter(ImageFilter.SMOOTH_MORE)