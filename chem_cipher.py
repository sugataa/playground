# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:43:56 2014

@author: Sugata Acharjya
"""
import shelve

# create a container for the cleaned up list
dbase = shelve.open("chem_list")

# take in a list of elements that 
#file = open("element_list.txt", "r")
#for line in file:
#    symbol = line.split('-')[1].strip().lower()
#    name = line.split('-')[2].strip()
#    #print line.split('-')
#    dbase[symbol] = name

#for name in dbase.keys():
#    print name
    
#TODO: problem is that i dont know which sentences are valid?
    # most aren't

sentence = 'back that ass up'

def transform(sent):
    out = ""
    i = 0
    
    while i < len(sent)-1 and i%2 == 0:
        letters = sent[i:i+2]
        if letters in dbase.keys():
            out += dbase[letters]
        elif letters[0] in dbase.keys() and letters[1] in dbase.keys():
            out += dbase[letters[0]]
            out += " "
            out += dbase[letters[1]]
        else:
            return False
        out += " "
        i+=2
    if len(sent)%2 != 0:
        out += dbase[sent[-1]]
    return out
    
output = transform(sentence.replace(" ", "").lower())
print output
    
    
