#Birthday Reminder
import pickle
import time as tm
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

#arrays for indexing
months_array = ["january","february","march","april","may","june","july","august","september","october","november","december"]
days_array = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

#converter functions
def months_index(mon=True):
    inp = mon.strip().lower()
    if isinstance(inp,bool):
        return "ERROR"
    elif isinstance(inp,str):
        for i,month in enumerate(months_array):
                if month == inp:
                    return i
        else:
            return "ERROR"
    elif isinstance(inp,int):
        try:
            month = months_array[inp]
            return month
        except:
            return "ERROR"
    else:
        return "ERROR"

def days_index(day=True):
    inp = day.strip().lower()
    if isinstance(inp,bool):
        return "ERROR"
    elif isinstance(inp,str):
        for i,day in enumerate(days_array):
                if day == inp:
                    return i
        else:
            return "ERROR"
    elif isinstance(inp,int):
        try:
            day = days_array[inp]
            return day
        except:
            return "ERROR"
    else:
        return "ERROR"

#time and date
class current_information:
    def __init__(self):
        self.refresh()
    def refresh(self):
        self.year = int(tm.strftime("%Y"))
        self.month = int(tm.strftime("%m"))-1
        self.month_name = tm.strftime("%B").strip().title()
        self.date = int(tm.strftime("%d"))
        self.day = days_index(tm.strftime("%A"))
        self.day_name = tm.strftime("%A").strip().title()
        try:
            February.Feb()
        except:
            pass
time = current_information()

#classes for lengths of time
class birthday:
    def __init__(self,name,year,month,date,image,colour):
        self.name = name
        self.year = year
        self.month = month
        self.date = date
        self.image = image
        self.colour = colour
        self.age = int(time.year) - self.year - birthday.passed(self)
        self.dict = {"name":self.name,"image":self.image,"age":self.age,"colour":self.colour}
    def passed(self):
        if time.month < self.month:
            return 1
        elif time.month == self.month:
            if time.date < self.date:
                return 1
            else:
                return 0
        else:
            return 0
class day:
    def __init__(self):
        self.day = []
    def add_birthday(self,birth):
        if isinstance(birth,birthday):
            self.day.append(birth)
        else:
            return "ERROR"
        self.birthdays = len(self.day)
        
class month:
    def __init__(self,days):
        self.days = []
        self.length = days
        for i in range(days):
            self.days.append(day())
    def get_dates(self,i):
        #get first date and colour
        self.date = time.date - time.day + i
        if self.date < 1:
            self.x = info.months[time.month-1].length + self.date
            if len(info.months[time.month-1].days[self.x-1].day)>0:
                random.shuffle(info.months[time.month-1].days[self.x-1].day)
                self.colour1 = info.months[time.month-1].days[self.x-1].day[0].colour
            else:
                self.colour1 = "black"
        elif self.date > self.length:
            self.x = self.date % self.length
            if len(info.months[time.month+1].days[self.x-1].day)>0:
                random.shuffle(info.months[time.month+1].days[self.x-1].day)
                self.colour1 = info.months[time.month+1].days[self.x-1].day[0].colour
            else:
                self.colour1 = "black"
        else:
            self.x = self.date
            if len(self.days[self.date-1].day)>0:
                random.shuffle(self.days[self.x-1].day)
                self.colour1 = self.days[self.x-1].day[0].colour
            else:
                self.colour1 = "black"
        #get second date and colour
        self.date = (time.date - time.day + i + 7)
        if self.date > self.length:
            self.y = self.date % self.length
            if len(info.months[time.month+1].days[self.y-1].day)>0:
                random.shuffle(info.months[time.month+1].days[self.y-1].day)
                self.colour2 = info.months[time.month+1].days[self.y-1].day[0].colour
            else:
                self.colour2 = "black"
        else:
            self.y = self.date
            if len(self.days[self.y-1].day)>0:
                random.shuffle(self.days[self.y-1].day)
                self.colour2 = self.days[self.y-1].day[0].colour
            else:
                self.colour2 = "black"
        return self.x,self.y,self.colour1,self.colour2
    def day_len(self,year):
        if year % 4 != 0:
            return 28
        else:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
    def Feb():
        if year % 4 != 0:
            self.length = 28
        else:
            if year % 100 == 0:
                if year % 400 == 0:
                    self.length = 29
                else:
                    self.length = 28
            else:
                self.length = 29

try:
    January = pickle.load(open("January",'rb'))
    February = pickle.load(open("February",'rb'))
    March = pickle.load(open("March",'rb'))
    April = pickle.load(open("April",'rb'))
    May = pickle.load(open("May",'rb'))
    June = pickle.load(open("June",'rb'))
    July = pickle.load(open("July",'rb'))
    August = pickle.load(open("August",'rb'))
    September = pickle.load(open("September",'rb'))
    October = pickle.load(open("October",'rb'))
    November = pickle.load(open("November",'rb'))
    December = pickle.load(open("December",'rb'))
except:
    print("ERROR LOADING FILES: ALL MONTHS RESET")
    January = month(31)
    February = month(29)
    March = month(31)
    April = month(30)
    May = month(31)
    June = month(30)
    July = month(31)
    August = month(31)
    September = month(30)
    October = month(31)
    November = month(30)
    December = month(31)

class year:
    def __init__(self):
        self.months = [January,February,March,April,May,June,July,August,September,October,November,December]
        self.today = self.months[time.month].days[time.date-1]
info = year()
day_length = len(info.today.day)

#add birthday
def add_birthday(name,year,month,date,image,colour):
    info.months[month].days[date-1].add_birthday(birthday(name,year,month,date,image,colour))
        
#declare GUI
root = Tk()
root.title("Birthday Reminder")

#set up images
Balloons = ImageTk.PhotoImage(Image.open("Balloons.png"))
Present = ImageTk.PhotoImage(Image.open("Present.png"))
Cake = ImageTk.PhotoImage(Image.open("Cake.png"))
Flowers = ImageTk.PhotoImage(Image.open("Flowers.png"))

#set text colour
if day_length > 0:
    random.shuffle(info.today.day)
    colour = info.today.day[0].colour
else:
    colour = "black"

class label:
    def __init__(self,parent,words,color=colour):
        self.f = Frame(parent)
        self.l = Label(self.f,text=words,fg=color)
    def grid(self,row,col,x=0,y=0):
        self.f.grid(row=row,column=col)
        self.l.grid(row=1,column=1,padx=x,pady=y)
        ttk.Separator(self.f,orient="vertical").grid(row=0,column=0,sticky="NS",rowspan=3,padx=0,pady=0)
        ttk.Separator(self.f,orient="horizontal").grid(row=0,column=0,columnspan=3,sticky="EW",padx=0,pady=0)
        ttk.Separator(self.f,orient="vertical").grid(row=0,column=2,sticky="NS",rowspan=3,padx=0,pady=0)
        ttk.Separator(self.f,orient="horizontal").grid(row=3,column=0,columnspan=3,sticky="EW",padx=0,pady=0)

#create frames
frame = Frame(root)
frame.grid(row=0,column=0)

frame1 = Frame(frame)
frame1.grid(row=0,column=0)

frame2 = Frame(frame)
frame2.grid(row=1,column=0)

frame3 = Frame(frame)
frame3.grid(row=2,column=0)

aframe = Frame(frame)
aframe.grid(row=4,column=0)

frame4 = Frame(frame)
frame4.grid(row=5,column=0)

for wig in frame.winfo_children():
    wig.grid(padx=10,pady=2)

ttk.Separator(frame,orient="horizontal").grid(row=3,column=0,padx=0,pady=(2,0),stick="EW")
def reset():
    pickle.dump(January, open( "January", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(February, open( "February", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(March, open( "March", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(April, open( "April", "wb" ),pickle.HIGHEST_PROTOCOL )
    pickle.dump(May, open( "May", "wb" ),pickle.HIGHEST_PROTOCOL )
    pickle.dump(June, open( "June", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(July, open( "July", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(August, open( "August", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(September, open( "September", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(October, open( "October", "wb" ),pickle.HIGHEST_PROTOCOL )
    pickle.dump(November, open( "November", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    pickle.dump(December, open( "December", "wb" ) ,pickle.HIGHEST_PROTOCOL)
    day_length = len(info.today.day)
    #set text colour
    if day_length > 0:
        random.shuffle(info.today.day)
        colour = info.today.day[0].colour
    else:
        colour = "black"
    #remove all
    for wig in frame1.winfo_children():
        wig.grid_remove()
    for wig in frame2.winfo_children():
        wig.grid_remove()
    for wig in frame3.winfo_children():
        wig.grid_remove()
    for wig in frame4.winfo_children():
        wig.grid_forget()
    #date at to
    date = StringVar()
    date.set("{} {} {} {}".format(time.day_name,time.date,time.month_name,time.year))
    date_label = Label(frame1,text=date.get(),fg=colour)
    date_label.grid(row=1,column=1,padx=10,pady=5)
    #separators
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=0,padx=(0,150),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=2,padx=(150,0),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=3,column=0,columnspan=3,padx=0,pady=0,stick="EW")

    #week grid
    Mon = Label(frame2,text="M")
    Tue = Label(frame2,text="T")
    Wed = Label(frame2,text="W")
    Thu = Label(frame2,text="T")
    Fri = Label(frame2,text="F")
    Sat = Label(frame2,text="S")
    Sun = Label(frame2,text="S")
    day_widgets = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]
    #dates
    for i,wig in enumerate(day_widgets):
        wig.config(fg=colour)
        wig.grid(row=1,column=2*i+1,padx=10,pady=5)
        week1 = IntVar()
        week2 = IntVar()
        week1,week2,c1,c2 = info.months[time.month].get_dates(i)
        Label(frame2,text=week1,fg=c1).grid(row=3,column=2*i+1,padx=10,pady=5)
        Label(frame2,text=week2,fg=c2).grid(row=5,column=2*i+1,padx=15,pady=5)
        #separators
        ttk.Separator(frame2,orient="vertical").grid(row=1,column=2*i,padx=5,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="vertical").grid(row=1,column=15,padx=0,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="horizontal").grid(row=0,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=2,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=4,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=6,column=0,columnspan=16,padx=3,pady=0,stick="EW")

    #happy birthday
    if day_length > 0:
        #initial separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        
        for i,person in enumerate(info.today.day):
            #text and images
            name_label = Label(frame3,text="{name} is {age} years old today".format(**person.dict),fg=person.colour)
            if person.image == "Flowers":
                cimage = Flowers
            elif person.image == "Cake":
                cimage = Cake
            elif person.image == "Present":
                cimage = Present
            elif person.image == "Balloons":
                cimage = Balloons
            image_label = Label(frame3,image=cimage)
            name_label.grid(row=1,column=2*i+1,padx=10,pady=5)
            image_label.grid(row=2,column=2*i+1,padx=5,pady=5)
            #separators
            ttk.Separator(frame3,orient="vertical").grid(row=0,column=2*(i+1),padx=0,pady=0,stick="NS",rowspan=4)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=3,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
    else:
        #label
        none = Label(frame3,text="No birthdays saved today!",fg=colour)
        none.grid(row=1,column=1,padx=100,pady=(50,100))

        #separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=2,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=2,column=0,columnspan=3,padx=0,pady=0,stick="EW")

#adding/deleting birthdays
#functions
def choose():
    for wig in frame4.winfo_children():
        wig.grid_forget()
    if option.get() == "Add":
        add()
    elif option.get() == "Remove":
        remove()
    
def add():
    step1a()
def remove():
    step1b()
def step1a():
    #ask for the year
    year_label = Label(frame4,text="Year",fg=colour)
    year_label.grid(row=2,column=1,pady=0)
    global byear
    byear = StringVar()
    year_entry = Entry(frame4,textvariable=byear)
    year_entry.grid(row=3,column=1)
    global move, year_tick
    move = IntVar()
    move.set(0)
    year_tick = Checkbutton(frame4,variable=move,command=check1a)
    year_tick.grid(row=3,column=2)
def check1a():
    #check the year
    if move.get() == 1:
        error1 = Label(frame4,text="Please enter a valid year between 1900 and now.",wraplength=150,fg="red")
        try:
            global add_year
            add_year = int(byear.get())
            if not(add_year >= 1900 and add_year <= time.year):
                error1.grid(row=3,column=3)
                move.set(0)
            else:
                error1.config(fg="#F0F0F0")
                error1.grid(row=3,column=3)
                step2a()
        except:
            error1.grid(row=3,column=3)
            move.set(0)
def step2a():
    #ask for the month
    month_label = Label(frame4,text="Month",fg=colour)
    month_label.grid(row=2,column=3,padx=5,pady=0)
    year_tick.config(state="disabled")
    year_label = label(frame4,byear.get())
    year_label.grid(3,1,45,1)
    global bmonth,months_arr
    bmonth = StringVar()
    months_arr = []
    for month in months_array:
        months_arr.append(month.capitalize())
    if byear.get() == str(time.year):
        for month in months_array:
            months_arr.append(month.capitalize())
        month_menu = ttk.OptionMenu(frame4,bmonth,months_arr[0],*months_arr[:time.month+1])
    else:
        month_menu = ttk.OptionMenu(frame4,bmonth,months_arr[0],*months_arr)
    month_menu.grid(row=3,column=3,pady=5,padx=5)
    global move1, month_tick
    move1 = IntVar()
    move1.set(0)
    month_tick = Checkbutton(frame4,variable=move1,command=check2a)
    month_tick.grid(row=3,column=4)
def check2a():
    #check the month
    if move1.get() == 1:
        for i,month in enumerate(months_arr):
            if month == bmonth.get():
                global add_month
                add_month = i
                step3a()
def step3a():
    #ask for the day
    day_label = Label(frame4,text="Day",fg=colour)
    day_label.grid(row=2,column=5,padx=5,pady=0)
    month_tick.config(state="disabled")
    month_label = label(frame4,bmonth.get())
    month_label.grid(3,3,45,1)
    global bday,day_arr
    bday = IntVar()
    days_arr = []
    for day in range(1,32):
        days_arr.append(day)
    if byear.get() == str(time.year) and bmonth.get() == time.month_name:
        day_menu = ttk.OptionMenu(frame4,bday,days_arr[0],*days_arr[:time.date-1])
    elif bmonth.get() == "February":
        day_menu = ttk.OptionMenu(frame4,bday,days_arr[0],*days_arr[:February.day_len(add_year)])
    else:
        day_menu = ttk.OptionMenu(frame4,bday,days_arr[0],*days_arr[:info.months[add_month].length])
    day_menu.grid(row=3,column=5,pady=5,padx=5)
    global move2, day_tick
    move2 = IntVar()
    move2.set(0)
    day_tick = Checkbutton(frame4,variable=move2,command=check3a)
    day_tick.grid(row=3,column=6)
def check3a():
    #check the day
    if move2.get() == 1:
        global add_day
        add_day = bday.get()
        step4a()
def step4a():
    day_tick.config(state="disabled")
    day_label = label(frame4,bday.get())
    day_label.grid(3,5,20,1)
    #name
    name_label = Label(frame4,text="Name",fg=colour)
    name_label.grid(row=4,column=1,padx=5,pady=0)
    global bname
    bname = StringVar()
    name_entry = Entry(frame4,textvariable=bname)
    name_entry.grid(row=5,column=1)
    #image
    image_label = Label(frame4,text="Image",fg=colour)
    image_label.grid(row=6,column=1)
    images = Frame(frame4)
    images.grid(row=7,column=1,columnspan=2,rowspan=2)
    global bimage
    bimage = StringVar()
    flowers = Radiobutton(images,text="Flowers",variable=bimage,value="Flowers",fg=colour)
    flowers.grid(row=2,column=2)
    cake = Radiobutton(images,text="Cake",variable=bimage,value="Cake",fg=colour)
    cake.grid(row=1,column=2)
    present = Radiobutton(images,text="Present",variable=bimage,value="Present",fg=colour)
    present.grid(row=2,column=1)
    balloons = Radiobutton(images,text="Balloons",variable=bimage,value="Balloons",fg=colour)
    balloons.grid(row=1,column=1)
    #separators
    ttk.Separator(images,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(images,orient="vertical").grid(row=0,column=3,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(images,orient="horizontal").grid(row=0,column=0,columnspan=4,padx=0,pady=0,stick="EW")
    ttk.Separator(images,orient="horizontal").grid(row=3,column=0,columnspan=4,padx=0,pady=0,stick="EW")
    #colours
    colour_label = Label(frame4,text="Colour",fg=colour)
    colour_label.grid(row=4,column=3)
    colours = Frame(frame4)
    colours.grid(row=5,column=3,columnspan=4,rowspan=2)
    global bcolour
    bcolour = StringVar()
    for i,color in enumerate(["red","green","blue","brown","orange","purple","lime","cyan","maroon","indigo"]):
        col = Radiobutton(colours,text=color.capitalize(),variable=bcolour,value=color,fg=color)
        col.grid(column=i//2+1,row=i%2+1)
    #separators
    ttk.Separator(colours,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(colours,orient="vertical").grid(row=0,column=6,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(colours,orient="horizontal").grid(row=0,column=0,columnspan=6,padx=0,pady=0,stick="EW")
    ttk.Separator(colours,orient="horizontal").grid(row=3,column=0,columnspan=6,padx=0,pady=0,stick="EW")
    finish = Button(frame4,text="Save",command=save,fg=colour)
    stop = Button(frame4,text="Cancel",command=cancel,fg=colour)
    stop.grid(column=6,row=7)
    finish.grid(column=5,row=7)
def save():
    error2 = Label(frame4,text="Error, please select valid options",wraplength = 100,fg="red")
    if not((bimage.get() == "Flowers" or bimage.get() == "Cake" or bimage.get() == "Present" or bimage.get() == "Balloons") and bcolour.get() in ["red","green","blue","brown","orange","purple","lime","cyan","maroon","indigo"] and len(bname.get()) > 0):
        error2.grid(column=3,row=7)
    else:
        add_birthday(bname.get(),add_year,add_month,add_day,bimage.get(),bcolour.get())
        reset()
def cancel():
    for wig in frame4.winfo_children():
        wig.grid_forget()
def step1b():
    month_label = Label(frame4,text="Month",fg=colour)
    month_label.grid(row=1,column=1,padx=5,pady=0)
    global bmonth,months_arr
    bmonth = StringVar()
    months_arr = []
    for month in months_array:
        months_arr.append(month.capitalize())
    month_menu = ttk.OptionMenu(frame4,bmonth,months_arr[0],*months_arr)
    month_menu.grid(row=2,column=1,pady=5,padx=5)
    global move1, month_tick
    move1 = IntVar()
    move1.set(0)
    month_tick = Checkbutton(frame4,variable=move1,command=check1b)
    month_tick.grid(row=2,column=2)
def check1b():
    #check the month
    if move1 == 1:
        for i,month in enumerate(months_arr):
            if month == bmonth.get():
                global rem_month
                rem_month = i
                step2b()
def step2b():
    day_label = Label(frame4,text="Day",fg=colour)
    day_label.grid(row=1,column=3,padx=5,pady=0)
    month_tick.config(state="disabled")
    month_label = label(frame4,bmonth.get())
    month_label.grid(2,1,45,1)
    global bday,day_arr
    bday = IntVar()
    days_arr = []
    for day in range(info.months[rem_month].length):
        days_arr.append(day+1)
    day_menu = ttk.OptionMenu(frame4,bday,days_arr[0],*days_arr[:info.months[rem_month].length])
    day_menu.grid(row=2,column=3,pady=5,padx=5)
    global move2, day_tick
    move2 = IntVar()
    move2.set(0)
    day_tick = Checkbutton(frame4,variable=move2,command=check2b)
    day_tick.grid(row=2,column=4)
def check2b():
    #check the day
    if move2.get() == 1:
        global rem_day
        rem_day = bday.get()
        step3b()
def step3b():
    day_tick.config(state="disabled")
    day_label = label(frame4,bday.get())
    day_label.grid(2,3,20,1)
    stop = Button(frame4,text="Cancel",command=cancel,fg=colour)
    submit = Button(frame4,text="Delete",command=delete,fg=colour)
    if len(info.months[rem_month].days[rem_day-1].day) > 0:
        stop.grid(column=4,row=3,pady=5)
        global pers
        pers = StringVar()
        births = []
        for person in info.months[rem_month].days[rem_day-1].day:
            births.append("{name} ({age})".format(**person.dict))
            
        bremove = ttk.OptionMenu(frame4,pers,births[0],*births)
        bremove.grid(column=1,row=3)
        submit.grid(column=3,row=3)
    else:
        error = Label(frame4,text="No birthdays found",fg="red")
        error.grid(column=1,row=3,pady=5)
        stop.grid(column=3,row=3,pady=5)
def delete():
    for i,per in enumerate(info.months[rem_month].days[rem_day-1].day):
        if "{name} ({age})".format(**per.dict) == pers.get():
            info.months[rem_month].days[rem_day-1].day.pop(i)
    reset()
def reset_time():
    time.refresh()
    day_length = len(info.today.day)
    #set text colour
    if day_length > 0:
        random.shuffle(info.today.day)
        colour = info.today.day[0].colour
    else:
        colour = "black"
    #remove all
    for wig in frame1.winfo_children():
        wig.grid_remove()
    for wig in frame2.winfo_children():
        wig.grid_remove()
    for wig in frame3.winfo_children():
        wig.grid_remove()
    #date at to
    date = StringVar()
    date.set("{} {} {} {}".format(time.day_name,time.date,time.month_name,time.year))
    date_label = Label(frame1,text=date.get(),fg=colour)
    date_label.grid(row=1,column=1,padx=10,pady=5)
    #separators
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=0,padx=(0,150),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=2,padx=(150,0),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=3,column=0,columnspan=3,padx=0,pady=0,stick="EW")

    #week grid
    Mon = Label(frame2,text="M")
    Tue = Label(frame2,text="T")
    Wed = Label(frame2,text="W")
    Thu = Label(frame2,text="T")
    Fri = Label(frame2,text="F")
    Sat = Label(frame2,text="S")
    Sun = Label(frame2,text="S")
    day_widgets = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]
    #dates
    for i,wig in enumerate(day_widgets):
        wig.config(fg=colour)
        wig.grid(row=1,column=2*i+1,padx=10,pady=5)
        week1 = IntVar()
        week2 = IntVar()
        week1,week2,c1,c2 = info.months[time.month].get_dates(i)
        Label(frame2,text=week1,fg=c1).grid(row=3,column=2*i+1,padx=10,pady=5)
        Label(frame2,text=week2,fg=c2).grid(row=5,column=2*i+1,padx=15,pady=5)
        #separators
        ttk.Separator(frame2,orient="vertical").grid(row=1,column=2*i,padx=5,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="vertical").grid(row=1,column=15,padx=0,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="horizontal").grid(row=0,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=2,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=4,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=6,column=0,columnspan=16,padx=3,pady=0,stick="EW")

    #happy birthday
    if day_length > 0:
        #initial separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        
        for i,person in enumerate(info.today.day):
            #text and images
            name_label = Label(frame3,text="{name} is {age} years old today".format(**person.dict),fg=person.colour)
            if person.image == "Flowers":
                cimage = Flowers
            elif person.image == "Cake":
                cimage = Cake
            elif person.image == "Present":
                cimage = Present
            elif person.image == "Balloons":
                cimage = Balloons
            image_label = Label(frame3,image=cimage)
            name_label.grid(row=1,column=2*i+1,padx=10,pady=5)
            image_label.grid(row=2,column=2*i+1,padx=5,pady=5)
            #separators
            ttk.Separator(frame3,orient="vertical").grid(row=0,column=2*(i+1),padx=0,pady=0,stick="NS",rowspan=4)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=3,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
    else:
        #label
        none = Label(frame3,text="No birthdays saved today!",fg=colour)
        none.grid(row=1,column=1,padx=100,pady=(50,100))

        #separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=2,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=2,column=0,columnspan=3,padx=0,pady=0,stick="EW")
    length = 1000*(3600*(23-int(tm.strftime("%H")))+60*(60-int(tm.strftime("%M"))))
    root.after(length, reset_time)
#initial choice
reset_time()
reset()
options = ["Add","Remove"]
option = StringVar()
add_del = ttk.OptionMenu(aframe,option,options[0],*options)
add_del.grid(row=0,column=0,pady=5)
submit1 = Button(aframe,text="Enter",command=choose)
submit1.grid(row=0,column=1)
root.mainloop()

