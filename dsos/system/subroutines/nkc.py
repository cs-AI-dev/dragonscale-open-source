def runSubroutine(raw):
  cipherBase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "\'", "\"", ",", "<", ".", ">", "/", "?", "`", "~"]

  newCipher = []
  for chara in list(raw):
    if not chara in newCipher:
      newCipher.append(chara)

  for chara in cipherBase:
    if not chara in newCipher:
      newCipher.append(chara)
    
  step1 = ""
  for chara in list(raw):
    for x in range(len(cipherBase)):
      if chara == cipherBase[x]:
        step1 = step1 + newCipher[x]
              
  step2 = ""
  for x in range(len(list(step1))):
    if x < 3:
      step2 = step2 + list(step1)[x]
    elif x % 2 == 0:
      step2 = step2 + list(step1)[x - 3]
    else:
      step2 = step2 + list(step1)[x]

  encrypted = ""
  for x in list(step2):
    encrypted = encrypted + format(
      (int(str(ord(x)), 16) ^ int(len(raw))) * int(hex(len(raw)), 16), "x"
    )

  return encrypted

def check(nkcPass, inputData):
  return nkc(inputData) == nkcPass
