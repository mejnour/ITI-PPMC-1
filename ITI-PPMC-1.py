#!/usr/bin/env python
# coding: utf-8

# # Encoder LZW

# In[93]:


import struct
import time
entrada='Teste.txt'
file = open(entrada,"rb")
ofile = open('saida_'+entrada+'.lzw', 'wb')
data = file.read(1024*1024)
dictionary_size = 256                   
dictionary = {str(i):i for i in range(dictionary_size)}
#print(dictionary)
nss='' #Next.Symbol.Sequence
kss='' #Known.Symbol.Sequence
while data:
    for symbol in data:
        #print(symbol)
        nss=kss+str(dictionary[str(symbol)])
        #print(symbol,nss,kss,sep='|')
        if nss in dictionary:
            kss=nss
        else:
            #ofile.write(bytearray(bin(dictionary[kss]),'utf-8'))
            ofile.write(struct.pack('i', dictionary[kss]))
            dictionary[nss] = dictionary_size
            dictionary_size += 1
            kss = str(symbol)
    data = file.read(1024*1024)
ofile.close()
file.close()


# # Decoder

# In[ ]:


input_file, n = argv[1:]            
maximum_table_size = pow(2,int(n))
file = open(input_file, "rb")
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

