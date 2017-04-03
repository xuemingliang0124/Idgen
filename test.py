# coding=utf-8
import tkinter as tk
from tkinter import ttk
from FrS import IDGen
import sqlite3 as sql
import os
class Gui:
    def __init__(self,parent):
        self.path=os.getcwd() 
        self.aten_label()
        self.state_comb()
        self.city_comb()
        self.county_comb()
        self.year_comb()
        self.month_comb()
        self.day_comb()
        self.sex_comb()
        self.gen_btn()
           
    def aten_label(self):
        self.a='''仅用于测试使用
        请不要用生成的身份证号码做任何非法活动
        否则后果自负!'''
        self.aten=ttk.Label(text=self.a)
        self.aten.grid(column=1,row=2)

    #省份下拉列表
    def state_comb(self):
        self.conn=sql.connect(self.path+'\\city')
        self.cur=self.conn.cursor()
        self.state=self.cur.execute('SELECT STA FROM STATES')
        
        self.state_li=list(self.state)
        self.state=ttk.Combobox(width=12,textvariable='省、直辖市',state='readonly')
        self.state['values']=(self.state_li)
        self.state.grid(column=0,row=3)
        self.state.current(0)
        

    #地级市
    def city_comb(self):
        self.conn=sql.connect(self.path+'\\city')
        self.cur=self.conn.cursor()
        self.city=self.cur.execute('SELECT CITY FROM CITYS WHERE STA_VAL=11')
        self.city_li=list(self.city)
        self.city=ttk.Combobox(width=12,textvariable='地级市',state='readonly')
        self.city['values']=(self.city_li)
        self.city.grid(column=1,row=3)
        self.city.current(0)


    #县、县级市
    def county_comb(self):
        self.conn=sql.connect(self.path+'\\city')
        self.cur=self.conn.cursor()
        self.county=self.cur.execute('SELECT COUNTY FROM COUNTY WHERE CITY_VAL="01" AND STA_VAL="11"')
        self.county_li=list(self.county)
        self.county=ttk.Combobox(width=12,textvariable='县、县级市',state='readonly')
        self.county['values']=(self.county_li)
        self.county.grid(column=2,row=3)
        self.county.current(0)

    def year_comb(self):
        self.year=ttk.Combobox(width=12,textvariable='出生年')
        self.year_li=[x for x in range(1900,2018)]
        self.year_li.reverse()
        self.year['values']=(self.year_li)
        self.year.grid(column=0,row=4)
        self.year.current(0)

    def month_comb(self):
        self.month=ttk.Combobox(width=12,textvariable='月')
        self.month_li=[x for x in range(1,13)]
        self.month['values']=(self.month_li)
        self.month.grid(column=1,row=4)
        self.month.current(0)

    def day_comb(self):
        self.day=ttk.Combobox(width=12,textvariable='日')
        self.day_li=[x for x in range(1,31)]
        self.day['values']=(self.day_li)
        self.day.grid(column=2,row=4)
        self.day.current(0)

    def sex_comb(self):
        self.sex=ttk.Combobox(width=4)
        self.sex['values']=('男','女')
        self.sex.grid(column=0,row=5)
        self.sex.current(0)

    #生成按钮
    def clickMe(self):
        self.state_gen=self.state.get()
        self.city_gen=self.city.get()
        self.county_gen=self.county.get()
        self.year_gen=self.year.get()
        self.month_gen=self.month.get()
        self.day_gen=self.day.get()
        self.sex_gen=self.sex.get()
        aaa=IDGen()
        return aaa.SetNum(str(self.state_gen),self.city_gen,self.county_gen)
    def gen_btn(self):    
        self.action = ttk.Button(text='生成',width=10,command=self.clickMe())
        self.action.grid(column=1,row=5)


if __name__=='__main__':
    root=tk.Tk()
    root.title('身份证号生成器')
    app=Gui(root)
    root.mainloop()
