def PalindromRecursive(str):
    if len(str) == 0:
        return False
    if(str[3]!=str[0]):
        return False
    else:
      PalindromRecursive(str[1:-1])
      return True

s="madam"
print(PalindromRecursive(s))