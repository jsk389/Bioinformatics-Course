# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:33:25 2015

@author: James
"""

def DNA_to_RNA(string):
    """
    Translation of DNA to RNA
    """
    return string.replace('T', 'U')    
    
def better_DNA_to_RNA(string, dic):
    """
    This method of translation is good if multiple
    replacements are needed (contained in dic)
    """
    for i, j in dic.iteritems():
        string = string.replace(i,j)
    return string
 
if __name__=="__main__": 

    # Sample string   
    sample_string = 'GATGGAACTTGACTACGTAAATT'
    # Import file
    with open('data/rosalind_rna.txt') as input_data:
        dna = input_data.read().strip()

    # Translate given DNA sequence to RNA sequence
    rna = DNA_to_RNA(dna)

    print(rna)

    # Save output to file
    with open('output/002_DNA_RNA.txt', 'w') as output_data:
        output_data.write(rna)

    # Create dictionary containing letters to replace and be
    # be replaced
    #dic = {'T': 'U'}
    #string = better_DNA_to_RNA(string, dic)
    #print(string)
