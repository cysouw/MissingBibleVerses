# Correcting missing verses in the Parallel Bible Corpus

# Format of corrections

For each bible, potentially missing verses were collected. Each file in this repository just list the verse numbers that might be missing. Any corrections/additions should be added after these numbers. As long as there is a line break immediately after a number, this number is considered as **not checked** and needs to be checked.

The following kind of corrections are possible:

* **remove the number**: this means that the verse is not missing at all, but is simply not translated. When all numbers in a specific file are removed, then the whole file can be removed.
* **add only a tab after a number**: this will be the most common situation. It means that the verse is translated as part of the immediately preceding verse in the bible. This happens quite often, as we find indications like `13-15` in bibles, meaning that verses 13, 14, and 15 are translated as one verse. In such a situation we include the complete text after the first number (i.e. after 13) and add two empty verses for 14 and 15. To indicate such an empty verse, only a tab mark is added after the number, and nothing else. Unfortunately, it seems like these empty verses are regularly omitted in the conversion, specifically in bibles from the website www.bible.is (this website often ignores the indication of multiple verses, just listing `13` in the above exmple).
* **add a tab and the text**: sometimes there is indeed a verse missing, in which case the text should be added after a tab. There is no need to separate punction, that will be done at the end.

All other problems should be noted at the start of the file after a hash `#` symbol at the start of the line.

# Format Description of Bible texts

The format for the Bible texts has the following structure. Each line contains two elements which are separated by a TAB. The first element is the verse ID and the second element contains the actual text. The verse ID contains information about the book, chapter and verse number and is structured as follows (for the example of the verse ID 40001003):

* the first two digits represent the number of the book (e.g. 40 refers to the first book in the New Testament, the Gospel according to Matthew). The correspondences between book names and numbers are given below.
* the next three digits indicate the chapter (e.g. 001 refers to the first chapter in the book)
* the last three digits show the verse number (e.g. 003 refers to the third verse in the chapter)

Some lines contain only a verse ID and a TAB, but no actual text. In these cases, the translation of the respective verse ID is combined into the last preceding full text line above the empty text line. For example, when ID 400001003 has no text, but ID 400001002 (directly preceding) contains text, then one can assume that the content of ID 400001003 is available somewhere inside that text of ID 400001002, but it is not easy to separate the content.

# Bible Book IDs

## Old Testament

* 01 : Genesis 
* 02 : Exodus 
* 03 : Leviticus 
* 04 : Numbers 
* 05 : Deuteronomy 
* 06 : Joshua 
* 07 : Judges 
* 08 : Ruth 
* 09 : 1 Samuel 
* 10 : 2 Samuel 
* 11 : 1 Kings 
* 12 : 2 Kings 
* 13 : 1 Chronicles 
* 14 : 2 Chronicles 
* 15 : Ezra 
* 16 : Nehemiah 
* 17 : Esther 
* 18 : Job 
* 19 : Psalms 
* 20 : Proverbs 
* 21 : Ecclesiastes 
* 22 : Song of Solomon 
* 23 : Isaiah 
* 24 : Jeremiah 
* 25 : Lamentations 
* 26 : Ezekiel 
* 27 : Daniel 
* 28 : Hosea 
* 29 : Joel 
* 30 : Amos 
* 31 : Obadiah 
* 32 : Jonah 
* 33 : Micah 
* 34 : Nahum 
* 35 : Habakkuk 
* 36 : Zephaniah 
* 37 : Haggai 
* 38 : Zechariah 
* 39 : Malachi 

## New Testament

* 40 : Matthew 
* 41 : Mark 
* 42 : Luke 
* 43 : John 
* 44 : Acts 
* 45 : Romans 
* 46 : 1 Corinthians 
* 47 : 2 Corinthians 
* 48 : Galatians 
* 49 : Ephesians 
* 50 : Philippians 
* 51 : Colossians 
* 52 : 1 Thessalonians 
* 53 : 2 Thessalonians 
* 54 : 1 Timothy 
* 55 : 2 Timothy 
* 56 : Titus 
* 57 : Philemon 
* 58 : Hebrews 
* 59 : James 
* 60 : 1 Peter 
* 61 : 2 Peter 
* 62 : 1 John 
* 63 : 2 John 
* 64 : 3 John 
* 65 : Jude 
* 66 : Revelation

## Apocryphal Books

books in brackets added elsewhere, see below

* 67 : Tobit
* 68 : Judith
* 69 : Greek version of Esther
* 70 : Wisdom of Solomon
* 71 : Ecclesiasticus 'Sirach'
* 72 : Baruch
* (73 : Epistle of Jeremiah)
* (74 : Prayer of Azariah)
* (75 : Susanna)
* (76 : Bel and the Dragon)
* 77 : 1 Maccabees
* 78 : 2 Maccabees
* 79 : 3 Maccabees
* 80 : 4 Maccabees
* 81 : 1 Esdras
* 82 : 2 Esdras
* 83 : Prayer of Manasseh
* 84 : Psalm 151
* 85 : Psalm of Solomon
* 86 : Odes