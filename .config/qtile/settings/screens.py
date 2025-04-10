"""
Qtile screen and status bar configuration.

This module defines the layout and behavior of the top and bottom status bars 
for each screen in the Qtile window manager. It uses themed colors, icons, and 
widget configurations to create a visually consistent and informative UI.

Functions:
    status_bar(w): Creates a Bar instance with a specified list of widgets.

Globals:
    screens (List[Screen]): A list of screen definitions with top and bottom bars.
"""


from typing import List

from libqtile.bar import Bar
from libqtile.config import Screen

from settings.theme import colors
from settings.widgets import bottom_widgets, top_widgets

# import subprocess


def status_bar(w) -> Bar:
    """
    Creates a Qtile Bar with the given widgets and default styling.

    Args:
        w (list): A list of Qtile widgets to include in the bar.

    Returns:
        Bar: A configured Bar instance with specified widgets, background color,
             size, and opacity.
    """
    return Bar(
        widgets=w, size=24, opacity=0.85, background=colors.get("dark") or "#0f101a"
    )


screens: List[Screen] = [
    Screen(top=status_bar(w=top_widgets), bottom=status_bar(w=bottom_widgets)),
]

# connected_monitors = subprocess.run(
#     "xrandr | grep 'connected' | cut -d ' ' -f 2",
#     shell=True,
#     stdout=subprocess.PIPE
# ).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

# if connected_monitors > 1:
#     for i in range(1, connected_monitors):
#         screens.append(Screen(top=status_bar(top_widgets)))
