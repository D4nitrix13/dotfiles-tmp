from typing import List

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings.keys import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:
# nf-fa-firefox,
# nf-fa-code_fork,
# nf-dev-terminal,
# nf-mdi-folder,
# nf-mdi-image,
# nf-mdi-layers

# 󰈹 -> nf-md-firefox
#  -> nf-dev-vscode
#  -> nf-dev-docker
#  -> nf-dev-terminal
# 󱍙 -> nf-md-folder_music
#  -> nf-fa-image
# 󰌨 -> nf-md-layers

i: int
g: str

groups: List[Group] = [
    Group(name=g) for g in [" 󰈹  ", "   ", "   ", " 󱍙  ", "   ", " 󰌨  "]
]

for i, group in enumerate(iterable=groups, start=0):
    current_key: str = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key(
                modifiers=[mod], key=current_key, desc=lazy.group[group.name].toscreen()
            ),
            # Send window to workspace N
            Key(
                modifiers=[mod, "shift"],
                key=current_key,
                desc=lazy.window.togroup(group.name),
            ),
        ]
    )
