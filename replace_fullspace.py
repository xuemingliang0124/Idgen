import os
state={}
city={}
county={}
file1=open('e:\\city.txt')
file2=open('e:\\city2.txt','w')
a=file1.readlines()
for each in a:
    if each=='\n':
        continue
    if each[11:12]!=' ':
        newstr=each.replace('\u3000','')
        file2.write(newstr)
    elif each[7:8]==' ' and each[:1]!=' ':
        newstr=each.replace('\u3000','')
        newstr='  '+newstr
        file2.write(newstr)
    elif each[7:8]!='  ' :
        newstr=each.replace('\u3000','')
        newstr='    '+newstr
        file2.write(newstr)
file1.close()
file2.close()
        
