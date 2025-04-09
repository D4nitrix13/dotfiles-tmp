# Imports Qtile
from libqtile import layout
from libqtile.config import Match

# Imports General
from settings.theme import colors
from typing import List, Dict, Union

layout_conf: Dict[str, Union[str, int]] = {
    "border_focus": colors["focus"][0],
    "border_width": 1,
    "margin": 4,
}

layouts: List[
    Union[
        layout.Max, layout.MonadTall, layout.MonadWide,
        layout.Bsp, layout.Matrix, layout.RatioTile,
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
    border_focus=colors["color4"][0],
)
