"""
This script defines the file paths related to the user's Qtile configuration.

It expands the home directory path and constructs the full path to the Qtile configuration
directory within the user's home directory.

Variables:
- home (str): The expanded path to the user's home directory.
- qtile_path (str): The full path to the user's Qtile configuration directory.

This script can be used to reference Qtile configuration files for further automation or customizations.
"""

from os import path

home: str = path.expanduser(path="~")
qtile_path: str = path.join(home, ".config", "qtile")
