#!/usr/bin/env python3
"""
Problem Title: Computing GC content
Rosalind ID: GC
Rosalind #: 005
"""

import numpy as np
import 009_SUBS# import RabinKarpSet

if __name__=="__main__":

    fname = '005_sampledata.txt'
    # Open file and remove '\n' from each element
    with open(fname) as f:
        sample_data = [line.rstrip('\n') for line in f]

    # Store name of sequence
    sequence = sample_data[::2]
    # Store content of sequence
    content = sample_data[1::2]

    patterns = {'1': 'C', '2': 'G'}
    positions = RabinKarpSet(content[0], patterns, 1)
    print(positions)
