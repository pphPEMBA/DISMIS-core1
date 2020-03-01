#!/bin/bash

# This script changes the wallpaper to a random wallpaper in the base wallpaper folder mentioned.

# Change this to the root of your wallpaper folder.
BASE_WALLPAPER_FOLDER_PATH="/home/adarsh/Personal/Wallpapers"

while true; do
	# generating a random path in the tree of the base wallpaper folder.
	random_path="$(find $BASE_WALLPAPER_FOLDER_PATH | shuf -n1)"

	# checking if the generated path is a file.
	if [[ -f $random_path ]]; then
		# changing the wallpapar to this file.
		gsettings set org.gnome.desktop.background picture-uri "file://$random_path"
		echo "Wallpaper changed successfully."
		break
	fi
done
