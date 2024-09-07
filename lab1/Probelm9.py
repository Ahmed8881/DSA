def PalindromRecursive(str):
    if len(str)==0:
        return False
    else:
         PalindromRecursive(str[1:-1])
         return True

s="rammar"
print(PalindromRecursive(s))

    