#turn off key repeat for this program to work
import tkinter as tk
from gpiozero import Robot


#changing the sequence changes the rotation of wheels
robby = Robot(left=(7,8), right=(9,10)) #mapping the GPIO pins


def keyup(e): #key pressed function for tkinter
    key=e.keysym
    if key=='a' or key=='d':
        robby.forward()
    elif key=='w' or key=='s' or key=='n' or key =='m':
        robby.stop()
        
def keydown(e): #key pressed function for tkinter
    key=e.keysym
    if key=='w':
        robby.forward()
    elif key=='a':
        robby.left()
    elif key=='d':
        robby.right()
    elif key=='s':
        robby.backward()
    elif key=='n':
        robby.left()
    elif key=='m':
        robby.right()
    
        
root = tk.Tk()
frame = tk.Frame(root,width=100,height=100)
frame.bind("<KeyPress>",keydown)
frame.bind("<KeyRelease>",keyup)
frame.pack()
frame.focus_set()
    

root.mainloop()





