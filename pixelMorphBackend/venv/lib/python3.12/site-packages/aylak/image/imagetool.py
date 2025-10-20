from PIL import Image, ImageEnhance

class ImageTools:
    def __init__(self):
        pass

    def convert(
        self, image_path: str, output_format: str = "png"
    ):  # output_format: str="png"
        """
        Bir görüntüyü belirtilen biçime dönüştürür.

        :param image_path: Görüntü path'ı.
        :param output_format: Dönüştürmek için biçim.
        :return: Dönüştürülmüş görüntünün path'ı.
        """
        supported_formats = ["png", "jpeg", "jpg", "webp", "tiff", "bmp", "gif", "ico"]
        try:
            if (
                output_format not in supported_formats
                or image_path.split(".")[-1] not in supported_formats
            ):
                raise Exception(
                    f"Desteklenmeyen biçim. Desteklenen biçimler: {supported_formats}"
                )
            extension = image_path.split(".")[-1]
            if extension == output_format:
                return image_path
            image = Image.open(image_path)
            image.save(
                f"{image_path.replace(extension, '')}.{output_format}",
                output_format.upper(),
            )
            return f"{image_path.replace(extension, '')}.{output_format}"
        except Exception as e:
            print(f"Error: {e}")
            return None

    def resize(self, image_path: str, width: int, height: int):
        """
        Bir görüntünün boyutunu belirtilen boyuta ayarlar.

        :param image_path: Görüntü path'ı.
        :param width: Yeni genişlik.
        :param height: Yeni yükseklik.
        :return: Boyutlandırılmış görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = image.resize((width, height))
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def crop(self, image_path: str, x1: int, y1: int, x2: int, y2: int):
        """
        Bir görüntünün belirtilen koordinatlarda kırpılmasını sağlar.

        :param image_path: Görüntü path'ı.
        :param x1: X1 koordinatı.
        :param y1: Y1 koordinatı.
        :param x2: X2 koordinatı.
        :param y2: Y2 koordinatı.
        :return: Kırpılmış görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = image.crop((x1, y1, x2, y2))
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def rotate(self, image_path: str, angle: int):
        """
        Bir görüntünün açısını belirtilen açıya döndürür.

        :param image_path: Görüntü path'ı.
        :param angle: Döndürme açısı.
        :return: Döndürülmüş görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = image.rotate(angle)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def flip(self, image_path: str, direction: str = "horizontal"):
        """
        Bir görüntünün yönünü belirtilen yönüne çevirir.

        :param image_path: Görüntü path'ı.
        :param direction: Yön. Varsayılan: "horizontal" (yatay) ya da "vertical" (dikey)
        :return: Çevrilmiş görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            if direction == "horizontal":
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif direction == "vertical":
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def mirror(self, image_path: str, direction: str = "horizontal"):
        """
        Bir görüntünün yönünü belirtilen yönüne çevirir.

        :param image_path: Görüntü path'ı.
        :param direction: Yön. Varsayılan: "horizontal" (yatay) ya da "vertical" (dikey)
        :return: Çevrilmiş görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            if direction == "horizontal":
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif direction == "vertical":
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def grayscale(self, image_path: str):
        """
        Bir görüntünün renklerini griye çevirir.

        :param image_path: Görüntü path'ı.
        :return: Gri görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = image.convert("L")
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def invert(self, image_path: str):
        """
        Bir görüntünün renklerini tersine çevirir.

        :param image_path: Görüntü path'ı.
        :return: Ters görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = Image.eval(image, lambda x: 255 - x)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def brightness(self, image_path: str, value: int):
        """
        Bir görüntünün parlaklığını belirtilen değere ayarlar.

        :param image_path: Görüntü path'ı.
        :param value: Parlaklık değeri.
        :return: Parlak görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = ImageEnhance.Brightness(image).enhance(value)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def contrast(self, image_path: str, value: int):
        """
        Bir görüntünün kontrastını belirtilen değere ayarlar.

        :param image_path: Görüntü path'ı.
        :param value: Kontrast değeri.
        :return: Kontrastlı görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = ImageEnhance.Contrast(image).enhance(value)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def color(self, image_path: str, value: int):
        """
        Bir görüntünün renklerini belirtilen değere ayarlar.

        :param image_path: Görüntü path'ı.
        :param value: Renk değeri.
        :return: Renkli görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = ImageEnhance.Color(image).enhance(value)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None

    def sharpness(self, image_path: str, value: int):
        """
        Bir görüntünün keskinliğini belirtilen değere ayarlar.

        :param image_path: Görüntü path'ı.
        :param value: Keskinlik değeri.
        :return: Keskin görüntünün path'ı.
        """
        try:
            image = Image.open(image_path)
            image = ImageEnhance.Sharpness(image).enhance(value)
            image.save(image_path)
            return image_path
        except Exception as e:
            print(f"Error: {e}")
            return None
