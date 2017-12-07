#!/usr/bin/env python3  
# coding=utf-8
import sys
import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import os
pypath=os.path.join(os.path.abspath(os.path.dirname(__file__))+'\IDGen.py')
sys.path.append(pypath)
pypath=os.path.join(os.path.abspath(os.path.dirname(__file__))+'\sqlite_pre.py')
sys.path.append(pypath)
import IDGen
import sqlite_pre

<<<<<<< HEAD
=======
    
>>>>>>> 9073bbb5a434e727b55e90673aa47ede6194f3a9
class Gui:
    def __init__(self,master=None):
        self.root=master
        self.addr=os.getcwd()
        if 'city' not in os.listdir(os.getcwd()):
             sqlite_pre.sqlite_pre()
        self.create_frame()
        self.state_gen()
        self.city_gen()
        self.county_gen()
        self.year_gen()
        self.month_gen()
        self.day_gen()
        self.sex_gen()
        self.gen_btn()
        self.ID_pcs()
<<<<<<< HEAD

=======

>>>>>>> 9073bbb5a434e727b55e90673aa47ede6194f3a9
    def create_frame(self):
        '''
        新建窗口，分为上下2个部分，下半部分为状态栏
        '''
        self.frm = tk.LabelFrame(self.root, 
                                     text="", 
                                     bg="purple", 
                                     fg="#1E90FF")
        self.frm.grid(row=0, column=0, sticky="wesn")
        self.create_frm()

    def create_frm(self):
        self.frm_top =tk.LabelFrame(self.frm)
        self.frm_result =tk.LabelFrame(self.frm)
        self.frm_top.grid(row=0, column=0, padx=8, pady=8, sticky="wesn")
        self.frm_result.grid(row=1, column=0, padx=8, pady=8, sticky="wesn")
        self.create_frm_top()

    def create_frm_top(self):      
        self.a='''仅用于测试使用请不要用生成的身份证号码做任何非法活动
否则后果自负!'''
        self.aten=ttk.Label(self.frm_top,text=self.a,foreground='red',font='16')
        self.aten.grid(column=1,row=2)
        self.state_gen()

    def SetPcs(self,*args):
        self.times=int(self.pcs.get())

    #生成按钮
    def clickMe(self,*args):
        self.ID=IDGen.IDGen()
        self.ID.SetNum(self.state.get(),self.city.get(),self.county.get())
        self.ID.SetSex(self.sex.get())
        self.ID.SetBirth(self.year.get(),self.month.get(),self.day.get())
        self.create_frm_result()

    def gen_btn(self,*args):
        self.action = ttk.Button(self.frm_top,text='生成',width=14)
        self.action.grid(column=2,row=5)
        self.action.bind('<Button>',self.clickMe)
       

    def ID_pcs(self,*args):
        self.pcs = ttk.Combobox(self.frm_top,width=16,state='readonly',textvariable=tk.StringVar())
        self.pcs.grid(column=1,row=5)
        self.pcs['values']=[1,5,10,20]
        self.pcs.current(0)
        self.pcs.bind('<<ComboboxSelected>>',self.SetPcs)

    #性别
    def sex_gen(self,*args):
        self.sex=ttk.Combobox(self.frm_top,state='readonly',width=14)
        self.sex['values']=('男','女')
        self.sex.grid(column=0,row=5)
        self.sex.current(0)
        self.sex.bind('<<ComboboxSelected>>',self.gen_btn)   

    def day_gen(self,*args):
        self.y=int(self.year.get())
        self.m=int(self.month.get())
        if self.m==2 :
            if self.y%4==0 and self.y%100 != 0 or self.y%400==0 :
                self.day_li=[x for x in range(1,30)]
            else:
                self.day_li=[x for x in range(1,29)]
        elif self.m in [1,3,5,7,8,10,12]:
            self.day_li=[x for x in range(1,32)]
        else:
            self.day_li=[x for x in range(1,31)]
        self.day=ttk.Combobox(self.frm_top,width=14,state='readonly',textvariable=tk.StringVar())
        self.day['values']=(self.day_li)
        self.day.grid(column=2,row=4)
        self.day.current(0)

    def month_gen(self,*args):
        self.month=ttk.Combobox(self.frm_top,width=16,state='readonly',textvariable=tk.StringVar())
        self.month_li=[x for x in range(1,13)]
        self.month['values']=(self.month_li)
        self.month.grid(column=1,row=4)
        self.month.current(0)
        self.month.bind('<<ComboboxSelected>>',self.day_gen)

    #生日
    def year_gen(self,*args):
        self.year=ttk.Combobox(self.frm_top,width=14,state='readonly',textvariable=tk.StringVar())
        self.year_li=[x for x in range(1900,2018)]
        self.year_li.reverse()
        self.year['values']=(self.year_li)
        self.year.grid(column=0,row=4)
        self.year.current(0)
        self.year.bind('<<ComboboxSelected>>',self.month_gen)
        
    #县、县级市
    def county_gen(self,*args):
        self.conn=sql.connect(self.addr+'\\city')
        self.cur=self.conn.cursor()
        self.county=self.cur.execute('SELECT COUNTY FROM COUNTYS WHERE CITY_VAL IN (SELECT CITY_VAL FROM CITYS WHERE CITY=?) AND STA_VAL IN (SELECT STA_VAL FROM STATES WHERE STA=?) ORDER BY ID ASC',(self.city.get(),self.state.get(),))
        self.county_li=[]
        for i in self.county:
            self.county_li.append(i[0])
        if self.county_li==[]:
            self.county_li=['无',]
        self.county=ttk.Combobox(self.frm_top,width=14,state='readonly',textvariable=tk.StringVar())
        self.county['values']=(self.county_li)
        self.county.grid(column=2,row=3)
        self.county.current(0)       

    #地级市
    def city_gen(self,*args):
        self.conn=sql.connect(self.addr+'\\city')
        self.cur=self.conn.cursor()
        self.city=self.cur.execute('SELECT CITY FROM CITYS AS C INNER JOIN STATES AS S \
ON C.STA_VAL=S.STA_VAL WHERE STA=? ORDER BY C.ID ASC',(self.state.get(),))
        self.city_li=[]
        for i in self.city:
            self.city_li.append(i[0])
        if self.city_li==[]:
            self.city_li=['无',]
        self.city=ttk.Combobox(self.frm_top,width=16,state='readonly',textvariable=tk.StringVar())
        self.city['values']=(self.city_li)
        self.city.grid(column=1,row=3)
        self.city.current(0)
        self.city.bind('<<ComboboxSelected>>',self.county_gen)

    def SetCityAndCoun(self,*args):
        self.city_gen()
        self.county_gen()

    #省份下拉列表
    def state_gen(self):
        self.conn=sql.connect(self.addr+'\\city')
        self.cur=self.conn.cursor()
        self.state=self.cur.execute('SELECT STA FROM STATES ORDER BY ID ASC')
        self.state_li=[]
        for i in self.state:
            self.state_li.append(i[0])
        self.state=ttk.Combobox(self.frm_top,width=14,state='readonly',textvariable=tk.StringVar())
        self.state['values']=(self.state_li)
        self.state.grid(column=0,row=3)
        self.state.current(0)
        self.state.bind('<<ComboboxSelected>>',self.SetCityAndCoun)
        
    def result_text(self,*args):
        self.res_tex=tk.Text(self.frm_result,height=20,width=20)
        self.res_tex.pack()
    def create_frm_result(self,*args):
        self.res_tex.delete(0.0,'end')
        if self.pcs.get()=='1':
            self.res_tex.insert(1.0, self.ID.GetID())
        else:
            for i in range(0,int(self.pcs.get())):
                a=self.ID.GetID()+'\n'
                i=str(i)+'.0'
                self.res_tex.insert(i, a)


root=tk.Tk()
root.title('身份证号生成器')
Gui(master=root)
root.mainloop()



          

