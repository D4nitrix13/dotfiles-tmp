#!/bin/sh


# systray battery icon
if [ -d /sys/class/power_supply/BAT0 ]; then
    cbatticon -u 5 &
fi

# systray volume
volumeicon &
