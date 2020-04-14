from PIL import ImageTk, Image

def get_images():
    #set up images
    Balloons = ImageTk.PhotoImage(Image.open("Images/Balloons.png"))
    Present = ImageTk.PhotoImage(Image.open("Images/Present.png"))
    Cake = ImageTk.PhotoImage(Image.open("Images/Cake.png"))
    Flowers = ImageTk.PhotoImage(Image.open("Images/Flowers.png"))
    return Balloons,Present,Cake,Flowers
