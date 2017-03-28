# coding=utf-8
import os
import random
def GetNum(x,y,z):
    city1={}
    state={}
    county={}
    file=open('e:\\city_new.txt')
    a=file.read()
    src1=a.split('\n')
    for line in src1:
        if line[:1]!=' ' :
            state[line[11:]]=line[0:2]
        if line[:2]=='  ' and line[8:9]==' ':
            city1[line[19:]]=line[4:6]
        if line[8:10]!='  ' :
            county[line[19:]]=line[8:10]
    return state[x]+city1[y]+county[z]
def GetID(state,city,county,birthday,sex):
    if sex=='男':
        sex=random.randrange(1,9,2)
    elif sex=='女':
        sex=random.randrange(0,9,2)
    else:
        sex=input('input error,please input again:')
    print(sex)
    id1=str()
    id1=GetNum(state,city,county)+birthday+str(random.randint(10,99))+str(sex)
    
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id1)):
        count = count +int(id1[i])*weight[i]
    id1 = id1 + checkcode[str(count%11)] #算出校验码
    return id1
def PersonID():
    state=input('please input state:')
    city=input('please input city:')
    county=input('please input county:')
    birthday=input('please input birthday:')
    sex=input('please input sex:')
    ID=GetID(state,city,county,birthday,sex)
    return ID
Person=PersonID()
print(Person)
