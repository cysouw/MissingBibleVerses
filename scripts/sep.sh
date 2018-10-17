#! /bin/bash

for file in ach-x-bible.txt afr-x-bible-1953.txt afr-x-bible-1983.txt agg-x-bible.txt afr-x-bible-lewende.txt

do
	../scripts/separate_punctuation.py $file > ../punctuation/$file
done
	