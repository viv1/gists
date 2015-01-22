#!/bin/bash

#This script extracts motivational quotes from a given website and reads it out loud after  certain interval

#This code also gets us the nth line
#head -5 quotes.txt > test.txt
#line=tail -1 test.txt

for i in {1..3}
do
sed "${i} q;d" quotes.txt > test.txt
say -f test.txt
done

