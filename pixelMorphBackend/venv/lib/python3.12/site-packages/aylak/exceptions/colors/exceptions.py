from ..rpc_errors import RPCError


# * Invalids
class InvalidRGBColorError(RPCError):
    """Raised when an invalid RGB color is provided."""

    CODE = 400
    NAME = "InvalidRGBColorError"
    MESSAGE = "Invalid RGB color: {value}"


class InvalidHEXColorError(RPCError):
    """Raised when an invalid HEX color is provided."""

    CODE = 400
    NAME = "InvalidHEXColorError"
    MESSAGE = "Invalid HEX color: {value}"


class InvalidColorError(RPCError):
    """Raised when an invalid color is provided."""

    CODE = 400
    NAME = "InvalidColorError"
    MESSAGE = "Invalid color: {value}"


class InvalidColorCodeError(RPCError):
    """Raised when an invalid color code is provided."""

    CODE = 400
    NAME = "InvalidColorCodeError"
    MESSAGE = "Invalid color code: {value}"


class InvalidColorNameError(RPCError):
    """Raised when an invalid color name is provided."""

    CODE = 400
    NAME = "InvalidColorNameError"
    MESSAGE = "Invalid color name: {value}"


class InvalidColorTypeError(RPCError):
    """Raised when an invalid color type is provided."""

    CODE = 400
    NAME = "InvalidColorTypeError"
    MESSAGE = "Invalid color type: {value}"


class InvalidColorValueError(RPCError):
    """Raised when an invalid color value is provided."""

    CODE = 400
    NAME = "InvalidColorValueError"
    MESSAGE = "Invalid color value: {value}"


class InvalidColorFormatError(RPCError):
    """Raised when an invalid color format is provided."""

    CODE = 400
    NAME = "InvalidColorFormatError"
    MESSAGE = "Invalid color format: {value}"


# * Not Founds
class ColorNotFoundError(RPCError):
    """Raised when a color is not found."""

    CODE = 404
    NAME = "ColorNotFoundError"
    MESSAGE = "Color not found: {value}"


# * Exists
class ColorAlreadyExistsError(RPCError):
    """Raised when a color already exists."""

    CODE = 400
    NAME = "ColorAlreadyExistsError"
    MESSAGE = "Color already exists: {value}"


class ColorCodeAlreadyExistsError(RPCError):
    """Raised when a color code already exists."""

    CODE = 400
    NAME = "ColorCodeAlreadyExistsError"
    MESSAGE = "Color code already exists: {value}"


class ColorNameAlreadyExistsError(RPCError):
    """Raised when a color name already exists."""

    CODE = 400
    NAME = "ColorNameAlreadyExistsError"
    MESSAGE = "Color name already exists: {value}"


# * Print JSON Errors
class PrintJSONError(RPCError):
    """Raised when a print JSON error occurs."""

    CODE = 400
    NAME = "PrintJSONError"
    MESSAGE = "Print JSON error: {value}"


class PrintJSONIndentError(RPCError):
    """Raised when a print JSON indent error occurs."""

    CODE = 400
    NAME = "PrintJSONIndentError"
    MESSAGE = "Print JSON indent error: {value}"


class PrintJSONEnsureAsciiError(RPCError):
    """Raised when a print JSON ensure ascii error occurs."""

    CODE = 400
    NAME = "PrintJSONEnsureAsciiError"
    MESSAGE = "Print JSON ensure ascii error: {value}"


class PrintJSONSortKeysError(RPCError):
    """Raised when a print JSON sort keys error occurs."""

    CODE = 400
    NAME = "PrintJSONSortKeysError"
    MESSAGE = "Print JSON sort keys error: {value}"


class PrintJSONSkipKeysError(RPCError):
    """Raised when a print JSON skip keys error occurs."""

    CODE = 400
    NAME = "PrintJSONSkipKeysError"
    MESSAGE = "Print JSON skip keys error: {value}"


class PrintJSONKeySeparatorError(RPCError):
    """Raised when a print JSON key separator error occurs."""

    CODE = 400
    NAME = "PrintJSONKeySeparatorError"
    MESSAGE = "Print JSON key separator error: {value}"


class PrintJSONNotSTRError(RPCError):
    """Raised when a print JSON not STR error occurs."""

    CODE = 400
    NAME = "PrintJSONNotSTRError"
    MESSAGE = "Print JSON not STR error: {value}"
