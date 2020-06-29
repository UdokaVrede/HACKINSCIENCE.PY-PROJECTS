#!/usr/bin/env python3

def longest_word(text):
    words=text.split()
    length=len(words)
    
    #pit=list(map(len, words))
    max=0
    idx=0
    for p in range(length):
        pit=len(words[p])
        if(pit > max):
            max=pit
            idx=p
            
    return words[idx]
