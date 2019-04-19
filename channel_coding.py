# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:39:30 2019

@author: USER
"""
import wave
import matplotlib.pyplot as plt
from random import *

def import_sound(filename):
    with wave.open(filename, mode='rb') as sound:
        print(sound.getparams())
        sample_list = []
        for i in range(sound.getnframes()):
            sample_list.append(sound.readframes(1))
        return sample_list
    
def from_bytes_list_to_int_list(bytes_list):
    integer_list = []
    for bytes_value in bytes_list:
        integer_value = int.from_bytes(bytes_value, 'big')
        integer_list.append(integer_value)
    return integer_list

def from_int_list_to_binaries(integer_list):
    binary_list = []
    for v in integer_list:
        res = ''
        reste = v % 2
        res += str(reste)
        v = int((v - reste) / 2)
        while(v!=0):
            reste = v % 2
            res += str(reste)
            v = int((v - reste) / 2)
        while(len(res) != 8):#because log2(256) = 8
            res += '0'
        binary_list.append(res[::-1])
    return binary_list

def hamming_7_4_coder(binaries):
    coding_table = {
        "0000": "0000000", "0001": "0001011", "0010": "0010111", "0011": "0011100",
        "0100": "0100110", "0101": "0101101", "0110": "0110001", "0111": "0111010",
        "1000": "1000101", "1001": "1001110", "1010": "1010010", "1011": "1011001",
        "1100": "1100011", "1101": "1101000", "1110": "1110100", "1111": "1111111"
    }
    res1 = coding_table[binaries[0:4]]
    res2 = coding_table[binaries[4:8]]
    return res1+res2

def code_signal(sound_binary_list):
    sound_coded_list = []
    for e in sound_binary_list:
        sound_coded_list.append(hamming_7_4_coder(e))
    return sound_coded_list

def corrupt_signal(binary_list):
    i = 0
    for bits in binary_list:
        copy = ''
        for bit in bits:
            if(random() <= 0.01):
                if(bit == '0'):
                    copy += '1'
                else:
                    copy += '0'
            else:
                copy += bit
        binary_list[i] = copy
        i += 1
    return binary_list

def from_binaries_to_int_list(binaries):
    integer_list = []
    for e in binaries:
        num = ''
        b = False
        for i in e:
            if( i == '1'):
                b = True
            if(b):
                num += i
        if(not b):
            num = 0
        dec_value = 0
        base = 1
        temp = int(num)
        while(temp):
            last_digit = temp % 10
            temp = int(temp/10)
            dec_value += last_digit * base
            base *= 2
        integer_list.append(dec_value)
    return integer_list

def from_int_list_to_bytes_list(integer_list):
    bytes_list = []
    for integer in integer_list:
        byte = bytes([integer])
        bytes_list.append(byte)

    return bytes_list

def export_sound(filename, sample_list):
    with wave.open(filename, mode='wb') as sound:
        sound.setnchannels(1)
        sound.setsampwidth(1)
        sound.setframerate(11025)

        for sample in sample_list:
            sound.writeframes(sample)
            
def recover_corrupted_symbol(symbol):
    coding_table = {
        "0000": "0000000", "0001": "0001011", "0010": "0010111", "0011": "0011100",
        "0100": "0100110", "0101": "0101101", "0110": "0110001", "0111": "0111010",
        "1000": "1000101", "1001": "1001110", "1010": "1010010", "1011": "1011001",
        "1100": "1100011", "1101": "1101000", "1110": "1110100", "1111": "1111111"
    }
    if(symbol == coding_table[symbol[0:4]]):#no errors
        return symbol
    else:#error
        counter = 0
        index = []
        i = 0
        for e in symbol[4:7]:
            if(e != coding_table[symbol[0:4]][4:7][i]):
                counter += 1
                index.append(i)
            i += 1
        if(counter > 1):
            strCopy = ''
            if(index == [0,2]):
                for e in range(len(symbol)):
                    if(e == 0):
                        strCopy += str((int(symbol[e]) + 1) % 2)
                    else:
                        strCopy += symbol[e]
                return strCopy
            elif(index == [0,1]):
                for e in range(len(symbol)):
                    if(e == 1):
                        strCopy += str((int(symbol[e]) + 1) % 2)
                    else:
                        strCopy += symbol[e]
                return strCopy
            elif(index == [0,1,2]):
                for e in range(len(symbol)):
                    if(e == 2):
                        strCopy += str((int(symbol[e]) + 1) % 2)
                    else:
                        strCopy += symbol[e]
                return strCopy
            elif(index == [1,2]):
                for e in range(len(symbol)):
                    if(e == 3):
                        strCopy += str((int(symbol[e]) + 1) % 2)
                    else:
                        strCopy += symbol[e]
                return strCopy
        else:
            return coding_table[symbol[0:4]]
        
def recover_corrupted_signal(corrupt_coded_list):
    recovered_coded_list = []
    for v in corrupt_coded_list:
        s = recover_corrupted_symbol(v[0:7])
        s += recover_corrupted_symbol(v[7:14])
        recovered_coded_list.append(s)
    return recovered_coded_list
        
        
    
    
    