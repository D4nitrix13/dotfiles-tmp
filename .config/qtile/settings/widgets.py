"""
Qtile bar widgets configuration using a themed layout.

This module defines utility functions and widget groups for constructing
customized top and bottom bars in a Qtile-based window manager setup.

Functions:
    - base(): Returns a dictionary of foreground and background colors.
    - text_box(): Returns default styling for TextBox widgets.
    - workspaces(): Returns a configured GroupBox for workspace indicators.

Widget groups:
    - top_widgets: Comprehensive list of widgets for the top bar including
      workspace indicators, system monitors, and a systray.
    - bottom_widgets: Slim status bar with focused window name, system info, and clock.

Constants:
    - separator: Thin spacer widget used between sections.
    - widget_defaults: Default font and padding settings for widgets.
    - extension_defaults: Copied defaults for use with Qtile extensions.
"""

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from subprocess import check_output
from typing import Dict, List, Union

from libqtile import qtile, widget

from settings.theme import colors, img


def base(fg: str = "text", bg: str = "dark") -> Dict[str, str]:
    """
    Returns a dictionary with foreground and background colors based on the
    keys defined in the `colors` dictionary.

    Args:
        fg (str): Key for the foreground color.
        bg (str): Key for the background color.

    Returns:
        Dict[str, str]: Dictionary with "foreground" and "background" keys.
    """
    return {
        "foreground": colors.get(fg) or "#0f101a",
        "background": colors.get(bg) or "#0f101a",
    }


def text_box(fontsize=20) -> Dict[str, Union[str, int]]:
    """
    Returns default parameters for a TextBox widget.

    Args:
        fontsize (int): Font size of the text.

    Returns:
    """
    return {
        "font": "UbuntuMono Bold Italic",
        "fontsize": fontsize,
        "padding": 5,
    }


def workspaces() -> List[widget.GroupBox]:
    """
    Creates a list with a single customized GroupBox widget for displaying workspaces.

    Returns:
        List[widget.GroupBox]: List containing one configured GroupBox instance.
    """
    return [
        widget.GroupBox(
            **base(fg="light"),
            font="UbuntuMono Nerd Font",
            fontsize=22,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors["light"],
            inactive=colors["light"],
            rounded=False,
            highlight_method="block",
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
        )
    ]


separator: Dict[str, Union[str, int]] = {
    **base(),
    "linewidth": 0,
    "padding": 5,
}
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

top_widgets: List[
    Union[
        List[widget.GroupBox],
        widget.Spacer,
        widget.Image,
        widget.TextBox,
        widget.CheckUpdates,
        widget.PulseVolume,
        widget.KeyboardLayout,
        widget.DF,
        widget.Memory,
        widget.CPU,
        widget.Net,
        widget.CurrentLayoutIcon,
        widget.CurrentLayout,
        widget.Systray,
        widget.Sep,
    ],
] = [
    *workspaces(),
    widget.Spacer(),
    widget.Image(filename=img["bar11"]),
    widget.TextBox(
        **base(bg="color10"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-fa-download
    ),
    widget.CheckUpdates(
        **base(bg="color10"),
        distro="Arch_checkupdates",
        execute="alacritty",
        update_interval=1,
        no_update_string="Updates: 0",
        fmt="{} ",
    ),
    widget.Image(filename=img["bar10"]),
    widget.TextBox(
        **base(bg="color9"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-fa-volume_high
    ),
    widget.PulseVolume(
        **base(bg="color9"),
        channel="Master",
        mute_format="Muted",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
        fmt="Vol: {} ",
    ),
    widget.Image(filename=img["bar9"]),
    widget.TextBox(
        **base(bg="color8"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-fa-keyboard
    ),
    widget.KeyboardLayout(
        **base(bg="color8"),
        fmt="Kbd: {} ",
    ),
    widget.Image(filename=img["bar8"]),
    widget.TextBox(
        **base(bg="color7"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-fa-floppy_disk
    ),
    widget.DF(
        **base(bg="color7"),
        update_interval=1,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e df")},
        partition="/",
        format="{p} {uf}{m} [{r:.2f}%]",
        fmt="Disk: {} ",
        # fmt="Disk: {} ",
        visible_on_warn=False,
    ),
    widget.Image(filename=img["bar7"]),
    widget.TextBox(
        **base(bg="color6"),
        **text_box(fontsize=26),
        text=" ",  # Icon: nf-fa-memory
    ),
    widget.Memory(
        **base(bg="color6"),
        font="UbuntuMono Bold Italic",
        format="{MemUsed: .2f}{mm} /{MemTotal: .2f}{mm}",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e htop")},
        fmt="{} ",
    ),
    widget.Image(filename=img["bar6"]),
    widget.TextBox(
        **base(bg="color5"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-oct-cpu
    ),
    widget.CPU(**base(bg="color5"), fmt="{} "),
    widget.Image(filename=img["bar5"]),
    widget.TextBox(
        **base(bg="color4"),
        **text_box(fontsize=26),
        text="",  # Icon: nf-fa-feed
    ),
    widget.Net(**base(bg="color4"), interface="enp10s0", fmt="{} "),
    widget.Image(filename=img["bar4"]),
    widget.CurrentLayoutIcon(**base(bg="color3"), scale=0.65),
    widget.CurrentLayout(**base(bg="color3"), padding=5),
    widget.Image(filename=img["bar3"]),
    widget.Systray(background=colors["dark"], padding=7),
    widget.Sep(**separator),
]


bottom_widgets: List[
    Union[
        widget.Sep,
        widget.WindowName,
        widget.Spacer,
        widget.Image,
        widget.GenPollText,
        widget.TextBox,
        widget.Clock,
    ]
] = [
    widget.Sep(**separator),
    widget.WindowName(
        **base(fg="focus"), font="UbuntuMono Bold Italic", fontsize=14, padding=5
    ),
    widget.Spacer(),
    widget.Image(filename=img["bar2"]),
    widget.GenPollText(
        **base(bg="color2"),
        func=lambda: check_output(
            args='printf "Arch Linux $(uname -r) "', shell=True, text=True
        ),
        fontsize=14,
        padding=5,
        fmt="❤ {}",
    ),
    widget.Image(filename=img["bar1"]),
    widget.TextBox(
        **base(bg="color1"),
        **text_box(fontsize=26),
        text="󰃰",  # Icon: nf-md-calendar_clock
    ),
    widget.Clock(**base(bg="color1"), format="%A, %d of %B %Y - %I:%M:%S %p "),
]

widget_defaults: Dict[str, Union[str, int]] = {
    "font": "UbuntuMono Bold Italic",
    "fontsize": 14,
    "padding": 1,
}

extension_defaults: Dict[str, Union[str, int]] = widget_defaults.copy()
