# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:26:42 2015
@author: James

Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
"""

import collections, random, operator
import numpy as np


def counting_nucleotides(string):
    # Return each base and number of occurrences
    count = {}
    for n in range(len(string)):
        c = string[n]
        if count.has_key(c):
            count[c] += 1
        else:
            count[c] = 1
 
    # Read final values out to list
    # Keys are not kept but can be using commented out part
    x = []
    for key, value in count.iteritems():
        x.append(value)
        #x.append((key, value))
    return x

if __name__=="__main__":
    
    # Example string
    example_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

    # Open input data
    with open('data/rosalind_dna.txt') as data:
        dna = data.read().strip()

    # Save output wanted, i.e. only numbers and map to string
    vals = map(str, counting_nucleotides(dna))

    # Output and save solution
    with open('output/001_DNA.txt', 'w') as output_data:
        output_data.write(' '.join(vals))
