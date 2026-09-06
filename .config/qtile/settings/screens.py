# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Multimonitor support
from subprocess import PIPE, CompletedProcess, run
from typing import List

from libqtile.bar import Bar
from libqtile.config import Screen
from libqtile.log_utils import logger

from settings.theme import colors

from .widgets import bottom_widgets, primary_widgets, secondary_widgets


def status_bar(widgets):
    # Creates a Qtile bar using the provided widget list.
    return Bar(
        widgets=widgets,
        size=24,
        opacity=0.92,
        background=colors.get("dark") or "#0f101a",
    )


# Primary screen configuration.
screens: List[Screen] = [
    Screen(top=status_bar(primary_widgets), bottom=status_bar(widgets=bottom_widgets))
]

# Command used to count the number of connected monitors.
xrandr: str = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

# Executes the xrandr command and captures stdout/stderr.
command: CompletedProcess[bytes] = run(
    args=xrandr,
    shell=True,
    stdout=PIPE,
    stderr=PIPE,
)

# Declare the variable only once to avoid mypy no-redef errors.
connected_monitors: int

if command.returncode != 0:
    # If the command fails, log the error and fallback to one monitor.
    error: str = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    # Convert the command output into an integer monitor count.
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    # Add one secondary screen configuration for each extra monitor.
    _: int
    for _ in range(1, connected_monitors, 1):
        screens.append(Screen(top=status_bar(secondary_widgets)))
