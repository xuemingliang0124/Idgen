# coding=utf-8
import os
import sqlite3

addr=os.getcwd()
con=sqlite3.connect(addr+'\\city')  #连接数数据库，不存在就创建
cur=con.cursor() #创建游标
cur.execute('drop table if exists state;')
cur.execute('drop table if exists city;')
cur.execute('drop table if exists county;') #清理旧库
cur.execute('create table if not exists state(\
id int primary key not null,\
STA TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS CITY(\
ID INT PRIMARY KEY NOT NULL,\
CITY TEXT NOT NULL,\
CITY_VAL TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS COUNTY(\
ID INT PRIMARY KEY NOT NULL,\
COUNTY TEXT NOT NULL,\
COU_VAL TEXT NOT NULL,\
CITY_VAL TEXT NOT NULL,\
STA_VAL TEXT NOT NULL);')     #创建表

'''========================================='''#读取文档保存到库
sta_ins='INSERT INTO STATE (ID,STA,STA_VAL) VALUES (?,?,?)'
city_ins='INSERT INTO CITY (ID,CITY,CITY_VAL,STA_VAL) VALUES (?,?,?,?)'
coun_ins='INSERT INTO COUNTY (ID,COUNTY,COU_VAL,CITY_VAL,STA_VAL) VALUES (?,?,?,?,?)'

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

