# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:28:31 2019

@author: USER
"""
from source_coding import *

lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
numbers = list('0123456789')
additional_characters = list('.,;:\'?!-=/& ')

def import_text(file):
    with open('text.csv','r') as csvFile:
        char = list()
        for line in csvFile:
            for symbol in line:
                char.append(symbol.lower())
        return char
    
text = import_text('text.csv')
pDistrib = marginal_pDistrib(text)
huffman_code = binary_huffman_code(pDistrib)

encoded_text = encode_text(text)

print('2.   marginal probability distribution : ', pDistrib, '\n')
print('3.   Coding table : ', huffman_code, '\n')
print('4.   Coded text : ', encoded_text)
print('     Length of th coded text :', len(encoded_text), '\n')
print('5.   Expected average length :', expected_average_length(pDistrib))
print('     Empirical average length :', len(encoded_text) / len(text), '\n')
