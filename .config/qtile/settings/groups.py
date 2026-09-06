"""
Qtile workspace and keybinding configuration using Nerd Font icons.

This script defines visual workspace groups using Nerd Font icons and sets up keybindings to:
1. Switch to a workspace (Mod + [1-9]).
2. Move the focused window to a workspace (Mod + Shift + [1-9]).

Dependencies:
- Nerd Font must be installed for icons to display correctly.
- settings.keys must define `keys` (List[Key]) and `mod` (modifier key, e.g., "mod4").

Icons used (with Nerd Font codes):

- 󰈹 : Web Browsers & Research (nf-md-firefox)
-  : Code Editors & IDEs (nf-dev-vscode)
-  : Terminals & Shells (nf-dev-terminal)
- 󱍙 : Music & Media Players (nf-md-folder_music)
- 󰈙 : Documents & Notes (nf-md-file_document)
-  : Image & Graphics Viewers (nf-fa-image)
-  : Containers & DevOps (nf-dev-docker)
-  : System Configuration & Tools (nf-seti-config)
- 󰌨 : Miscellaneous & Experiments (nf-md-layers)
"""

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from typing import List

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings.keys import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:

# 󰈹 -> nf-md-firefox
#  -> nf-dev-vscode
#  -> nf-dev-terminal
# 󱍙 -> nf-md-folder_music
# 󰈙 -> nf-md-file_document
#  -> nf-fa-image
#  -> nf-dev-docker
#  -> nf-seti-config
# 󰌨 -> nf-md-layers

i: int
g: str

groups: List[Group] = [
    Group(name=g)
    for g in [" 󰈹  ", "   ", "   ", " 󱍙  ", " 󰈙  ", "   ", "   ", "   ", " 󰌨  "]
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
