#Birthday Reminder
from tkinter import *
from tkinter import ttk
from time_periods import *
from Time import Time
from Images import image
from GUI import *
import random
#find the Time and declare it
Time = Time.Time()
months_array = ["January","February","March","April","May","June","July","August","September","October","November","December"]
#define a colour
global colour
colour = "default"
#year object
class year:
    def __init__(self):
        #retrieve months
        self.months = [January,February,March,April,May,June,July,August,September,October,November,December]
        #find current day
        self.today = self.months[Time.month].days[Time.date-1]

#get months
January,February,March,April,May,June,July,August,September,October,November,December = load()

#set up variables
def configure():
    global day_length,colour
    #set day length (birthdays today)
    day_length = len(info.today.day)
    #set text colour
    if day_length > 0:
        #choose random birthday
        random.shuffle(info.today.day)
        colour = info.today.day[0].colour
    elif colour == "default":
        colour = random.choice(["red","green","blue","brown","orange","purple","lime","cyan","maroon","indigo"])


#create GUI
def reset():
    configure()
    reset_time()
    save(January,February,March,April,May,June,July,August,September,October,November,December)
    f1(frame1,Time.day_name,Time.date,Time.month_name,Time.year,colour)
    f2(frame2,colour,info,Time.month)
    f3(frame3,day_length,colour,info,[Flowers,Cake,Present,Balloons])
    f4and5()

configure()
#label with a frame
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

#auto update
def reset_time():
    #update Time
    Time.refresh()
    configure()
    #frame functions
    f1(frame1,Time.day_name,Time.date,Time.month_name,Time.year,colour)
    f2(frame2,colour,info,Time.month)
    f3(frame3,day_length,colour,info,[Flowers,Cake,Present,Balloons])
    #check again in a minute
    root.after(60000, reset_time)

#result of choosing add/remove
def choose():
    #clear
    clear(frame5)
    if option.get() == "Add":
        step1a()
    elif option.get() == "Remove":
        step1b()
    elif option.get() == "View":
        step1c()

#frame 5
def f4and5(x=True):
    #clear
    clear(frame5)
    #options choice
    global option
    try:
        #if it exists, reset
        option.set("Add")
    except:
        if x:
            #otherwise, create it
            options = ["Add","View","Remove"]
            option = StringVar()
            add_del = ttk.OptionMenu(frame4,option,options[0],*options)
            add_del.grid(row=0,column=0,pady=5)
            #submit button
            submit1 = Button(frame4,text="Enter",command=choose)
            submit1.grid(row=0,column=1)

#add sequence
def step1a():
    #ask for the year
    year_label = Label(frame5,text="Year",fg=colour)
    year_label.grid(row=2,column=1,pady=0)
    global byear
    byear = StringVar()
    #year entry
    year_entry = Entry(frame5,textvariable=byear)
    year_entry.grid(row=3,column=1)
    global move, year_tick
    move = IntVar()
    move.set(0)
    #check button to confirm year
    year_tick = Checkbutton(frame5,variable=move,command=check1a)
    year_tick.grid(row=3,column=2)
def check1a():
    #check the year
    if move.get() == 1:
        error1 = Label(frame5,text="Please enter a valid year between 1900 and now.",wraplength=150,fg="red")
        try:
            #check the year is reasonable
            global add_year
            add_year = int(byear.get())
            if not(add_year >= 1900 and add_year <= Time.year):
                #display error message
                error1.grid(row=3,column=3)
                move.set(0)
            else:
                #hide error message and move on
                error1.config(fg="#F0F0F0")
                error1.grid(row=3,column=3)
                move.set(1)
                
                step2a()
        except:
            #display error message
            error1.grid(row=3,column=3)
            move.set(0)
def step2a():
    #ask for the month
    month_label = Label(frame5,text="Month",fg=colour)
    month_label.grid(row=2,column=3,padx=5,pady=0)
    #disable year confirm
    year_tick.config(state="disabled")
    #stop editing year
    year_label = label(frame5,byear.get())
    year_label.grid(3,1,45,1)
    global bmonth,months_arr
    bmonth = StringVar()
    #get list of months
    months_arr = []
    for month in months_array:
        months_arr.append(month.capitalize())
    if byear.get() == str(Time.year):
        #slice to current month (no future bithdays)
        month_menu = ttk.OptionMenu(frame5,bmonth,months_arr[Time.month],*months_arr[:Time.month+1])
    else:
        month_menu = ttk.OptionMenu(frame5,bmonth,months_arr[Time.month],*months_arr)
    month_menu.grid(row=3,column=3,pady=5,padx=5)
    global move1, month_tick
    move1 = IntVar()
    move1.set(0)
    #confirm checkbutton
    month_tick = Checkbutton(frame5,variable=move1,command=check2a)
    month_tick.grid(row=3,column=4)
def check2a():
    #check the month
    if move1.get() == 1:
        for i,month in enumerate(months_arr):
            if month == bmonth.get():
                global add_month
                #save the position as int for later
                add_month = i
                step3a()
def step3a():
    #ask for the day
    day_label = Label(frame5,text="Day",fg=colour)
    day_label.grid(row=2,column=5,padx=5,pady=0)
    #disable year confirm
    month_tick.config(state="disabled")
    #stop editing month
    month_label = label(frame5,bmonth.get())
    month_label.grid(3,3,45,1)
    global bday,day_arr
    bday = IntVar()
    days_arr = []
    #create a list
    for day in range(1,32):
        days_arr.append(day)
    if byear.get() == str(Time.year) and bmonth.get() == Time.month_name:
        #slice at the present
        day_menu = ttk.OptionMenu(frame5,bday,days_arr[Time.date-1],*days_arr[:Time.date])
    elif bmonth.get() == "February":
        #make sure the date exists
        day_menu = ttk.OptionMenu(frame5,bday,days_arr[0],*days_arr[:February.day_len(add_year)])
    else:
        #find length of month
        day_menu = ttk.OptionMenu(frame5,bday,days_arr[0],*days_arr[:info.months[add_month].length])
    day_menu.grid(row=3,column=5,pady=5,padx=5)
    global move2, day_tick
    move2 = IntVar()
    move2.set(0)
    #checkbutton to confirm
    day_tick = Checkbutton(frame5,variable=move2,command=check3a)
    day_tick.grid(row=3,column=6)
def check3a():
    #check the day
    if move2.get() == 1:
        global add_day
        #save day
        add_day = bday.get()
        step4a()
def step4a():
    #disable day confirm
    day_tick.config(state="disabled")
    #stop editing day
    day_label = label(frame5,bday.get())
    day_label.grid(3,5,20,1)
    #name entry
    name_label = Label(frame5,text="Name",fg=colour)
    name_label.grid(row=4,column=1,padx=5,pady=0)
    global bname
    bname = StringVar()
    name_entry = Entry(frame5,textvariable=bname)
    name_entry.grid(row=5,column=1)
    #image choice
    image_label = Label(frame5,text="Image",fg=colour)
    image_label.grid(row=6,column=1)
    images = Frame(frame5)
    images.grid(row=7,column=1,columnspan=2,rowspan=2)
    global bimage
    #radiobutton options
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
    #colour choice
    colour_label = Label(frame5,text="Colour",fg=colour)
    colour_label.grid(row=4,column=3)
    colours = Frame(frame5)
    colours.grid(row=5,column=3,columnspan=4,rowspan=2)
    global bcolour
    bcolour = StringVar()
    #colour options
    for i,color in enumerate(["red","green","blue","brown","orange","purple","lime","cyan","maroon","indigo"]):
        col = Radiobutton(colours,text=color.capitalize(),variable=bcolour,value=color,fg=color)
        col.grid(column=i//2+1,row=i%2+1)
    #separators
    ttk.Separator(colours,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(colours,orient="vertical").grid(row=0,column=6,padx=0,pady=0,stick="NS",rowspan=4)
    ttk.Separator(colours,orient="horizontal").grid(row=0,column=0,columnspan=6,padx=0,pady=0,stick="EW")
    ttk.Separator(colours,orient="horizontal").grid(row=3,column=0,columnspan=6,padx=0,pady=0,stick="EW")
    #option to save and move on
    finish = Button(frame5,text="Save",command=lambda:b_save(frame5,bimage,bcolour,bname,add_year,add_month,add_day,info),fg=colour)
    #option to abort
    stop = Button(frame5,text="Cancel",command=lambda:f4and5(False),fg=colour)
    stop.grid(column=6,row=7)
    finish.grid(column=5,row=7)

#remove sequence
def step1b():
    month_label = Label(frame5,text="Month",fg=colour)
    month_label.grid(row=1,column=1,padx=5,pady=0)
    global bmonth,months_arr
    bmonth = StringVar()
    #create list of months
    months_arr = []
    for month in months_array:
        months_arr.append(month.capitalize())
    #choose months
    month_menu = ttk.OptionMenu(frame5,bmonth,months_arr[Time.month],*months_arr)
    month_menu.grid(row=2,column=1,pady=5,padx=5)
    #confirm checkbutton
    global move1, month_tick
    move1 = IntVar()
    move1.set(0)
    month_tick = Checkbutton(frame5,variable=move1,command=check1b)
    month_tick.grid(row=2,column=2)
def check1b():
    #check the month
    if move1.get() == 1:
        for i,month in enumerate(months_arr):
            if month == bmonth.get():
                global rem_month
                #save the month as an integer
                rem_month = i
                step2b()
def step2b():
    day_label = Label(frame5,text="Day",fg=colour)
    day_label.grid(row=1,column=3,padx=5,pady=0)
    #disable month confirm
    month_tick.config(state="disabled")
    #stop editing month
    month_label = label(frame5,bmonth.get())
    month_label.grid(2,1,45,1)
    global bday,day_arr
    bday = IntVar()
    days_arr = []
    #days array
    for day in range(info.months[rem_month].length):
        days_arr.append(day+1)
    day_menu = ttk.OptionMenu(frame5,bday,days_arr[0],*days_arr[:info.months[rem_month].length])
    day_menu.grid(row=2,column=3,pady=5,padx=5)
    global move2, day_tick
    move2 = IntVar()
    move2.set(0)
    #day confirm checkbutton
    day_tick = Checkbutton(frame5,variable=move2,command=check2b)
    day_tick.grid(row=2,column=4)
def check2b():
    #check the day
    if move2.get() == 1:
        global rem_day
        #save day
        rem_day = bday.get()
        step3b()
def step3b():
    #disable day confirm
    day_tick.config(state="disabled")
    #stop editing day
    day_label = label(frame5,bday.get())
    day_label.grid(2,3,20,1)
    #abort button
    stop = Button(frame5,text="Cancel",command=lambda:f4and5(False),fg=colour)
    #remove button
    submit = Button(frame5,text="Delete",command=lambda:delete(info),fg=colour)
    #list of birthdays on that day
    if len(info.months[rem_month].days[rem_day-1].day) > 0:
        stop.grid(column=4,row=4,pady=5)
        global pers
        pers = StringVar()
        births = []
        #give name and age
        for person in info.months[rem_month].days[rem_day-1].day:
            births.append(str(person))
        bremove = ttk.OptionMenu(frame5,pers,births[0],*births)
        blabel = Label(frame5,text="Please, select birthday to remove:",fg=colour)
        blabel.grid(column=1, row=3)
        bremove.grid(column=1,row=4)
        submit.grid(column=3,row=4)
    else:
        #display error message and cancel button
        error = Label(frame5,text="No birthdays found",fg="red")
        error.grid(column=1,row=3,pady=5)
        stop.grid(column=3,row=3,pady=5)

#view sequence
def step1c():
    month_label = Label(frame5,text="Month",fg=colour)
    month_label.grid(row=1,column=1,padx=5,pady=0)
    global cmonth,months_arr
    cmonth = StringVar()
    #create list of months
    months_arr = []
    for month in months_array:
        months_arr.append(month.capitalize())
    #choose months
    month_menu = ttk.OptionMenu(frame5,cmonth,months_arr[Time.month],*months_arr)
    month_menu.grid(row=2,column=1,pady=5,padx=5)
    #confirm checkbutton
    global move1, month_tick
    move1 = IntVar()
    move1.set(0)
    month_tick = Checkbutton(frame5,variable=move1,command=check1c)
    month_tick.grid(row=2,column=2)
def check1c():
    #check the month
    if move1.get() == 1:
        for i,month in enumerate(months_arr):
            if month == cmonth.get():
                global rem_month
                #save the month as an integer
                rem_month = i
                step2c()
def step2c():
    day_label = Label(frame5,text="Day",fg=colour)
    day_label.grid(row=1,column=3,padx=5,pady=0)
    #disable month confirm
    month_tick.config(state="disabled")
    #stop editing month
    month_label = label(frame5,cmonth.get())
    month_label.grid(2,1,45,1)
    global cday,day_arr
    cday = IntVar()
    days_arr = []
    #days array
    for day in range(info.months[rem_month].length):
        days_arr.append(day+1)
    day_menu = ttk.OptionMenu(frame5,cday,days_arr[0],*days_arr[:info.months[rem_month].length])
    day_menu.grid(row=2,column=3,pady=5,padx=5)
    global move2, day_tick
    move2 = IntVar()
    move2.set(0)
    #day confirm checkbutton
    day_tick = Checkbutton(frame5,variable=move2,command=check2c)
    day_tick.grid(row=2,column=4)
def check2c():
    #check the day
    if move2.get() == 1:
        global rem_day
        #save day
        rem_day = cday.get()
        step3c()
def step3c():
    #disable day confirm
    day_tick.config(state="disabled")
    #stop editing day
    day_label = label(frame5,cday.get())
    day_label.grid(2,3,20,1)
    #finish button
    stop = Button(frame5,text="Done",command=lambda:f4and5(False),fg=colour)
    #list of birthdays on that day
    if len(info.months[rem_month].days[rem_day-1].day) > 0:
        #show name and age
        for i,person in enumerate(info.months[rem_month].days[rem_day-1].day):
            Label(frame5,text=str(person),fg=person.colour).grid(column=1,row=3+i)
        stop.grid(column=3,row=2+(len(info.months[rem_month].days[rem_day-1].day)),pady=5)
    else:
        #display error message and cancel button
        error = Label(frame5,text="No birthdays found",fg="red")
        error.grid(column=1,row=3,pady=5)
        stop.grid(column=3,row=3,pady=5)
#save birthday
def b_save(frame5,image,col,name,year,month,day,info):
    #create error message
    error2 = Label(frame5,text="Error, please select valid options",wraplength = 100,fg="red")
    if not((image.get() == "Flowers" or image.get() == "Cake" or image.get() == "Present" or image.get() == "Balloons") and col.get() in ["red","green","blue","brown","orange","purple","lime","cyan","maroon","indigo"] and len(name.get()) > 0):
        #if something is wrong, display error message
        error2.grid(column=3,row=7)
    else:
        #save birthday
        add_birthday(name.get(),year,month,day,image.get(),col.get(),info)
        #reset page
        reset()

#delete birthday
def delete(info):
    for i,per in enumerate(info.months[rem_month].days[rem_day-1].day):
        if str(per) == pers.get():
            del info.months[rem_month].days[rem_day-1].day[i]
    reset()

#create GUI
def start():
    #declare GUI
    global root,frame,frame1,frame2,frame3,frame4,frame5
    root = Tk()
    root.title("Birthday Reminder")
    
    #save images as variables
    global Flowers,Cake,Present,Balloons
    Flowers,Cake,Present,Balloons = image.get_images()
    
    #create frames
    frame = Frame(root)
    frame.grid(row=0,column=0)

    frame1 = Frame(frame)
    frame1.grid(row=0,column=0)

    frame2 = Frame(frame)
    frame2.grid(row=1,column=0)

    frame3 = Frame(frame)
    frame3.grid(row=2,column=0)

    #create a separator part way down
    ttk.Separator(frame,orient="horizontal").grid(row=3,column=0,padx=0,pady=(2,0),stick="EW")

    frame4 = Frame(frame)
    frame4.grid(row=4,column=0)

    frame5 = Frame(frame)
    frame5.grid(row=5,column=0)

    for wig in frame.winfo_children():
        #padding for all frames
        wig.grid(padx=10,pady=2)

    #frame functions
    f1(frame1,Time.day_name,Time.date,Time.month_name,Time.year,colour)
    f2(frame2,colour,info,Time.month)
    f3(frame3,day_length,colour,info,[Flowers,Cake,Present,Balloons])
    f4and5()

#get everything ready
start()

#save
save(January,February,March,April,May,June,July,August,September,October,November,December)
#reset
reset()
reset_time()

#run program
root.mainloop()

