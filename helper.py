def formatColors(type, file = None):
  boldEncoding = '\033[1m' + 'Encoding' + '\033[0;0m'
  greenBoldDone = '\033[38;5;118m' + '\033[1m' + 'done' + '\033[0;0m'
  
  if type == 'enc':
    boldType = '\033[1m' + 'Encoding' + '\033[0;0m'
  elif type == 'dec':
    boldType = '\033[1m' + 'Decoding' + '\033[0;0m'
  else:
    return None, None, None

  if file:
    boldFile = '\033[1m' + file + '\033[0;0m'
    return boldType, greenBoldDone, boldFile
  else:
    return boldType, greenBoldDone