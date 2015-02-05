#!/bin/bash

#This script hibernates the system, when the battery power left is lt 5%.

#Checks for battery power and stores the result in text.txt

upower -d|grep perc  > text.txt  	#Specific line
sed 's/%//g' text.txt > newt.txt	#Remove %

awk '/[0-9]/{print $1}' RS=" " newt.txt > text.txt #Extract number and store in text.txt



