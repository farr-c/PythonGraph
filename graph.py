import math 
import time 
import tkinter as tk
import random

# this is a test change

window = tk.Tk()
window.geometry("600x600") 
window.title("Sin Over Time")
e = tk.Entry(window)
e.pack()
e.focus_set()

speed = .01
increase = 10 
x = 0
elements = []
while True:
    x += 1
    if len(e.get()) > 0:
        increase = e.get()
    window.update()
    y = (math.sin(math.radians(x*float(increase))))
    time.sleep(float(speed)) 
    ypos = x*15
    pos = 291 + (y *290)
    ct = [x % 255, 100,100] 
    print(ct)
    ct_hex = "%02x%02x%02x" % tuple(ct) # from https://www.python-co urse.eu/
    main = tk.Label(bg="#" + ct_hex)

    if ypos >= 560:
        ypos = 560
        elements[0][0].destroy()
        del elements[0]
        c = 0
        for v in (elements):
            c+=1
            if tk.Label.winfo_exists(v[0]):
                v[2] -= 15
                v[0].place(x = v[1],y = v[2] , width=15, height=15)
        
    main.place(x = pos,y = ypos , width=15, height=15)
    elements.append([main, pos, ypos])
         





