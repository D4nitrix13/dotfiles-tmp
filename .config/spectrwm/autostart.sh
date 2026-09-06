#!/bin/bash

# Keyborad Latam
# Launch the battery icon in the system tray if a battery device is detected
if [ -d /org/freedesktop/UPower/devices/battery_BAT0 ]; then
  /bin/cbatticon -i standard -u 15 -l 20 -r 10 -n &
fi

# Set keyboard layout to Latin American if it's not already set
if [[ "$(setxkbmap -query | tail -n 1 | xargs | awk '{print $2}')" != "latam" ]]; then
  /bin/setxkbmap latam
fi

# Enable NumLock if it's currently off
if xset q | grep -iq "Num Lock: *off"; then
  /bin/numlockx on
fi

trayer \
  --edge top \
  --align right \
  --monitor 0 \
  --widthtype request \
  --heighttype request \
  --height 20 \
  --alpha 0 \
  --transparent true \
  --tint 0x0F101A \
  --SetDockType false \
  --SetPartialStrut false \
  --iconspacing 5 \
  --margin 715 &>/dev/null &
disown

if [ -f ~/.theme/set-themes.py ]; then
  python ~/.theme/set-themes.py "spectrwm" &
fi
