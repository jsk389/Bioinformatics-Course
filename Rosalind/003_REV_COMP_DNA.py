# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:06:52 2015

@author: James
"""

"""
Problem:
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' 
and 'G'. The reverse complement of a DNA string s is the string sc formed by 
reversing the symbols of s, then taking the complement of each symbol (e.g., 
the reverse complement of "GTCA" is "TGAC").
"""

from string import maketrans

string = 'AAAACCCGGT'
print(string)
print(string[::-1])

# Dictionary containing DNA complements
#dic = {'A': 'T', 'T': 'A',
#       'C': 'G', 'G': 'C'}
DNA = 'ATCG'
complement = 'TAGC'
translation_table = maketrans(DNA, complement)

print(string[::-1].translate(translation_table))