import sys
from sys import argv
import struct
from struct import *
import helper
import os
import enum


class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

def convert_unit(size_in_bytes, unit):
  """ Convert the size from bytes to other units like KB, MB or GB"""
  if unit == SIZE_UNIT.KB:
      return size_in_bytes/1024
  elif unit == SIZE_UNIT.MB:
      return size_in_bytes/(1024*1024)
  elif unit == SIZE_UNIT.GB:
      return size_in_bytes/(1024*1024*1024)
  else:
      return size_in_bytes

def encoder(file):
  print('.', end='', flush=True)
  openedFile = open(file,'rb')                 
  data = openedFile.read()                      
  k=12
  dictionarySize = 256

  dictionary = {}
  for i in range(dictionarySize):
      dictionary[str(i)] = i

  currentStr = ""
  lzwCompressed = []

  for binCode in data:
    AccumulatedSymbol = currentStr + str(binCode)
  
    if AccumulatedSymbol in dictionary: 
      currentStr = AccumulatedSymbol
  
    else:
      lzwCompressed.append(dictionary[currentStr])
      if(len(dictionary) <= 2**k):
        dictionary[AccumulatedSymbol] = dictionarySize
        dictionarySize += 1
        currentStr = str(binCode)

  print('.', end='', flush=True)

  if currentStr in dictionary:
      lzwCompressed.append(dictionary[currentStr])

  out = file.split(".")[0]
  output_file = open(out + ".lzw", "wb")
  for data in lzwCompressed:
    output_file.write(pack('<H',int(data)))
        
  output_file.close()
  openedFile.close()

  print('.', end=' ', flush=True)

def get_file_size(file_name, size_type = SIZE_UNIT.MB ):
   """ Get file in size in given unit like KB, MB or GB"""
   size = os.path.getsize(file_name)
   return convert_unit(size, size_type)


def run(file):
  bEncoding, gbDone, bFile  = helper.formatColors('enc', file)
  print(f'LZW {bEncoding} for file {bFile} has started ', end='', flush=True)
  encoder(file)
  print(f'{gbDone}')

  print(get_file_size(file))

if __name__ == '__main__':
    run('ArnaldoPina.txt')
