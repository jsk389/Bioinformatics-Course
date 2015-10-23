#!/usr/bin/env python3
"""
Problem Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
"""

import hashlib
import numpy as np

def NaiveSearch(string, pattern):
    """
    Naive search for substring in string

    Return the positions where the given pattern is found in the text
    """

    n = len(string)
    m = len(pattern)

    positions = []
    for i in range(n-m+1):
        if pattern == string[i:i+m]:
            positions.append(str(i+1))

    return positions

def RabinKarp(string, pattern):
    """
    Rabin-Karp algorithm
    """
    # Ensure in byte format for hashing
    string = string.encode('utf-8')
    pattern = pattern.encode('utf-8')

    n = len(string)
    m = len(pattern)

    # Hash pattern and first string segment equal to length of pattern
    hpattern = hashlib.sha256(pattern).hexdigest()
    hs = hashlib.sha256(string[:m]).hexdigest()

    # Set up empty list to hold positions
    positions = []

    # Iterate over input string
    for i in range(n-m+1):
        if hs == hpattern:
             if string[i:i+m] == pattern:
                positions.append(str(i+1))
        if i < n-m:
            hs = hashlib.sha256(string[i+1:i+1+m]).hexdigest()
    return positions

def RabinKarpSet(string, patterns, m):
    """
    Rabin-Karp algorithm extended to multiple patterns of fixed length m

    string - byte containing input string
    patterns - dictionary containing patterns of length m

    example usage:
    text = 'GATATATGCATATACTTGCAT'.encode('utf-8')
    patterns = {'1': 'ATAT'.encode('utf-8'), '2': 'GCAT'.encode('utf-8')} 

    m = 4
    positions3 = RabinKarpSet(text, patterns, m)
    print("Positions where pattern is found for Rabin-KarpSet "+" ".join(positions3))

    """

    # TO DO! Add positions to dictionary so that can differentiate
    # between the multiple patterns given

    n = len(string)

    # Create dictionary to put hashed patterns into
    hsubs = {}
    for index, value in patterns.items():
        hsubs[index] = hashlib.sha256(value).hexdigest()

    # Hash first segment of input string
    hs = hashlib.sha256(string[:m]).hexdigest()

    positions = []
    # Iterate over input string segments
    for i in range(n-m+1):
        if (hs in hsubs.values()) and (string[i:i+m] in patterns.values()):          
            positions.append(str(i+1))
        if i < n-m:
            hs = hashlib.sha256(string[i+1:i+1+m]).hexdigest()

    return positions 

if __name__=="__main__":

    # Example text
    #text = 'GATATATGCATATACTT'
    #pattern = 'ATAT'

    # Load in input
    with open('data/rosalind_subs.txt') as input_data:
        text, pattern = input_data.readlines()
        text = text.rstrip()
        pattern = pattern.rstrip()

    positions = NaiveSearch(text, pattern)
    print("Positions where pattern is found for NaiveSearch "+" ".join(positions))

    positions2 = RabinKarp(text, pattern)
    print("Positions where pattern is found for Rabin-Karp "+" ".join(positions2))

    # Save solution
    with open('output/009_SUBS.txt', 'w') as output_data:
        output_data.write(' '.join(positions2))

    




