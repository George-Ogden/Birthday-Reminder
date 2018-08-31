#GUI
from tkinter import *
from tkinter import ttk
import pickle
from time_periods import birthday

#clear func
def clear(frame):
    if isinstance(frame,Frame):
        #clear frame
        for wig in frame.winfo_children():
            wig.grid_remove()
    else:
        for f in frame:
            #clear frame
            for wig in f.winfo_children():
                wig.grid_remove()

def save(January,February,March,April,May,June,July,August,September,October,November,December):
    #save files to folder
    pickle.dump(January,open("Months/January","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(February,open("Months/February","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(March,open("Months/March","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(April,open("Months/April","wb"),pickle.HIGHEST_PROTOCOL )
    pickle.dump(May,open("Months/May","wb"),pickle.HIGHEST_PROTOCOL )
    pickle.dump(June,open("Months/June","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(July,open("Months/July","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(August,open("Months/August","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(September,open("Months/September","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(October,open("Months/October","wb"),pickle.HIGHEST_PROTOCOL )
    pickle.dump(November,open("Months/November","wb"),pickle.HIGHEST_PROTOCOL)
    pickle.dump(December,open("Months/December","wb"),pickle.HIGHEST_PROTOCOL)

#frame 1
def f1(frame1,day,tdate,month,year,color):
    #clear frame
    clear(frame1)
        
    #date at to
    date = StringVar()
    date.set("{} {} {} {}".format(day,tdate,month,year))
    date_label = Label(frame1,text=date.get(),fg=color)
    date_label.grid(row=1,column=1,padx=10,pady=5)
    #separators
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=0,padx=(0,150),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
    ttk.Separator(frame1,orient="vertical").grid(row=0,column=2,padx=(150,0),pady=0,stick="NS",rowspan=3)
    ttk.Separator(frame1,orient="horizontal").grid(row=3,column=0,columnspan=3,padx=0,pady=0,stick="EW")

#frame 2
def f2(frame2,colour,year,month):
    clear(frame2)
        
    #days of the week at top
    Mon = Label(frame2,text="M")
    Tue = Label(frame2,text="T")
    Wed = Label(frame2,text="W")
    Thu = Label(frame2,text="T")
    Fri = Label(frame2,text="F")
    Sat = Label(frame2,text="S")
    Sun = Label(frame2,text="S")
    day_widgets = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]
    #dates for current week and following week
    for i,wig in enumerate(day_widgets):
        wig.config(fg=colour)
        wig.grid(row=1,column=2*i+1,padx=10,pady=5)
        week1 = IntVar()
        week2 = IntVar()
        #get the colours and numbers
        week1,week2,c1,c2 = year.months[month].get_dates(i,year)
        Label(frame2,text=week1,fg=c1).grid(row=3,column=2*i+1,padx=10,pady=5)
        Label(frame2,text=week2,fg=c2).grid(row=5,column=2*i+1,padx=15,pady=5)
        #separators
        ttk.Separator(frame2,orient="vertical").grid(row=1,column=2*i,padx=5,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="vertical").grid(row=1,column=15,padx=0,pady=0,stick="NS",rowspan=7)
    ttk.Separator(frame2,orient="horizontal").grid(row=0,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=2,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=4,column=0,columnspan=16,padx=3,pady=0,stick="EW")
    ttk.Separator(frame2,orient="horizontal").grid(row=6,column=0,columnspan=16,padx=3,pady=0,stick="EW")

def f3(frame3,day_length,colour,info,image):
    clear(frame3)
        
    #happy birthday
    if day_length > 0:
        #initial separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        
        for i,person in enumerate(info.today.day):
            #text
            name_label = Label(frame3,text="{name} is {age} years old today".format(**person.dict),fg=person.colour)
            #find image
            if person.image == "Flowers":
                cimage = image[0]
            elif person.image == "Cake":
                cimage = image[1]
            elif person.image == "Present":
                cimage = image[2]
            elif person.image == "Balloons":
                cimage = image[3]
            #display image and text
            image_label = Label(frame3,image=cimage)
            name_label.grid(row=1,column=2*i+1,padx=10,pady=5)
            image_label.grid(row=2,column=2*i+1,padx=5,pady=5)
            #separators
            ttk.Separator(frame3,orient="vertical").grid(row=0,column=2*(i+1),padx=0,pady=0,stick="NS",rowspan=4)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=3,column=0,columnspan=day_length*2+1,padx=0,pady=0,stick="EW")
    else:
        #label without birthday
        none = Label(frame3,text="No birthdays saved today!",fg=colour)
        none.grid(row=1,column=1,padx=100,pady=(50,100))

        #separators
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=0,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="vertical").grid(row=0,column=2,padx=0,pady=0,stick="NS",rowspan=3)
        ttk.Separator(frame3,orient="horizontal").grid(row=0,column=0,columnspan=3,padx=0,pady=0,stick="EW")
        ttk.Separator(frame3,orient="horizontal").grid(row=2,column=0,columnspan=3,padx=0,pady=0,stick="EW")

#add birthday
def add_birthday(name,year,month,date,image,colour,info):
    info.months[month].days[date-1].add_birthday(birthday(name,year,month,date,image,colour))
