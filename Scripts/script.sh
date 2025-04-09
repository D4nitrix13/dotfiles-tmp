#!/usr/bin/env bash

path="/home/d4nitrix13/Wallpapers/JPG"

list=("$path"/*)

index=$(($RANDOM % ${#list[@]}))

echo "${list[$index]}"
