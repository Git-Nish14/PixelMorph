import re
from .rgb import RGBRenkler
import sys
from .utils import convert_color_to_ansi

TURKISH_COLORS_NAMES = {}

for color_name, color_value in RGBRenkler.__dict__.items():
    if not color_name.startswith("__"):
        TURKISH_COLORS_NAMES[color_name] = color_value


def print(
    text: str,
    end: str | None = "\n",
) -> None:
    reset_escape = "\033[0m"

    # Handle color tags in the text
    pattern = re.compile(r"\[([^\[\]]+)\]")
    matches = pattern.finditer(text)

    for match in matches:
        color_tag = match.group(1)
        color = convert_color_to_ansi(color_tag)
        text = text.replace(f"[{color_tag}]", f"{color}", 1)

    sys.stdout.write(text + reset_escape + (end or ""))
    sys.stdout.flush()
