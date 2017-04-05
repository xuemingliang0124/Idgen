# coding=utf-8
import tkinter as tk
from tkinter import ttk
from FrS import IDGen
import sqlite3 as sql
import os
class Gui:
    def __init__(self,master=None):
        self.root=master
        self.ID=IDGen()
        self.addr=os.getcwd()
        if 'city' not in os.listdir(os.getcwd()):
            os.system(self.addr+'\\sqlite_pre.py') 
        self.create_frame()
        
    def create_frame(self):
        self.frm=tk.LabelFrame(self.root,text='',bg='black',fg='blue')
        self.frm_result=tk.LabelFrame(self.root,text='',bg='#292929',fg='#1E90FF')
        self.frm.grid(row=0,column=0,sticky='wesn')
        self.frm_result.grid(row=1,column=0,sticky='wesn')
        self.create_frm()
        self.create_frm_result()

    #生成按钮
    def clickMe(self):
        self.ID_result()
        
        

    def create_frm(self):
        self.frm_top =tk.LabelFrame(self.frm)
        self.frm_top.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")
        self.create_frm_top()

    def create_frm_top(self):
        
        self.a='''仅用于测试使用
请不要用生成的身份证号码做任何非法活动
否则后果自负!'''
        self.aten=ttk.Label(self.frm,text=self.a)
        self.aten.grid(column=1,row=2)

    #省份下拉列表

        self.state=IDGen()
        self.state_li=list(self.state.GetNumList('state'))
        self.state=ttk.Combobox(self.frm,width=12,state='readonly')
        self.state['values']=(self.state_li)
        self.state.grid(column=0,row=3)
        self.state.current(0)
        self.city_gen()
        
    #地级市
    def city_gen(self,*args):
        self.conn=sql.connect(self.addr+'\\city')
        self.cur=self.conn.cursor()
        self.city=self.cur.execute('SELECT CITY FROM CITYS AS C INNER JOIN STATES AS S \
ON C.STA_VAL=S.STA_VAL WHERE STA=?',(self.state.get(),))
        self.city_li=list(self.city)
        self.city=ttk.Combobox(self.frm,width=12,state='readonly')
        self.city['values']=(self.city_li)
        self.city.grid(column=1,row=3)
        self.city.current(0)

    #县、县级市

        self.conn=sql.connect(self.addr+'\\city')
        self.cur=self.conn.cursor()
        self.county=self.cur.execute('SELECT COUNTY FROM COUNTYS WHERE CITY_VAL="01" AND STA_VAL="11"')
        self.county_li=list(self.county)
        self.county=ttk.Combobox(self.frm,width=12,state='readonly')
        self.county['values']=(self.county_li)
        self.county.grid(column=2,row=3)
        self.county.current(0)
        self.county.bind('<B1>',self.ID.SetNum(self.state.get(),self.city.get(),self.county.get()))

    #生日

        self.year=ttk.Combobox(self.frm,width=12)
        self.year_li=[x for x in range(1900,2018)]
        self.year_li.reverse()
        self.year['values']=(self.year_li)
        self.year.grid(column=0,row=4)
        self.year.current(0)

        self.month=ttk.Combobox(self.frm,width=12)
        self.month_li=[x for x in range(1,13)]
        self.month['values']=(self.month_li)
        self.month.grid(column=1,row=4)
        self.month.current(0)

        self.day=ttk.Combobox(self.frm,width=12)
        self.day_li=[x for x in range(1,31)]
        self.day['values']=(self.day_li)
        self.day.grid(column=2,row=4)
        self.day.current(0)
        self.day.bind('<FocusOut>',self.ID.SetBirth(self.year.get(),self.month.get(),self.day.get()))
        
    #性别

        self.sex=ttk.Combobox(self.frm,width=4)
        self.sex['values']=('男','女')
        self.sex.grid(column=0,row=5)
        self.sex.current(0)
        self.sex.bind('<FocusOut>',self.ID.SetSex(self.sex.get()))
        
    def create_frm_result(self):
        self.action = ttk.Button(self.frm,text='生成',width=10)
        self.action.winfo_rgb(color='red')
        self.action.grid(column=1,row=5)
        self.action.bind('<Button1>',self.clickMe())

    def ID_result(self):
        self.result=self.ID.GetID()
        self.res_tex=ttk.Label(self.frm,text=self.result)
        self.res_tex.grid(row=6,column=0,padx=5, pady=5, sticky="wesn")

root=tk.Tk()
root.title('身份证号生成器')
Gui(master=root)
a=Gui()
a.state.bind("<<ComboboxSelected>>", a.city_gen())

root.mainloop()
