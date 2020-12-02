#ex1
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))

#ex2
import re
def textmatch(text):
    patterns='a.*?b$'
    if re.search(patterns,text):
        return("match found")
    else:
        return("match not found")
print(textmatch("aaaabbbb"))    

#ex3
import re
def textmatch(text):
    patterns='1'
    if re.search(patterns,text):
        return("true")
    else:
        return("false")
print(textmatch("hi12"))

#ex4
import re
results=re.finditer(r"([0-9]{1,3})","1,12 and 345")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

#ex5
import re
def textmatch(text):
    patterns='^[A-Z]'
    if re.search(patterns,text):
        return("match found")
    else:
        return("match not found")
print(textmatch("HI ALL"))    
