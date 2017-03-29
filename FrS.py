# coding=utf-8
import os
import random
class IDGen:
    def GetNum(self,x,y,z):
        city={}
        state={}
        county={}
        file=open('e:\\city2.txt')
        a=file.read()
        src1=a.split('\n')
        for line in src1:
            if line[:1]!=' ' :
                state[line[11:]]=line[0:2]
            if line[2:3]!=' ' and line[7:8]!=' ':
                city[line[17:]]=line[4:6]
            if line[8:9]!=' ' :
                county[line[15:]]=line[8:10]
        return state.get(x)+city.get(y)+county.get(z)
    def GetID(self,x,y,z,birthday,sex):
        if sex=='男':
            sex=random.randrange(1,9,2)
        elif sex=='女':
            sex=random.randrange(0,9,2)
        else:
            sex=input('input error,please input again:')
        id1=str()
        id1=self.GetNum(x,y,z)+birthday+str(random.randint(10,99))+str(sex)
        
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
        checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
        for i in range(0,len(id1)):
            count = count +int(id1[i])*weight[i]
        id1 = id1 + checkcode[str(count%11)] #算出校验码
        return id1
    def PersonID(self):
        x=input('please input state:')
        y=input('please input city:')
        z=input('please input county:')
        birthday=input('please input birthday:')
        sex=input('please input sex:')
        ID=self.GetID(x,y,z,birthday,sex)
        return ID
