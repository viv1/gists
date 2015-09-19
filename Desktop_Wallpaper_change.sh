#!/bin/bash

# This script automates the changing of the Desktop Wallpaper.
#that is, it changes wallpaper after every 100 seconds and uses images from Downloads directory for use.

#To  check version of Gnome
# "gnome-session --version"
#If version is >=3, gsettings should be used

#To get current uri of the background image
# "gsettings get org.gnome.desktop.background picture-uri"

#To set the background URI,
# "gsettings set org.gnome.desktop.background picture-uri file:///home/vivek/.local/share/eog-wallpaper.jpg"


#Select Directory containing picture elements
DIR="/home/vivek/Downloads"


#Select an image(by selecting from formats jpeg,jpg,png)
#PIC=$(ls $TEST_DIR/*.jpeg $TEST_DIR/*.png $TEST_DIR/*.jpg |shuf -n1)
#PIC=$(ls $DIR/*.{jpeg,png,jpg}|shuf -n1)  # Better(since shorter)

#echo $PIC

PIC_all=$(ls $DIR/*.{jpeg,png,jpg})
for i in $PIC_all; do
	gsettings set org.gnome.desktop.background picture-uri file://$i
	sleep 100
done

#Set it as a desktop wallpaper
#gsettings set org.gnome.desktop.background picture-uri file://$PIC


