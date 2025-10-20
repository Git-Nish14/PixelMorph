from .hex import HEXRenkler
from .rgb import RGBRenkler


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color: tuple[int, int, int]) -> str:
    return "#%02x%02x%02x" % rgb_color


def convert_color_to_ansi(color):
    if color is None:
        return ""

    if isinstance(color, tuple):  # RGB color
        red, green, blue = color
    elif isinstance(color, str):  # HEX color
        color = color.lower()
        if color in RGBRenkler.__dict__:
            red, green, blue = RGBRenkler.__dict__[color]
        elif color.startswith("#"):
            red, green, blue = hex_to_rgb(color)
        elif "," in color or isinstance(color, (list, tuple)):
            red, green, blue = map(int, color.split(","))
        else:
            raise ValueError("Invalid color value")

    # Convert RGB color to ANSI escape sequence
    return f"\033[38;2;{red};{green};{blue}m"
