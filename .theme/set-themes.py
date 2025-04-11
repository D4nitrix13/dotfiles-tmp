#!/usr/bin/env python

import json
import subprocess
from io import TextIOWrapper
from os import path
from sys import argv
from typing import Dict


def main() -> None:
    wm: str = argv[1]
    home: str = path.expanduser("~")
    f: TextIOWrapper

    with open(file=path.join(home, ".theme", "theme.json")) as f:
        theme: Dict[str, str] = json.load(fp=f).get(wm)

    # subprocess.call(
    #     [path.join(home, ".config", "alacritty", "theme.py"), theme["alacritty"]]
    # )

    if wm == "qtile":
        qtile_theme_file = path.join(
            path.expanduser("~"), ".config", "qtile", "config.json"
        )

        with open(file=qtile_theme_file) as f:
            qtile_config: Dict[str, str] = json.load(fp=f)

        qtile_config["theme"] = theme.get("wm") or "material-ocean"

        with open(file=qtile_theme_file, mode="w") as f:
            json.dump(obj=qtile_config, fp=f)

    subprocess.call(args=["notify-send", "-u", "normal", "Theme Set!"])
    return None


if __name__ == "__main__":
    main()
