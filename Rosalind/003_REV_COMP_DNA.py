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

def create_trans_table(string, complement):
    """
    Creates a translation table to turn DNA sequence into
    it's complement
    """
    return maketrans(string, complement)
    
if __name__=="__main__":
    
    #dna = 'AAAACCCGGT'
    # Load in input
    with open('data/rosalind_revc.txt') as input_data:
        dna = input_data.read().strip()

    trans_table = create_trans_table('ATCG', 'TAGC')

    # Reverse the DNA sequence before transforming
    rev_dna = dna[::-1].translate(trans_table)
    
    print(rev_dna)
    # Save solution
    with open('output/003_REV_COMP_DNA.txt', 'w') as output_data:
        output_data.write(rev_dna)
