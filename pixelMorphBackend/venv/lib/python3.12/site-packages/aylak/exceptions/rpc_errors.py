from datetime import datetime
from typing import Union


class RPCError(Exception):
    ID: int = None
    CODE: int = None
    NAME: str = None
    MESSAGE: str = "{value}"

    def __init__(
        self,
        value: Union[int, str, Exception] = None,
        rpc_name: str = None,
        is_unknown: bool = False,
        is_signed: bool = False,
    ):
        super().__init__(
            "Aylak ERROR: [{}{} {}] - {} {}".format(
                "-" if is_signed else "",
                self.CODE,
                self.ID or self.NAME,
                self.MESSAGE.format(value=value),
                f'(caused by "{rpc_name}")' if rpc_name else "",
            )
        )
        try:
            self.value = int(value)
        except (ValueError, TypeError):
            self.value = value

        if is_unknown:
            with open("unknown_errors-aylak.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}\t{value}\t{rpc_name}\n")
