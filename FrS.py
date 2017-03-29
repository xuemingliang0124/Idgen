# coding=utf-8
import os
import random
class IDGen:
    def __init__(self):
        self.city={}
        self.state={}
        self.county={}
        file=open('e:\\city2.txt')
        a=file.read()
        src1=a.split('\n')
        for line in src1:
                if line[:1]!=' ' :
                        self.state[line[11:]]=line[0:2]
                if line[2:3]!=' ' and line[7:8]!=' ':
                        self.city[line[17:]]=line[4:6]
                if line[8:9]!=' ' :
                        self.county[line[15:]]=line[8:10]
    def SetNum(self):        
        x=input('please input state:')
        y=input('please input city:')
        z=input('please input county:')
        return self.state.get(x)+self.city.get(y)+self.county.get(z)
    def GetNumDict(self,menu):
        IDGen.SetNum
        
        if menu=='state':
            
            return self.state
        if menu=='city':
            return self.city
        if menu=='county':
            return self.county
    def GetID(self):
        a=self.SetNum()
        birth=input('please input birthday:')
        id1=str()
        id1=a+birth+str(random.randint(10,99))+str(self.SetSex())

        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
        checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
        for i in range(0,len(id1)):
            count = count +int(id1[i])*weight[i]
        id1 = id1 + checkcode[str(count%11)] #算出校验码
        return id1
    def SetSex(self):
        sex=input('please input sex:')
        while True :
            if sex=='男':
                sex=random.randrange(1,9,2)
                return sex
            elif sex=='女':
                sex=random.randrange(0,9,2)
                return sex
            else:
                sex=input('input error,please input again:')
    def PersonID(self):
        ID=self.GetID()
        return ID
