import sys
from sys import argv
import struct
from struct import *
import helper


def encoder(file):
  print('.', end='', flush=True)
  openedFile = open(file,'rb')                 
  data = openedFile.read()                      
  k=16
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

def run(file):
  bEncoding, gbDone, bFile  = helper.formatColors('enc', file)
  print(f'LZW {bEncoding} for file {bFile} has started ', end='', flush=True)
  encoder(file)
  print(f'{gbDone}')

if __name__ == '__main__':
    run('ArnaldoPina.txt')
