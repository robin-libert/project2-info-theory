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
        min1Key = min(copy, key = copy.get)
        min1V = min(copy.values())
        copy.pop(min1Key)
        min2Key = min(copy, key = copy.get)
        min2V = min(copy.values())
        copy.pop(min2Key)
        summ = min1V + min2V
        copy[min1Key+min2Key] = summ
        if(min1Key[0] <= min2Key[0]):
            for e in min1Key:
                coded[e] += '0'
            for e in min2Key:
                coded[e] += '1'
        else:
            for e in min2Key:
                coded[e] += '0'
            for e in min1Key:
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
    return len(text)/len(encoded_text)