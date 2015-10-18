# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:26:42 2015

@author: James
"""

import collections, random, operator
import numpy as np

"""
Simple code designed to solve counting DNA nucleotides
problem in Rosalind DNA problems
"""

def counting_nucleotides(string):
    # Return each base and number of occurrences
    count = {}
    for n in range(len(string)):
        c = string[n]
        print(c)
        print(count)
        if count.has_key(c):
            count[c] += 1
        else:
            count[c] = 1
 
   
    x = []
    for key, value in count.iteritems():
        x.append((key, value))
    return x

# Import file
string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
#string = np.genfromtxt('rosalind_dna.txt', dtype='str')
x = counting_nucleotides(string)

print(x)
