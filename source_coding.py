# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:43:20 2019

@author: USER
"""

def marginal_pDistrib(text):
    text_length = len(text)
    dictionary = dict()
    for s in text:
        if s not in dictionary:
            dictionary[s] = 1
        else:
            dictionary[s] += 1
    for s in dictionary:
        dictionary[s] = dictionary[s] / text_length
    return dictionary

def binary_huffman_code(pDistrib):
    copy = pDistrib.copy()
    coded = dict()
    #create new dictionary with symbols
    for v in copy:
        coded[v] = ""
    summ = 0
    while(summ != 1):
        #find the 2 lowest valued symbols
        minKeys = []
        minValues = []
        for n in range(2):
            minKeys.append(min(copy, key = copy.get))
            minValues.append(min(copy.values()))
            copy.pop(minKeys[n])
        #summ is sused to stop the while loop
        summ = minValues[0] + minValues[1]
        #create the values of the coded dictionary
        copy[minKeys[0] + minKeys[1]] = summ
        if(minKeys[0][0] <= minKeys[1][0]):
            for e in minKeys[0]:
                coded[e] += '0'
            for e in minKeys[1]:
                coded[e] += '1'
        else:
            for e in minKeys[1]:
                coded[e] += '0'
            for e in minKeys[0]:
                coded[e] += '1'
    for e in coded:
        #reverse a string
        coded[e] = coded[e][::-1]
    return coded

def encode_text(text):
    distrib = marginal_pDistrib(text)
    huffman_code = binary_huffman_code(distrib)
    encoded_text = ""
    for s in text:
        encoded_text += huffman_code[s]
    return encoded_text

def expected_average_length(pDistrib):
    huffman_code = binary_huffman_code(pDistrib)
    n = 0
    for s in huffman_code:
        n += len(huffman_code[s]) * pDistrib[s]
    return n

def compression_rate(text, encoded_text):
    return (8*len(text))/len(encoded_text)