# coding=utf-8
import tkinter as tk
from tkinter import ttk
from FrS import IDGen
import random
win=tk.Tk()
win.title('身份证号生成器')
a='''仅用于测试使用
请不要拿生成的身份证号码做任何非法活动
否则后果自负!'''
ttk.Label(win,text=a).grid(column=1,row=2)

#省份下拉列表
state1=IDGen()
state2=state1.GetNumDict('state')
state_li=list(state2.keys())
state=ttk.Combobox(win,width=12,textvariable='省、直辖市')
state['values']=(state_li)
state.grid(column=0,row=3)
state.current(0)

#地级市
city1=IDGen()
city2=city1.GetNumDict('city')
city_li=list(city2.keys())
city=ttk.Combobox(win,width=12,textvariable='地级市')
city['values']=(city_li)
city.grid(column=1,row=3)
city.current(0)

#县、县级市
county1=IDGen()
county2=county1.GetNumDict('county')
county_li=list(county2.keys())
county=ttk.Combobox(win,width=12,textvariable='县、县级市')
county['values']=(county_li)
county.grid(column=2,row=3)
county.current(0)

year=ttk.Combobox(win,width=12,textvariable='出生年')
year1=[x for x in range(1900,2018)]
year1.reverse()
year['values']=(year1)
year.grid(column=0,row=4)
year.current(0)

month=ttk.Combobox(win,width=12,textvariable='月')
month1=[x for x in range(1,13)]
month['values']=(month1)
month.grid(column=1,row=4)
month.current(0)

day=ttk.Combobox(win,width=12,textvariable='日')
day1=[x for x in range(1,31)]
day['values']=(month1)
day.grid(column=2,row=4)
day.current(0)
#生成按钮
action = ttk.Button(win,text='生成',command=clickMe)
action.grid(column=2,row=6)

def clickMe():
    pass
win.mainloop()
