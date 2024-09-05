def StringReverse(str,starting,ending):
    return str[starting:ending:-1]
    

s = "University of Engineering and Technology Lahore"
a=StringReverse(s,25,9)
print(a)