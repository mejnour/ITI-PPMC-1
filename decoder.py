import sys
from sys import argv
import struct
from struct import *

def decoder(file):
  openedFile = open(file, "rb")
  compressed_data = []
  next_code = 256
  decompressed_data = ""
  string = ""

  while True:
      rec = openedFile.read(2)
      if len(rec) != 2:
          break
      (data, ) = unpack('>H', rec)
      compressed_data.append(data)

  dictionary_size = 256
  dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

  for code in compressed_data:
      if not (code in dictionary):
          dictionary[code] = string + (string[0])
      decompressed_data += dictionary[code]
      if not(len(string) == 0):
          dictionary[next_code] = string + (dictionary[code][0])
          next_code += 1
      string = dictionary[code]

  out = file.split(".")[0]
  output_file = open(out + "_decoded.txt", "w")
  for data in decompressed_data:
      output_file.write(data)
      
  output_file.close()
  openedFile.close()

def run(file):
  decoder(file)

if __name__ == '__main__':
    run('ArnaldoPina.lzw')
