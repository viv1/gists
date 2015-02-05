#!/bin/bash

#This script hibernates the system, when the battery power left is lt 5%.

#Checks for battery power and stores the result in text.txt

upower -d|grep perc  > text.txt  	#Specific line
sed 's/%//g' text.txt > newt.txt	#Remove %

awk '/[0-9]/{print $1}' RS=" " newt.txt > text.txt #Extract number and store in text.txt

battery_left=`cat text.txt`

#IMP NOTE
#Run sudo VISUAL=vim crontab -e -u root and append the line @reboot /path/to/script to the bottom of the file, then the root user will automagically run your script as root on login. And a friendly reminder to make sure nobody apart from you and root can access the script, otherwise people could run any command as root.

if [ "$battery_left" -lt "6" ]; then
	pm-hibernate
fi


