import sys
from typing import TYPE_CHECKING, Optional, Union

from .jupyter import JupyterMixin
from .segment import Segment
from .style import Style

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal  # pragma: no cover


if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult


EmojiVariant = Literal["emoji", "text"]


class NoEmoji(Exception):
    """No emoji by that name."""
