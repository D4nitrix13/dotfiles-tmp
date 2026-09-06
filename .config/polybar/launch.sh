#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
/bin/killall -q polybar

## Wait until the processes have been shut down
while /bin/pgrep -u $UID -x polybar >/dev/null; do /bin/sleep 1; done

## Launch

## Left bar
/bin/polybar distro -c ~/.config/polybar/current.ini &
/bin/polybar date -c ~/.config/polybar/current.ini &
/bin/polybar ethernet -c ~/.config/polybar/current.ini &
/bin/polybar vpn -c ~/.config/polybar/current.ini &

## Right bar
# /bin/polybar top -c ~/.config/polybar/current.ini &
/bin/polybar machine -c ~/.config/polybar/current.ini &
/bin/polybar power_button -c ~/.config/polybar/current.ini &

## Center bar
/bin/polybar primary -c ~/.config/polybar/workspace.ini &
