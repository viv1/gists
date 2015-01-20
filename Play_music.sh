#!/bin/bash

#Script to select all the media in the given folder and play it using vlc

DIR_2="/media/vivek/7E36D45836D4134F/Users/vivek/Downloads"

#To tell it to only split on newlines

IFS=$'\n' # Very important otherwise treats filenames with spaces between them as separate files.(so big cause of headache)

#The shell reads the IFS variable, which is which is set to <space><tab><newline> by default.

#Then it looks at each character in the output of find. As soon as it sees any character that's in IFS, it thinks that marks the end of the file name, so it sets file to whatever characters it saw until now and runs the loop. Then it starts where it left off to get the next file name, and runs the next loop, etc., until it reaches the end of output.

<<COMMENT 
	...since a much more elegant solution found 

	for i in $DIR_2/*.{mp3,mpeg};
	do
		#echo $i "1111111111111111111111"
		vlc file://$i
		vlc vlc://quit
	done

COMMENT

#Elegant one line solution
vlc --random --loop $DIR_2/*.{mpeg,mp3,mp4,mpg,flv,avi,mkv}

