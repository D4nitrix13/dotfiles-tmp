"""
This script defines mouse actions and bindings for interacting with windows in the Qtile window manager.

It configures drag and click actions using modifier keys and mouse buttons to control window behavior.

Mouse Actions:
- Dragging with `Button1` moves the window to a floating position.
- Dragging with `Button3` resizes the floating window.
- Clicking with `Button2` brings the window to the front.

Variables:
- mouse (List[Union[Drag, Click]]): A list of mouse actions including drag and click events bound to specific buttons and modifiers.

This script allows for customized mouse interactions with windows in Qtile for better workflow control.
"""

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from typing import List, Union
from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from settings.keys import mod

mouse: List[Union[Drag, Click]] = [
    Drag(
        [mod],  # Modifiers
        "Button1",  # Button
        lazy.window.set_position_floating(),  # Commands
        start=lazy.window.get_position(),  # Start
    ),
    Drag(
        [mod],  # Modifiers
        "Button3",  # Button
        lazy.window.set_size_floating(),  # Commands
        start=lazy.window.get_size(),  # Start
    ),
    Click(
        [mod],  # Modifiers
        "Button2",  # Button
        lazy.window.bring_to_front(),  # Commands
    ),
]
