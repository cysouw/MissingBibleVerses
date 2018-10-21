#!/usr/bin/env bash

# use with dir 'ready' to produce complete bible, separate punctuation, and produce stats for checking

for file in $@

do

	../scripts/merge.py $file
	../scripts/separate_punctuation.py ../complete/$file > ../stats/${file%.*}_separation.txt
	../../corpus/scripts/makeStats -o ../stats ../complete/$file

done
