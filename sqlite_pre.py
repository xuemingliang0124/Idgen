# coding=utf-8
import os
import sqlite3

a=os.getcwd()
print(a)
con=sqlite3.connect(a+'\\addr')  #连接数数据库，不存在就创建
cur=con.cursor() #创建游标
cur.execute('drop table if exists state;')
cur.execute('drop table if exists city;')
cur.execute('drop table if exists county;') #清理旧库
cur.execute('create table if not exists state(\
id int primary key not null,\
STA TEXT NOT NULL,\
STA_VAL INT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS CITY(\
ID INT PRIMARY KEY NOT NULL,\
CITY TEXT NOT NULL,\
CITY_VAL INT NOT NULL,\
STA_VAL INT NOT NULL);')
cur.execute('CREATE TABLE IF NOT EXISTS COUNTY(\
ID INT PRIMARY KEY NOT NULL,\
COUNTY TEXT NOT NULL,\
COU_VAL INT NOT NULL,\
CITY_VAL INT NOT NULL,\
STA_VAL INT NOT NULL);')     #创建表

'''========================================='''#读取文档保存到库
sta_ins='INSERT INTO STATE (ID,STA,STA_VAL) VALUES (?,?,?)'
city_ins='INSERT INTO CITY (ID,CITY,CITY_VAL,STA_VAL) VALUES (?,?,?,?)'
coun_ins='INSERT INTO COUNTY (ID,COUNTY,COU_VAL,CITY_VAL,STA_VAL) VALUES (?,?,?,?,?)'

file=open('e:\\city2.txt')
b=file.read()
src1=b.split('\n')
x=0
y=0
z=0
for line in src1:
    if line[:1]!=' ' :
        cur.execute(sta_ins,(x,line[11:],int(line[:2])))
        x+=1
    if line[2:3]!=' ' and line[7:8]!=' ':
        cur.execute(city_ins,(y,line[17:],int(line[4:6]),int(line[2:4])))
        y+=1
    if line[8:9]!=' ':
        cur.execute(coun_ins,(z,line[15:],int(line[8:10]),int(line[6:8]),int(line[4:6])))
        z+=1
'''========================================='''

con.commit()#提交修改
cur.close()#关闭游标
con.close()#关闭数据库连接

