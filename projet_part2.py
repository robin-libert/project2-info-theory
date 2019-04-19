# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:37:13 2019

@author: USER
"""

from channel_coding import *
from math import *

    
sound = import_sound('sound.wav')
sound_int_list = from_bytes_list_to_int_list(sound)

#plt.figure(figsize=(100,10))
plt.plot(sound_int_list)
plt.savefig('sound.png', dpi=300)
plt.show()

print('8.   Sound signal plotted')
print('     Sound signal : ', sound_int_list[0:7], '...')
print('     Number of sample : ', len(sound_int_list), '\n')


sound_binary_list = from_int_list_to_binaries(sound_int_list)
sound_coded_list = code_signal(sound_binary_list)

corrupt_coded_list = corrupt_signal(sound_coded_list)
corrupt_sound_binary_list = []

for e in corrupt_coded_list:
    copy = e[0:4] + e[7:11]
    corrupt_sound_binary_list.append(copy)

corrupt_sound_int_list = from_binaries_to_int_list(corrupt_sound_binary_list)
corrupt_sound_binary_list = from_int_list_to_bytes_list(corrupt_sound_int_list)
export_sound('corrupt_sound.wav', corrupt_sound_binary_list)

#plt.figure(figsize=(100,10))
plt.plot(corrupt_sound_int_list)
plt.savefig('corrupted_sound.png', dpi=300)
plt.show()

recovered_coded_list = recover_corrupted_signal(corrupt_coded_list)
recovered_sound_list = []
for e in recovered_coded_list:
    copy = e[0:4] + e[7:11]
    recovered_sound_list.append(copy)
    
recovered_sound_int_list = from_binaries_to_int_list(recovered_sound_list)
recovered_sound_binary_list = from_int_list_to_bytes_list(recovered_sound_int_list)
export_sound('recovered_sound.wav', recovered_sound_binary_list)

#plt.figure(figsize=(100,10))
plt.plot(recovered_sound_int_list)
plt.savefig('recovered_sound.png', dpi=300)
plt.show()