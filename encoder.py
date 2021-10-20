import struct
import sys
import time

def encoder(file):
  openedFile = open(file,"rb")
  decodedFile = open('saida_' + file + '.lzw', 'wb')

  data = openedFile.read(1024*1024)

  dictionary_size = 256                   
  dictionary = {str(i):i for i in range(dictionary_size)}

  #print(dictionary)

  print(data)
#   sys.exit()
  
  nss='' #Next.Symbol.Sequence
  kss='' #Known.Symbol.Sequence
  while data:
      for symbol in data:
          print('symb ', symbol)

          nss=kss+str(dictionary[str(symbol)])
        #   sys.exit()

          nss=kss+str(dictionary[symbol])
          sys.exit()
          
          print('symb ', symbol, 'nss ', nss, 'kss ', kss, sep='|')
          if nss in dictionary:
              kss=nss
          else:
              #ofile.write(bytearray(bin(dictionary[kss]),'utf-8'))
              decodedFile.write(struct.pack('i', dictionary[kss]))
              dictionary[nss] = dictionary_size
              dictionary_size += 1
              kss = str(symbol)
      data = openedFile.read(1024*1024)
  decodedFile.close()
  openedFile.close()

def run(file):
  encoder(file)

if __name__ == '__main__':
    run('teste1.txt')