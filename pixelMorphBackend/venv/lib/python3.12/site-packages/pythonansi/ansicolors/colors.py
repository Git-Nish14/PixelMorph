class colors:
    """Renkler

    Args:
        colortype (`str`, optional): Almak istediğiniz renk türü. Varsayılan olarak 'bright' seçilmiştir...
        *colortype* için şunlar seçilebilir:

        `color`
        `bright`
        `backround`
        `brightbackround`
    Usage:
        >>> bg = colors(colortype='backround')
        >>> print(bg.red, "Bu bir test mesajıdır.")
        >>> # Bu yazı kırmızı arka plan ile yazdırılacaktır.
    """

    reset = "\033[0m"

    def __init__(self, colortype="bright") -> str:
        self.colortype = colortype
        if self.colortype == "color":
            # Black
            self.black = "\033[30m"

            # Red
            self.red = "\033[31m"

            # Green
            self.green = "\033[32m"

            # Yellow
            self.yellow = "\033[33m"

            # Blue
            self.blue = "\033[34m"

            # Magenta
            self.magenta = "\033[35m"

            # Cyan
            self.cyan = "\033[36m"

            # White
            self.white = "\033[37m"
        elif self.colortype == "bright":

            # Black
            self.black = "\033[30;1m"

            # Red
            self.red = "\033[31;1m"

            # Green
            self.green = "\033[32;1m"

            # Yellow
            self.yellow = "\033[33;1m"

            # Blue
            self.blue = "\033[34;1m"

            # Magenta
            self.magenta = "\033[35;1m"

            # Cyan
            self.cyan = "\033[36;1m"

            # White
            self.white = "\033[37;1m"
        elif self.colortype == "backround":

            # Black
            self.black = "\033[40m"

            # Red
            self.red = "\033[41m"

            # Green
            self.green = "\033[42m"

            # Yellow
            self.yellow = "\033[43m"

            # Blue
            self.blue = "\033[44m"

            # Magenta
            self.magenta = "\033[45m"

            # Cyan
            self.cyan = "\033[46m"

            # White
            self.white = "\033[47m"
        elif self.colortype == "brightbackround":

            # Black
            self.black = "\033[40;1m"

            # Red
            self.red = "\033[41;1m"

            # Green
            self.green = "\033[42;1m"

            # Yellow
            self.yellow = "\033[43;1m"

            # Blue
            self.blue = "\033[44;1m"

            # Magenta
            self.magenta = "\033[45;1m"

            # Cyan
            self.cyan = "\033[46;1m"

            # White
            self.white = "\033[47;1m"
        else:

            # Black
            self.black = "\033[30;1m"

            # Red
            self.red = "\033[31;1m"

            # Green
            self.green = "\033[32;1m"

            # Yellow
            self.yellow = "\033[33;1m"

            # Blue
            self.blue = "\033[34;1m"

            # Magenta
            self.magenta = "\033[35;1m"

            # Cyan
            self.cyan = "\033[36;1m"

            # White
            self.white = "\033[37;1m"

    def print(self, text: str, tip=None):
        """Renkli Yazdırma

        Args:
            text (str): Yazdıracağınız metin.
            tip (str): Yazılacak resim rengi. Varsayılan olarak kalın beyaz stilidir.
            
        Usage:
            >>> color = colors("bright")
            >>> color.print("Mesajınız", color.red)
        """
        if tip is None:
            tip = self.white
        return print(f"{tip}{text}{colors.reset}")
