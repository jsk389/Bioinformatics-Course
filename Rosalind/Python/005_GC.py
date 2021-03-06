#!/usr/bin/env python3
"""
Problem Title: Computing GC content
Rosalind ID: GC
Rosalind #: 005
"""

import numpy as np

if __name__=="__main__":

    fname = '005_sampledata.txt'
    # Open file and remove '\n' from each element
    with open(fname) as f:
        sample_data = [line.rstrip('\n') for line in f]

    # Store name of sequence
    sequence = sample_data[::2]
    # Store content of sequence
    content = sample_data[1::2]
    
    GC_content = []
    for i in range(len(sequence)):
        amount = 0
        for base in content[i]:
            if base in ('G', 'C'):
                amount += 1
        GC_content.append(float(amount) / float(len(content[i])) * 100.0)

    m = GC_content.index(max(GC_content))
    print(sequence[m])
    print(content[m])
    

    # FAR TOO ROUGH AT THE MOMENT!!
