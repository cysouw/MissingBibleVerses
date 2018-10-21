#!/usr/bin/env python3

# merge complete bible with addition, overwriting verses with new versions
# output a copy into ../complete

import sys
import re
from os import path

def make_dict(bible):
    # turn bible into dictionary
    bible = bible.readlines()
    
    # separate metadata
    metadata = [line for line in bible if re.match("#", line)]
    
    # dictionary with verse numbers as key
    lines = [(line[0:8], line[9:]) for line in bible if re.match("\d", line)]
    text_dict = dict(list(lines))

    return metadata, text_dict
    
def main(filename):
    
    origin = path.join('../../corpus/bibles/corpus', filename)
    result = path.join('../complete', filename)
    
    with open(origin, 'r', encoding='utf8') as o, open(filename, 'r', encoding='utf8') as f:
        
        raw = make_dict(o)
        meta = raw[0]
        text = raw[1]
        
        add = make_dict(f)
        add = add[1]
        
        for line in add:
            text[line] = add[line]
        
        # merge back and write out
        if text:
            text = ['\t'.join(x) for x in zip(text.keys(), text.values())]
            text = sorted(text)
            
            with open(result, 'w') as f:
                for line in meta:
                    f.write(line)
                for line in text:
                    f.write(line)


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        main(filename)