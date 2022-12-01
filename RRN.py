import re

loc = input(r'example : (C:\Users\20220872\Downloads\num.txt)')
f = open(loc, 'r', encoding='UTF-8')
RRN = f.readlines() 

for i in range(len(RRN)):
    regexSub = re.compile(r'\d{6}$')
    str = regexSub.sub('******', RRN[i])
    print(str.strip('\n'))
