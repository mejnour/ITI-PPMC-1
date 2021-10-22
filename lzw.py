import sys
import decoder
import encoder
import time
import re


def elapsedTime(initialTime, finalTime):
  return finalTime - initialTime

def run():
  
  try:
    start = time.time()
    # sys.exit()
    if (sys.argv[1] == 'encode'):
      encoder.run(sys.argv[2])
    elif (sys.argv[1] == 'decode'):
      decoder.run(sys.argv[2])
    elif (sys.argv[1] == 'bothways'):
      encoder.run(sys.argv[2])
      decoder.run(
        '{}.lzw'.format(re.search(
          r'^(.+?)[^\.]+', 
          sys.argv[2]).group()))
    else:
      print('Did you mean \'encode\', \'decode\' or maybe \'bothways\'?')
      
    finish = time.time()
    print('Elapsed time: {:.5f}'.format(elapsedTime(start, finish)))

  except:
    print('I didnt like It. Get your stuff together! Error:')
    raise

if __name__ == '__main__':
  run()