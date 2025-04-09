from libqtile import widget
from settings.theme import colors, img


base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = {
    **base(),
    'linewidth': 0,
    'padding': 5,
}

text_box = lambda fontsize = 22: {
    'font': 'UbuntuMono Nerd Font Mono:style=Bold Italic',
    'fontsize': fontsize,
    'padding': 5
}

workspaces = lambda: [
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=24,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['light'],
        inactive=colors['light'],
        rounded=False,
        highlight_method='block',
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark']
    ),
    widget.Sep(**separator),
    widget.Sep(**separator),
]

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

top_widgets = [
    *workspaces(),
    widget.Spacer(),
    widget.Systray(
        background=colors['dark'],
        padding=7
    ),
    widget.Sep(**separator),
    widget.Image(filename=img['bar4']),
    widget.TextBox(
        **base(bg='color4'),
        **text_box(fontsize=24),
        text=''  # Icon: nf-fa-download
    ),
   widget.CheckUpdates(
        **base(bg='color4'),
        distro='Arch_checkupdates',
        execute='alacritty',
        update_interval=1,
        no_update_string="Updates: 0",
        fmt="{} "
    ),

    widget.Image(
        filename=img['bar3']
    ),
    widget.TextBox(
        **base(bg='color3'),
        **text_box(fontsize=24),
        text=''  # Icon: nf-fa-feed
    ),
    widget.Net(
        **base(bg='color3'),
        interface='enp10s0',
        fmt="{} "
    ),
    widget.Image(
        filename=img['bar2']
    ),
    widget.CurrentLayoutIcon(
        **base(bg='color2'),
        scale=0.65
    ),
    widget.CurrentLayout(
        **base(bg='color2'),
        padding=5
    ),
    widget.Image(
        filename=img['bar1']
    ),
    widget.TextBox(
        **base(bg='color1'),
        **text_box(fontsize=24),
        text='󰃰'  # Icon: nf-md-calendar_clock
    ),
    widget.Clock(
        **base(bg='color1'),
       format='%A, %d of %B %Y - %I:%M:%S %p '
    ),
]


bottom_widgets = [
    widget.Sep(**separator),
    widget.WindowName(
        **base(fg='focus'),
        font='UbuntuMono Bold Italic',
        fontsize=16,
        padding=5
    ),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Mono Bold Italic',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
