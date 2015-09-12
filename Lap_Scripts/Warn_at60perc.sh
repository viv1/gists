#!/bin/bash

#This script warns when the battery is below a specified value(60).

# Add it to crontab (run crontab -e) to keep the script running after every 1 minute by adding the following line:

#	/1 * * * * bash Pathto/Warn_at60perc.sh 

upower -d|grep perc  > text.txt  	#Specific line
sed 's/%//g' text.txt > newt.txt	#Remove %

awk '/[0-9]/{print $1}' RS=" " newt.txt > text.txt #Extract number and store in text.txt

battery_left=`cat text.txt`

ifCharging=`upower -d|grep online`		#Check if already charging

if [ $battery_left -lt 60 ] && [[ $ifCharging == *"online"*"no"* ]];then say "Plug in power source";fi
