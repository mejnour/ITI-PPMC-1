import sys

def encoder(file):
  print('encoder' + file)

def decoder(file):
  print('decoder' + file)

def run():
  try:
    encodeOrDecode = sys.argv[1]

    if (encodeOrDecode == 'encode'):
      encoder(sys.argv[2])
    elif (encodeOrDecode == 'decode'):
      decoder(sys.argv[2])

  except:
    print('Review code parameters.')
    raise

if __name__ == '__main__':
  run()