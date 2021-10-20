import sys
from sys import argv
from struct import *

input_file='Teste16mb.txt'
file = open(input_file,'rb')                 
data = file.read(1024*1024)                      

# Building and initializing the dictionary.
dictionary_size = 256                   
dictionary = {str(i): i for i in range(dictionary_size)}    
string = ""             # String is null.
compressed_data = []    # variable to store the compressed data.

# iterating through the input symbols.
# LZW Compression algorithm
while data:
    for symbol in data:                     
        string_plus_symbol = string + str(symbol) # get input symbol.
        if string_plus_symbol in dictionary: 
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if(len(dictionary) <= 65535):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = str(symbol)
    data = file.read(1024*1024)

if string in dictionary:
    compressed_data.append(dictionary[string])

# storing the compressed string into a file (byte-wise).
out = input_file.split(".")[0]
output_file = open(out + ".lzw", "wb")
print(out)
for data in compressed_data:
    output_file.write(pack('>H',int(data)))
    
output_file.close()
file.close()


import sys
from sys import argv
import struct
from struct import *

file = open('Teste16mb.lzw', "rb")
compressed_data = []
next_code = 256
decompressed_data = ""
string = ""

# Reading the compressed file.
while True:
    rec = file.read(2)
    if len(rec) != 2:
        break
    (data, ) = unpack('>H', rec)
    compressed_data.append(data)

# Building and initializing the dictionary.
dictionary_size = 256
dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

# iterating through the codes.
# LZW Decompression algorithm
for code in compressed_data:
    if not (code in dictionary):
        dictionary[code] = string + (string[0])
    decompressed_data += dictionary[code]
    if not(len(string) == 0):
        dictionary[next_code] = string + (dictionary[code][0])
        next_code += 1
    string = dictionary[code]

# storing the decompressed string into a file.
out = input_file.split(".")[0]
output_file = open(out + "_decoded.txt", "w")
for data in decompressed_data:
    output_file.write(data)
    
output_file.close()
file.close()


# In[ ]:




