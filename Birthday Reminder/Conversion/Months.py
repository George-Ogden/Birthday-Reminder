#array of months
array = ["january","february","march","april","may","june","july","august","september","october","november","december"]
#convert months to int or vice versa
def index(mon):
    #check whether to go str -> int or int -> str
    if isinstance(inp,str):
        mon = mon.strip().lower()
        #loop through months to find location in array
        for i,month in enumerate(months_array):
            #return correct position
            if month == inp:
                return i
    elif isinstance(inp,int):
        #find month at point in array
        month = months_array[inp]
        return month

