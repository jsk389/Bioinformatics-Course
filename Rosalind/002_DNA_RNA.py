# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:33:25 2015

@author: James
"""

def simple_DNA_to_RNA(string):
    return string.replace('T', 'U')    
    
def better_DNA_to_RNA(string, dic):
    for i, j in dic.iteritems():
        string = string.replace(i,j)
    return string
 
# Sample string   
#string = 'GATGGAACTTGACTACGTAAATT'
# Import file
f = open('rosalind_rna.txt', 'r')
string = f.read()
# Create dictionary containing letters to replace and be
# be replaced
dic = {'T': 'U'}
string = better_DNA_to_RNA(string, dic)
print(string)
