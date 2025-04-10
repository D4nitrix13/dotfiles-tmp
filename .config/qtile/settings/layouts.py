"""
Configures window layouts and floating window behavior in Qtile.

This file defines the configurations for window layouts in the Qtile window 
manager, including window layouts and rules for floating windows.

It imports configuration values from the `settings.theme` file for colors 
and uses those values to customize the appearance of the windows.

Attributes:
    layout_conf (dict): A dictionary containing configuration for border 
                        and margin settings for layouts.
    layouts (list): A list of different window layouts that will be used 
                    in Qtile.
    floating_layout (layout.Floating, optional): A floating layout with 
                                                  specific rules, if a 
                                                  valid color is defined.

Dependencies:
    - libqtile.layout: Provides the different layout types available.
    - libqtile.config: Provides necessary configurations for floating 
                       windows and window class matching.
    - settings.theme: The color configuration file.
    
Note:
    The floating layout is only configured if the color specified in 
    `colors.get("color4")` is not `None`.
"""

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Imports Qtile
from typing import Dict, List, Optional, Union

from libqtile import layout
from libqtile.config import Match

# Imports General
from settings.theme import colors

layout_conf: Dict[str, Union[str, int]] = {
    "border_focus": colors["focus"][0],
    "border_width": 1,
    "margin": 4,
}

layouts: List[
    Union[
        layout.Max,
        layout.MonadTall,
        layout.MonadWide,
        layout.Bsp,
        layout.Matrix,
        layout.RatioTile,
    ]
] = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


color: Optional[str] = colors.get("color4")

if color is not None:
    floating_layout: layout.Floating = layout.Floating(
        float_rules=[
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="file_progress"),
            Match(wm_class="notification"),
            Match(wm_class="splash"),
            Match(wm_class="toolbar"),
            Match(wm_class="confirmreset"),
            Match(wm_class="makebranch"),
            Match(wm_class="maketag"),
            Match(title="branchdialog"),
            Match(title="pinentry"),
            Match(wm_class="ssh-askpass"),
        ],
        border_focus=color,
    )
