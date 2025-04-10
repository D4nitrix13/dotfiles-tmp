"""
Qtile workspace and keybinding configuration using Nerd Font icons.

This script defines visual workspace groups using Nerd Font icons and sets up keybindings to:
1. Switch to a workspace (Mod + [1–6]).
2. Move the focused window to a workspace (Mod + Shift + [1–6]).

Dependencies:
- Nerd Font must be installed for icons to display correctly.
- settings.keys must define `keys` (List[Key]) and `mod` (modifier key, e.g., "mod4").

Icons used (with Nerd Font codes):
- 󰈹 : Browser (nf-md-firefox)
-  : Code editor (nf-dev-vscode)
-  : Terminal (nf-dev-terminal)
- 󱍙 : Music folder (nf-md-folder_music)
-  : Image viewer (nf-fa-image)
- 󰌨 : Layers or misc (nf-md-layers)
"""

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

for i, group in enumerate(iterable=groups, start=1):
    current_key: str = str(i)
    keys.extend(
        [
            # Switch to workspace N
            Key(
                [mod],  # Modifiers
                current_key,  # Key
                lazy.group[group.name].toscreen(),  # Commands
            ),
            # Send window to workspace N
            Key(
                [mod, "shift"],  # Modifiers
                current_key,  # Key
                lazy.window.togroup(group.name),  # Commands
            ),
        ]
    )
