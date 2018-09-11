from Time import Time
import random
import pickle

Time = Time.Time()

#birthday
class birthday:
    #relevant information
    def __init__(self,name,year,month,date,image,colour):
        self.name = name
        self.year = year
        self.month = month
        self.date = date
        self.image = image
        self.colour = colour
        self.age = int(Time.year) - self.year - birthday.passed(self)
        self.dict = {"name":self.name,"image":self.image,"age":self.age,"colour":self.colour}
        #check is a birthday has passed
    def passed(self):
        #check month has passed
        if Time.month < self.month:
            return 1
        #check day has passed
        elif Time.month == self.month:
            if Time.date < self.date:
                return 1
            else:
                return 0
        else:
            return 0
        #results are inverted
    def __str__(self):
        return "{name} ({year})".format(**self.__dict__) #str(birthday) function

#day
class day:
    def __init__(self):
        #create an array to store birthdays
        self.day = []
    def add_birthday(self,birth):
        #add birthday object to day
        if isinstance(birth,birthday):
            self.day.append(birth)

#month
class month:
    def __init__(self,days):
        #array of days and length of month
        self.days = []
        self.length = days
        for i in range(days):
            self.days.append(day())
    def get_dates(self,i,year):
        #get first date and colour
        self.date = Time.date - Time.day + i
        if self.date < 1:
            #if the date < 1, it is in the previous month
            self.x = year.months[Time.month-1].length + self.date
            if len(year.months[Time.month-1].days[self.x-1].day)>0:
                self.colour1 = random.choice(year.months[Time.month-1].days[self.x-1].day).colour
            else:
                self.colour1 = "black"
        elif self.date > self.length:
            #if the date > length of month, it is in the next month
            self.x = self.date % self.length
            if len(year.months[Time.month+1].days[self.x-1].day)>0:
                self.colour1 = random.choice(year.months[Time.month+1].days[self.x-1].day).colour
            else:
                self.colour1 = "black"
        else:
            #current month
            self.x = self.date
            if len(self.days[self.date-1].day)>0:
                self.colour1 = random.choice(self.days[self.x-1].day).colour
            else:
                self.colour1 = "black"
        #get second date and colour
        self.date = (Time.date - Time.day + i + 7)
        if self.date > self.length:
            #if the date > length of month, it is in the next month
            self.y = self.date % self.length
            if len(year.months[Time.month+1].days[self.y-1].day)>0:
                self.colour2 = random.choice(year.months[Time.month+1].days[self.y-1].day).colour
            else:
                self.colour2 = "black"
        else:
            #current month
            self.y = self.date
            if len(self.days[self.y-1].day)>0:
                self.colour2 = random.choice(self.days[self.y-1].day).colour
            else:
                self.colour2 = "black"
        #return colour and dates
        return self.x,self.y,self.colour1,self.colour2
    def get_future(self,year):
        birthdays = []
        for i in range(0,14):
            #find date
            self.date = Time.date + i
            if self.date > self.length:
                #if the date > length of month, it is in the next month
                self.x = self.date % self.length
                for birth in year.months[Time.month+1].days[self.x-1].day:
                    birthdays.append(birth)
            else:
                #current month
                for birth in self.days[self.date-1].day:
                    birthdays.append(birth)
        return birthdays #return list of birthdays
            
    
    def day_len(self,year):
    #work out if it is a leap year
        if year % 4 != 0:
            return 28
        else:
            #special cases of months divisible by 4
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
    def Feb():
        #set length of Feb if required later
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

#get months
def load():
    try:
        #try to access months
        Jan = pickle.load(open("Months/January",'rb'))
        Feb = pickle.load(open("Months/February",'rb'))
        Mar = pickle.load(open("Months/March",'rb'))
        Apr = pickle.load(open("Months/April",'rb'))
        May = pickle.load(open("Months/May",'rb'))
        Jun = pickle.load(open("Months/June",'rb'))
        Jul = pickle.load(open("Months/July",'rb'))
        Aug = pickle.load(open("Months/August",'rb'))
        Sep = pickle.load(open("Months/September",'rb'))
        Oct = pickle.load(open("Months/October",'rb'))
        Nov = pickle.load(open("Months/November",'rb'))
        Dec = pickle.load(open("Months/December",'rb'))
    except:
        #if error or months are reset, create new ones
        print("ERROR LOADING FILES: ALL MONTHS RESET")
        Jan = month(31)
        Feb = month(29)
        Mar = month(31)
        Apr = month(30)
        May = month(31)
        Jun = month(30)
        Jul = month(31)
        Aug = month(31)
        Sep = month(30)
        Oct = month(31)
        Nov = month(30)
        Dec = month(31)
    return Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
