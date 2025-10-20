import os
import platform

from aylak.rich import inspect
from aylak.rich.console import Console, get_windows_console_features
from aylak.rich.panel import Panel
from aylak.rich.pretty import Pretty


def report() -> None:  # pragma: no cover
    """Print a report to the terminal with debugging information"""
    console = Console()
    inspect(console)
    features = get_windows_console_features()
    inspect(features)

    env_names = (
        "TERM",
        "COLORTERM",
        "CLICOLOR",
        "NO_COLOR",
        "TERM_PROGRAM",
        "COLUMNS",
        "LINES",
        "JUPYTER_COLUMNS",
        "JUPYTER_LINES",
        "JPY_PARENT_PID",
        "VSCODE_VERBOSE_LOGGING",
    )
    env = {name: os.getenv(name) for name in env_names}
    console.print(Panel.fit((Pretty(env)), title="[b]Environment Variables"))

    console.print(f'platform="{platform.system()}"')


if __name__ == "__main__":  # pragma: no cover
    report()
