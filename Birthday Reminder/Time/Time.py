from Conversion import Days,Months
import time
class Time:
    def __init__(self):
        self.refresh()
    def refresh(self):
        #everything useful
        self.year = int(time.strftime("%Y"))
        self.month = int(time.strftime("%m"))-1
        self.month_name = time.strftime("%B").strip().title()
        self.date = int(time.strftime("%d"))
        self.day = Days.index(time.strftime("%A"))
        self.day_name = time.strftime("%A").strip().title()
        try:
            February.Feb()
        except:
            pass
