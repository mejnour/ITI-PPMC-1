import sys
from sys import argv
import struct
from struct import *
import helper

def decoder(file):
  print('.', end='', flush=True)    

  openedFile = open(file, "rb")
  lzwCompressed = []
  next_code = 256
  lzwDecompressed = ""
  currentStr = ""

  while True:
      twoBitStepper = openedFile.read(2)
      if len(twoBitStepper) != 2:
          break
      (data, ) = unpack('<H', twoBitStepper)
      lzwCompressed.append(data)

  dictionarySize = 256
  dictionary = dict([(x, chr(x)) for x in range(dictionarySize)])

  print('.', end='', flush=True)

  for code in lzwCompressed:
      if not (code in dictionary):
          dictionary[code] = currentStr + (currentStr[0])
      lzwDecompressed += dictionary[code]
      if not(len(currentStr) == 0):
          dictionary[next_code] = currentStr + (dictionary[code][0])
          next_code += 1
      currentStr = dictionary[code]

  out = file.split(".")[0]
  output_file = open(out + "Extract.txt", "w")
  for data in lzwDecompressed:
      output_file.write(data)
      
  output_file.close()
  openedFile.close()

  print('.', end=' ', flush=True)

def run(file):
  bDecoding, gbDone, bFile = helper.formatColors('dec', file)
  print(f'LZW {bDecoding} for file {bFile} has started ', end='', flush=True)
  decoder(file)
  print(f'{gbDone}')


if __name__ == '__main__':
    run('ArnaldoPina.lzw')
