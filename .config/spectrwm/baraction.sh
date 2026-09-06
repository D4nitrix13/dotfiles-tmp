#!/bin/bash

# baraction.sh For Spectrwm Status Bar
# https://github.com/conformal/spectrwm

icon() {
  echo -n "+@fg=1;$1 +@fg=0;"
}

percentage() {
  current=$(echo $1 | sed 's/%//')
  if [ $current -le 25 ]; then
    echo -n "$(icon $2)"
  elif [ $current -le 50 ]; then
    echo -n "$(icon $3)"
  elif [ $current -le 75 ]; then
    echo -n "$(icon $4)"
  else
    echo -n "$(icon $5)"
  fi
}

declare -i SLEEP_SEC=1
declare -i i=0

while :; do
  # ------------ Updates ------------
  if (($i % 60 == 0)); then
    updates=$(checkupdates | wc -l)
  fi
  #  -> nf-fa-download
  echo -n "$(icon ) $updates "

  # ------------ Brightness ------------
  # nf-md-brightness_7 -> 󰃠
  # nf-md-brightness_6 -> 󰃟
  # nf-md-brightness_5 -> 󰃞
  # nf-md-brightness_4 -> 󰃝
  # (( br = $(brightnessctl get) * 100 / 255 ))
  # echo -n "$(percentage $br 󰃝  󰃞  󰃟  󰃠 ) $br% "

  # ------------ Volume ------------
  # nf-fa-volume_xmark -> 
  # nf-fa-volume_off -> 
  # nf-fa-volume_down -> 
  # nf-md-volume_high -> 󰕾
  # nf-fa-volume_high -> 
  declare -i vol=$(pamixer --get-volume)
  if [[ $(pamixer --get-mute) == "true" ]]; then
    echo -n "$(icon ) $vol% "
  else
    if [[ $vol -ge 80 ]]; then
      echo -n "$(percentage $vol   󰕾 ) $vol% "
    else
      echo -n "$(percentage $vol   󰕾 )$vol% "
    fi
  fi

  # ------------ Disk ------------
  # device="/dev/nvme1n1p3"
  # hdd="$(df -h $device | awk 'NR==2{print $3, $5}')"
  # echo -n "$(icon ) $hdd "

  # ------------ Battery ------------
  # nf-fa-battery_1 -> 
  # nf-fa-battery_2 -> 
  # nf-fa-battery_3 -> 
  # nf-fa-battery_4 -> 
  # nf-weather-lightning -> 
  battery_path=false

  if upower -e | grep -iq "/org/freedesktop/UPower/devices/battery_BAT1"; then
    battery_path="/org/freedesktop/UPower/devices/battery_BAT1"
  elif upower -e | grep -iq "/org/freedesktop/UPower/devices/battery_BAT0"; then
    battery_path="/org/freedesktop/UPower/devices/battery_BAT0"
  fi

  if [[ "$battery_path" != "false" ]]; then
    if ((i % 60 == 0)); then
      bat=$(upower -i "$battery_path" | grep percentage | sed 's/ *percentage: *//g')
      state=$(upower -i "$battery_path" | grep state | sed 's/ *state: *//g')
    fi

    if [[ "$state" == "charging" || "$state" == "fully-charged" ]]; then
      echo -n "$(icon )"
    else
      echo -n "$(percentage "$bat"    )"
    fi

    echo -n "$bat "
  fi

  # ------------ Cpu ------------
  # nf-oct-cpu -> 
  # read cpu a b c previdle rest </proc/stat
  # declare -i prevtotal=$((a + b + c + previdle))
  # sleep 0.5
  # read cpu a b c idle rest </proc/stat
  # declare -i total=$((a + b + c + idle))
  # declare -i cpu=$((100 * ((total - prevtotal) - (idle - previdle)) / (total - prevtotal)))
  # printf "$(icon ) %.1f%% " "$cpu"

  # ------------ Memory ------------
  mem=$(free | awk '/Mem/ {printf "%.2f MiB/%.2f MiB\n", $3 / 1024.0, $2 / 1024.0 }')
  echo -n "$(icon ) $mem "

  # ------------ Date ------------
  # nf-md-calendar_clock -> 󰃰
  # if (( $i % 60 == 0 )); then
  #     dte="$(date +"$(icon 󰃰) %d/%m/%Y $(icon ) %H:%M:%S %p ")"
  # fi
  dte="$(date +"$(icon 󰃰) %d/%m/%Y $(icon ) %H:%M:%S %p ")"
  echo -e "$dte"

  sleep $SLEEP_SEC
  ((i += $SLEEP_SEC))
done

# +@fg=1;

