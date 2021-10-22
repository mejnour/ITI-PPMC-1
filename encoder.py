import sys
from sys import argv
import struct
from struct import *
import helper


def encoder(file):
  print('.', end='', flush=True)
  openedFile = open(file,'rb')                 
  data = openedFile.read(1024*1024)                      

  dictionary_size = 256                   
  dictionary = {str(i): i for i in range(dictionary_size)}    
  string = ""
  compressed_data = []

  while data:
    for symbol in data:
      string_plus_symbol = string + str(symbol)

      if string_plus_symbol in dictionary: 
        string = string_plus_symbol

      else:
        compressed_data.append(dictionary[string])
        if(len(dictionary) <= 65535):
          dictionary[string_plus_symbol] = dictionary_size
          dictionary_size += 1
          string = str(symbol)
    data = openedFile.read(1024*1024)

  print('.', end='', flush=True)

  if string in dictionary:
      compressed_data.append(dictionary[string])

  out = file.split(".")[0]
  output_file = open(out + ".lzw", "wb")
  for data in compressed_data:
      output_file.write(pack('>H',int(data)))
        
  output_file.close()
  openedFile.close()

  print('.', end=' ', flush=True)

def run(file):
  bEncoding, gbDone, bFile  = helper.formatColors('enc', file)
  print(f'LZW {bEncoding} for file {bFile} has started ', end='', flush=True)
  encoder(file)
  print(f'{gbDone}')

if __name__ == '__main__':
    run('ArnaldoPina.txt')
