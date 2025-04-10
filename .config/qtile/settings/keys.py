from typing import Any, List, Tuple

from libqtile.config import Key  # type: ignore
from libqtile.lazy import lazy  # type: ignore

mod: str = "mod4"
key: Tuple[List[str], "str", Any]

keys: List[Key] = [
    Key(
        key[0],  # Modifiers
        key[1],  # Key
        *key[2 : len(key) : 1],  # Commands
    )
    for key in [
        # ------------ Window Configs ------------
        # Switch between windows in current stack pane
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        # Change window sizes (MonadTall)
        ([mod, "shift"], "l", lazy.layout.grow()),
        ([mod, "shift"], "h", lazy.layout.shrink()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Move windows up or down in current stack
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        # Kill window
        ([mod], "w", lazy.window.kill()),
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        ([mod], "r", lazy.spawncmd()),
        # Switch window focus to other pane(s) of stack
        ([mod], "space", lazy.layout.next()),
        # Swap panes of split stack
        ([mod, "shift"], "space", lazy.layout.rotate()),
        # ------------ App Configs ------------
        # Menu
        ([mod], "m", lazy.spawn("rofi -show run")),
        # Window Nav
        ([mod, "shift"], "m", lazy.spawn("rofi -show")),
        # Browser
        ([mod], "b", lazy.spawn("firefox")),
        # File Explorer
        ([mod], "e", lazy.spawn("thunar")),
        # Terminal
        ([mod], "Return", lazy.spawn("alacritty")),
        # Redshift
        # ([mod], "r", lazy.spawn("redshift -O 2400")),
        # ([mod, "shift"], "r", lazy.spawn("redshift -x")),
        # Screenshot
        ([mod], "s", lazy.spawn("scrot")),
        ([mod, "shift"], "s", lazy.spawn("scrot -s")),
        # ------------ Hardware Configs ------------
        # Volume
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        ),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ]
]
