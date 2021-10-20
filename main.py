import sys
import decoder
import encoder

def run():
  try:
    encodeOrDecode = sys.argv[1]

    if (encodeOrDecode == 'encode'):
      encoder.run(sys.argv[2])
    elif (encodeOrDecode == 'decode'):
      decoder.run(sys.argv[2])

  except:
    print('Review code parameters.')
    raise

if __name__ == '__main__':
  run()