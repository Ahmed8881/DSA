def PalindromRecursive(str):
    Start=0
    if len(str)==0:
        return False
    elif(str[Start]!=str[-1]):
        return False
    else:
         Start+=1
         PalindromRecursive(str[Start:-1])
         return True

s="radar"
print(PalindromRecursive(s))

    