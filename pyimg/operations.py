from PIL import ImageOps, Image


class Operations:
    @staticmethod
    def auto_contrast(image, cutoff=0, ignore=None, preserve_tone=False):
        """Normalizes the contrast of an image"""
        print(f"Normalized Contrast of '{image.filename}'")
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            adjusted_image = ImageOps.autocontrast(rgb_image, cutoff, ignore, preserve_tone)

            r2,g2,b2 = adjusted_image.split()
            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

            return final_transparent_image

        else:
            adjusted_image = ImageOps.autocontrast(rgb_image, cutoff, ignore, preserve_tone)
            return adjusted_image


    @staticmethod
    def invert(image):
        """Inverts colours of an image"""
        print(f"Inverted '{image.filename}'")
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            inverted_image = ImageOps.invert(rgb_image)

            r2,g2,b2 = inverted_image.split()

            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

            return final_transparent_image

        else:
            inverted_image = ImageOps.invert(image)
            return inverted_image
    
    @staticmethod
    def posterize(image, bits):
        """Reduces the amount of bits on an image"""
        print(f"Reduced '{image.filename}' to {bits} bits")
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            adjusted_image = ImageOps.posterize(rgb_image, bits)

            r2,g2,b2 = adjusted_image.split()
            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

            return final_transparent_image

        else:
            adjusted_image = ImageOps.posterize(image, bits)
            return adjusted_image
    
    @staticmethod
    def solarize(image, threshold):
        """Solarizes the image by the threshold"""
        print(f"Solarized '{image.filename}'")
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            adjusted_image = ImageOps.solarize(rgb_image, threshold)

            r2,g2,b2 = adjusted_image.split()
            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

            return final_transparent_image

        else:
            adjusted_image = ImageOps.solarize(image, threshold)
            return adjusted_image