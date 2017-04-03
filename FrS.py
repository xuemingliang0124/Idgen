# coding=utf-8
import os
import random
import sqlite3 as sql
class IDGen:
    def __init__(self):
        self.addr=os.getcwd()
        os.system(self.addr+'\\sqlite_pre.py')
        self.state={}
        self.city={}
        self.county={}
        self.con=sql.connect(self.addr+'\\city')
        self.cur=self.con.cursor()
        self.data=self.cur.execute('select sta,sta_val from state')
        for i in self.data:
            self.state.update({i[0]:i[1]})
        self.data=self.cur.execute('select city,city_val from city')
        for i in self.data:
            self.city.update({i[0]:i[1]})
        self.data=self.cur.execute('select county,cou_val from county')
        for i in self.data:
            self.county.update({i[0]:i[1]})
        self.cur.close()
        self.con.close()
    def SetNum(self,x,y,z):        
        self.con=sql.connect(self.addr+'\\city')
        self.cur=self.con.cursor()
        self.data1=self.cur.execute('SELECT STA_VAL FROM STATES WHERE STA=?','北京市')
        self.data2=self.cur.execute('SELECT CITY_VAL FROM CITYS WHERE CITY=?',y)
        self.data3=self.data+self.cur.execute('SELECT COU_VAL FROM COUNTYS WHERE COUNTY=?',z)
        data1=data1+data2+data3
        self.cur.close()
        self.con.close()
        return data1

    def GetNumList(self,menu):
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

        count = 0 #计算校验码
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
