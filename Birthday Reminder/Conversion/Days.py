#array of days
days_array = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
#convert days to int or vice versa
def index(inp):
    #check whether to go str -> int or int -> str
    if isinstance(inp,str):
        inp = inp.strip().lower()
        #loop through days to find location in array
        for i,day in enumerate(days_array):
            #return correct position
            if day == inp:
                return i
    elif isinstance(inp,int):
        #find month at point in array
        day = days_array[inp]
        return day
