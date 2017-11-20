#!/bin/sh

# script to add all missing verses from bible.is bibles to the texts

for missing in "$@" ;

do
	text=../../corpus/bibles/corpus/$missing
	if
		head -10 $text | grep -q 'bible.is'
	then
		sed $'s/$/\t/g' $missing | sponge $missing
		grep '^#' $text > ../new/$missing
		grep '^\d' $text | cat - $missing | sort >> ../new/$missing
		mv $missing ../done/$missing
	fi
done
