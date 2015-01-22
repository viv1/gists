#!/bin/bash

#This script reads lines from the file where we extracted our quotes and reads it out loud after certain interval(20 min.). The contents are preprocessed slightly to make more sense.

#This code also gets us the nth line
#head -5 quotes.txt > test.txt
#line=tail -1 test.txt

sed 's/[0-9]/" "/g' original_quotes.txt > helper.txt   #Convert numbers to blank
sed 's/~/told by /g' helper.txt > quotes.txt		#Convert ~ to "told by"

#Beware of using tr.It translates only one character to another single character.
#Here, it reads ".." and "..."  as ".":
#cat quotes.txt | tr [:digit:] ".." | tr "..." " " > test.txt
#cat test.txt | tr "~" "told by  " > quotes.txt

for i in {1..99}
do
sed "${i} q;d" quotes.txt > helper.txt 		# Get the i'th line
cat helper.txt					# display the line
say -f helper.txt				# Read the line
sleep 1200					# Go to sleep for 20 minutes(1200 sec)
done

