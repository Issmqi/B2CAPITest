# s1=['a','b','c','d','e']
# s2=['a','c','d']
s1='abcde'
s2='acd'
re=''
# re=[]
for i in s1:
    if i not in s2:
        re=re+i
        # re.append(i)


print(re)