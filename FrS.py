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
        self.data=self.cur.execute('select sta,sta_val from states')
        for i in self.data:
            self.state.update({i[0]:i[1]})
        self.data=self.cur.execute('select city,city_val from citys')
        for i in self.data:
            self.city.update({i[0]:i[1]})
        self.data=self.cur.execute('select county,cou_val from countys')
        for i in self.data:
            self.county.update({i[0]:i[1]})
        self.cur.close()
        self.con.close()

    def GetNumList(self,menu):
        if menu=='state':   
            self.conn=sql.connect(self.addr+'\\city')
            self.cur=self.conn.cursor()
            self.state=self.cur.execute('SELECT STA FROM STATES')
            return self.state
        if menu=='city':
            return self.city
        if menu=='county':
            return self.county

    def SetNum(self,x,y,z):        
        self.data1=self.state.get(x)
        self.data2=self.city.get(y)
        self.data3=self.county.get(z)
        self.data_sum=self.data1+self.data2+self.data3

    def SetBirth(self,year,month,day):
        if month<'10':
            month='0'+month
        if day<'10':
            day='0'+day
        self.birth=year+month+day
    def SetSex(self,sex):
        self.sex=sex
        if self.sex=='男':
            self.sex=random.randrange(1,9,2)
        elif self.sex=='女':
            self.sex=random.randrange(0,9,2)

    def GetID(self):
        id1=self.data_sum+self.birth+str(random.randint(10,99))+str(self.sex)

        count = 0 #计算校验码
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
        checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
        for i in range(0,len(id1)):
            count = count +int(id1[i])*weight[i]
        id1 = id1 + checkcode[str(count%11)] #算出校验码
        return id1
    
