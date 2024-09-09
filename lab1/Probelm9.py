def PalindromRecursive(str):
    Start=0
    End=-1
    if len(str)==0 or len(str)==1:
        return True
    elif(str[Start]!=str[End]):
        return False
    else:
         Start+=1
         End=-Start+1
         return PalindromRecursive(str[Start:-1])
         

s="radar"
print(PalindromRecursive(s))

    