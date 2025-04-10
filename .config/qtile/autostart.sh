#!/bin/sh

# systray battery icon
if [ -d /sys/class/power_supply/BAT0 ]; then
  cbatticon -u 5 &
fi

# Keyborad Latam
if [[ "$(setxkbmap -query | tail -n 1 | xargs | awk '{print $2}')" != "latam" ]]; then
  setxkbmap latam
fi

# systray volume
volumeicon &
