# coding=utf-8
import os
def GetStateNumeber(x,y,z):
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
