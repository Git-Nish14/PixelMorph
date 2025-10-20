import logging
from aylak.colors import Renkler


class ColoredHandler(logging.Handler):
    colors = Renkler()
    COLORS = {
        "DEBUG": colors.orta_mavi,
        "INFO": colors.sari,
        "WARNING": colors.turuncu,
        "ERROR": colors.turuncu_kirmizi,
        "CRITICAL": colors.turkuaz,
    }
    MARKINGS = {
        "DEBUG": "-",
        "INFO": "+",
        "WARNING": "!",
        "ERROR": "x",
        "CRITICAL": "*",
    }
    RESET = colors.reset

    def emit(self, record):

        try:
            msg = self.format(record)
            levelname = record.levelname
            colored_levelname = self.COLORS.get(levelname, self.colors.beyaz)
            marking = self.MARKINGS.get(levelname, "+")
            formatted_message = f"{colored_levelname}[{self.colors.beyaz}{marking}{colored_levelname}] {msg}{self.RESET}"
            print(formatted_message)
        except Exception:
            self.handleError(record)
