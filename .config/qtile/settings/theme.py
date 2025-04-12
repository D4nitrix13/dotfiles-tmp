"""
Theme loader for Qtile.

This script sets up the current Qtile theme by:
1. Executing a theme setup script if it exists.
2. Loading the desired theme name from a JSON config.
3. Falling back to a default theme if necessary.
4. Loading color definitions and image paths associated with the theme.

Requires:
- settings.path: must define 'home' and 'qtile_path' variables.
- config.json in qtile_path: must include a 'theme' key.
- themes/[theme_name]/colors.json
- themes/[theme_name]/img/ (directory of image files)
"""

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

import json
import subprocess
from io import TextIOWrapper
from os import listdir, path
from typing import Dict

from settings.path import home, qtile_path

f: TextIOWrapper
default_theme: str = "dark-grey"

theme_setup_script: str = path.join(home, ".theme", "set-themes.py")

if path.isfile(path=theme_setup_script):
    subprocess.call(args=[theme_setup_script, "qtile"])

with open(file=path.join(qtile_path, "config.json"), mode="r") as f:
    theme: str = json.load(fp=f).get("theme")

theme_path: str = path.join(qtile_path, "themes", theme)

if not path.isdir(s=theme_path):
    theme_path = path.join(qtile_path, "themes", default_theme)

# Map color name to hex values
with open(file=path.join(theme_path, "colors.json"), mode="r") as f:
    colors: Dict[str, str] = json.load(f)

# Map image name to its path
img: Dict[str, str] = dict()
img_path: str = path.join(theme_path, "img")
i: str


def get_image_name(*, image: str) -> str:
    """
    Extracts the base name of an image file without its extension.

    Parameters:
        image (str): The image file name (e.g., 'bar1.jpg').

    Returns:
        str: The name of the image without the file extension (e.g., 'bar1').

    Raises:
        ValueError: If the input string does not contain a period separator.
    """
    name: str
    extension: str
    name, extension = image.split(sep=".")

    return name


for i in listdir(path=img_path):
    name: str = get_image_name(image=i)
    img[name] = path.join(img_path, i)
