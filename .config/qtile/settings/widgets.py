"""
Qtile widget bar configuration.

This file defines the appearance, layout, and functionality of the widgets used in the
top and bottom bars of a custom Qtile desktop environment. It uses a color palette
inspired by the Material Ocean theme and organizes widgets into three main groups:

- `primary_widgets`: Widgets shown on the primary screen (system info, network, audio, etc.)
- `secondary_widgets`: Widgets shown on secondary screens (layout, clock, etc.)
- `bottom_widgets`: Optional widgets for a bottom bar (active window, system info, clock, etc.)

Each widget is styled consistently using helper functions such as `base()`, `icon()`,
and `powerline()`, and utilizes Nerd Font icons.
"""
# -*- coding: utf-8 -*-
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from subprocess import check_output
from typing import Any, Dict, List, Union

from libqtile import qtile, widget  # type: ignore

from .path import interface_path
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg: str = "text", bg: str = "dark") -> Dict[str, Any]:
    """
    Returns a dictionary with foreground and background colors
    based on the current theme configuration.

    Parameters:
        fg (str): The key for the foreground color in the theme dictionary. Defaults to "text".
        bg (str): The key for the background color in the theme dictionary. Defaults to "dark".

    Returns:
        dict: A dictionary containing 'foreground' and 'background' keys with hex color values.
    """
    return dict(
        foreground=colors.get(fg) or "#0f101a", background=colors.get(bg) or "#0f101a"
    )


def separator() -> widget.Sep:
    """
    Creates a separator widget with transparent spacing.

    Returns:
        widget.Sep: A separator with no visible line, used to add padding between widgets.
    """
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(
    fg: str = "text", bg: str = "dark", fontsize: int = 16, text: str = "?"
) -> widget.TextBox:
    """
    Creates a styled TextBox widget used as an icon with Nerd Font glyphs.

    Parameters:
        fg (str): The foreground color key from the theme. Defaults to "text".
        bg (str): The background color key from the theme. Defaults to "dark".
        fontsize (int): Font size of the icon. Defaults to 16.
        text (str): The text or glyph to display. Defaults to "?".

    Returns:
        widget.TextBox: A TextBox configured as an icon with the specified styles.
    """
    return widget.TextBox(**base(fg, bg), fontsize=fontsize, text=text, padding=3)


def powerline(fg: str = "light", bg: str = "dark") -> widget.TextBox:
    """
    Creates a triangle-shaped separator using a Nerd Font icon, styled with the given theme colors.

    This widget simulates a powerline transition effect between sections of the bar.

    Parameters:
        fg (str): Foreground color key from the theme. Defaults to "light".
        bg (str): Background color key from the theme. Defaults to "dark".

    Returns:
        widget.TextBox: A TextBox widget displaying a triangular glyph with styling.
    """
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        # padding=-1,
    )


def workspaces() -> List[Union[widget.Sep, widget.GroupBox]]:
    """
    Creates a GroupBox widget to display workspaces, along with a separator.

    The GroupBox shows active, inactive, urgent, and focused workspace states
    using colors from the theme. It disables dragging and uses block highlights.

    Returns:
        list: A list containing a separator and a styled GroupBox widget.
    """
    return [
        separator(),
        widget.GroupBox(
            **base(fg="light"),
            font="UbuntuMono Nerd Font",
            fontsize=22,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors.get("active") or "#f1ffff",
            inactive=colors.get("inactive") or "#4c566a",
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors.get("urgent") or "#F07178",
            this_current_screen_border=colors.get("focus") or "#a151d3",
            this_screen_border=colors.get("grey") or "#353c4a",
            other_current_screen_border=colors.get("dark") or "#0f101a",
            other_screen_border=colors.get("dark") or "#0f101a",
            disable_drag=True,
        ),
    ]


primary_widgets: List[Any] = [
    *workspaces(),
    widget.Spacer(),
    # ------------ Displays the number of available system package updates ------------
    powerline(fg="color8", bg="dark"),
    icon(bg="color8", text=" "),  # Icon: nf-fa-download
    widget.CheckUpdates(
        font="UbuntuMono Bold Italic",
        fontsize=14,
        fmt="{}",
        background=colors.get("color8") or "#ffd47e",
        colour_have_updates=colors.get("text") or "#0f101a",
        colour_no_updates=colors.get("text") or "#0f101a",
        no_update_string="0",
        display_format="{updates}",
        update_interval=1,
        custom_command="checkupdates",
        distro="Arch_checkupdates",
    ),
    # ------------ Displays and controls the system audio volume using PulseAudio ------------
    powerline(fg="color7", bg="color8"),
    icon(bg="color7", text=" "),  # Icon: nf-fa-volume_high
    widget.PulseVolume(
        **base(bg="color7"),
        channel="Master",
        mute_format="Muted",
        mouse_callbacks={"Button1": lambda: qtile.spawn("pavucontrol")},
        fmt="{}",
    ),
    # ------------ Shows current RAM usage, including used and total memory ------------
    powerline(fg="color6", bg="color7"),
    icon(bg="color6", text="󱐋"),  # Icon: nf-md-lightning_bolt
    widget.Memory(
        **base(bg="color6"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        format="{MemUsed: .2f}{mm} /{MemTotal: .2f}{mm}",
        mouse_callbacks={"Button1": lambda: qtile.spawn("/bin/alacritty -e htop")},
        fmt="{}",
        update_interval=1,
    ),
    # ------------ Displays the current CPU usage as a percentage ------------
    powerline(fg="color5", bg="color6"),
    icon(bg="color5", text=" "),  # Icon: nf-oct-cpu
    widget.CPU(
        **base(bg="color5"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        fmt="{}",
        update_interval=1,
    ),
    # ------------ Shows current network upload and download speeds ------------
    powerline(fg="color4", bg="color5"),
    icon(bg="color4", text=" "),  # Icon: nf-fa-feed
    widget.Net(
        **base(bg="color4"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        fmt="{}",
        interface=open(file=interface_path, mode="r").read().strip(),
        update_interval=1,
    ),
    # ------------ Displays an icon representing the current window layout ------------
    powerline(fg="color3", bg="color4"),
    widget.CurrentLayout(
        **base(bg="color3"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        scale=0.65,
        mode="icon",
    ),
    # ------------ Shows the name of the currently active layout ------------
    widget.CurrentLayout(
        **base(bg="color3"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        padding=5,
        fmt="{}",
    ),
    # ------------ # Provides a system tray for app icons (e.g. volume, network) ------------
    powerline(fg="dark", bg="color3"),
    widget.Systray(
        fmt="{}",
        background=colors.get("dark") or "#0f101a",
        padding=5,
    ),
]

secondary_widgets: List[Any] = [
    # ------------ Workspace separator ------------
    *workspaces(),
    # ------------ Spacer to fill the space between widgets ------------
    separator(),
    # ------------ Displays an icon representing the current window layout ------------
    powerline(fg="color1", bg="dark"),
    widget.CurrentLayout(
        **base(bg="color1"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        scale=0.65,
        mode="icon",
    ),
    # ------------ Shows the name of the currently active layout ------------
    widget.CurrentLayout(
        **base(bg="color1"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        padding=5,
        fmt="{}",
    ),
    # ------------ Shows the current date and time in a customizable format ------------
    powerline(fg="color2", bg="color1"),
    widget.Clock(
        **base(bg="color2"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        format="%A, %d of %B %Y - %I:%M:%S %p ",
    ),
    powerline(fg="dark", bg="color2"),
]

bottom_widgets: List[Any] = [
    # ------------ Displays the title of the currently focused window ------------
    widget.WindowName(
        **base(fg="focus"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        padding=5,
        max_chars=195,
    ),
    # ------------ Displays custom text output by polling a shell command at intervals ------------
    powerline(fg="color2", bg="dark"),
    widget.GenPollText(
        **base(bg="color2"),
        func=lambda: check_output(
            args='printf "Arch Linux $(uname -r)"', shell=True, text=True
        ),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        padding=5,
        fmt="❤ {}",
        update_interval=86400,
    ),
    # ------------ Shows the current date and time in a customizable format ------------
    powerline(fg="color1", bg="color2"),
    icon(bg="color1", fontsize=17, text="󰃰 "),  # Icon: nf-md-calendar_clock
    widget.Clock(
        **base(bg="color1"),
        font="UbuntuMono Bold Italic",
        fontsize=14,
        format="%A, %d of %B %Y - %H:%M:%S %p ",
    ),
]


widget_defaults: Dict[str, Union[str, int]] = {
    "font": "UbuntuMono Nerd Font Bold Italic",
    "fontsize": 16,
    "padding": 1,
}
extension_defaults: Dict[str, Union[str, int]] = widget_defaults.copy()
