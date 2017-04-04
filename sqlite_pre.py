# coding=utf-8
import os
import sqlite3

addr=os.getcwd()
con=sqlite3.connect(addr+'\\city')  #连接数据库，不存在就创建
cur=con.cursor() #创建游标
cur.execute('DROP TABLE IF EXISTS STATES;')
cur.execute('DROP TABLE IF EXISTS CITYS;')
cur.execute('DROP TABLE IF EXISTS COUNTYS;') #清理旧库
cur.execute('CREATE TABLE IF NOT EXISTS STATES(\
ID INT PRIMARY KEY NOT NULL,\
STA TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS CITYS(\
ID INT PRIMARY KEY NOT NULL,\
CITY TEXT NOT NULL,\
CITY_VAL TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS COUNTYS(\
ID INT PRIMARY KEY NOT NULL,\
COUNTY TEXT NOT NULL,\
COU_VAL TEXT NOT NULL,\
CITY_VAL TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')     #创建表

'''========================================='''#读取文档保存到库
sta_ins='INSERT INTO STATES (ID,STA,STA_VAL) VALUES (?,?,?)'
city_ins='INSERT INTO CITYS (ID,CITY,CITY_VAL,STA_VAL) VALUES (?,?,?,?)'
coun_ins='INSERT INTO COUNTYS (ID,COUNTY,COU_VAL,CITY_VAL,STA_VAL) VALUES (?,?,?,?,?)'

file=open(addr+'\\city2.txt')
b=file.read()
src1=b.split('\n')
x=0
y=0
z=0
for line in src1:
    if line[:1]!=' ' :
        cur.execute(sta_ins,(x,line[11:],line[:2]))
        x+=1
    if line[2:3]!=' ' and line[7:8]!=' ':
        cur.execute(city_ins,(y,line[17:],line[4:6],line[2:4]))
        y+=1
    if line[8:9]!=' ':
        cur.execute(coun_ins,(z,line[15:],line[8:10],line[6:8],line[4:6]))
        z+=1
'''========================================='''
file.close()
con.commit()#提交修改
cur.close()#关闭游标
con.close()#关闭数据库连接

