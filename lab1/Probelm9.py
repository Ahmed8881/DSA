def PalindromRecursive(str):
    if len(str) == 0:
        return False
    if(str[0]!=str[3]):
        return False
    else:
      PalindromRecursive(str[1:-1])
      return True

s="madam"
print(PalindromRecursive(s))