from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width = 500,height=500, background='grey')
drawpad.grid(row=0, column=1)
 
 #create the shapes

shape1Square = drawpad.create_rectangle(0,500,50,450, outline='black', fill = 'yellow', width = 2)
shape2Rectangle = drawpad.create_rectangle(475,500,500,400, outline = 'black', fill = 'DeepSkyBlue2', width = 2)
 
tpoints = [140, 350, 140, 375, 165, 375, 165, 400, 190, 
     400, 190, 375, 215, 375, 215, 350]

t = drawpad.create_polygon(tpoints, outline='black', 
    fill='purple', width=2)
rlpoints = [355, 95, 355,170, 400, 170, 400, 
    145, 380,145, 380,95]
rl = drawpad.create_polygon(rlpoints, outline='black', 
    fill='orange', width=2)
llpoints =[430, 305, 430, 330, 475, 330, 475, 255,
450, 255, 450, 305]
ll = drawpad.create_polygon(llpoints, outline='black', 
    fill='dark blue', width=2)
lzpoints = [355, 375, 355, 400, 405, 400, 405, 375, 430, 375,
430, 350, 380, 350, 380, 375]
lz = drawpad.create_polygon(lzpoints, outline='black', 
    fill='red', width=2)
rzpoints = [15, 45, 15, 70, 65, 70, 65, 45, 90, 45,
90, 20, 40, 20, 40, 45]
rz = drawpad.create_polygon(rzpoints, outline='black', 
    fill='green', width=2)

shapes = [t, rl, ll, lz, rz, shape1Square, shape2Rectangle]


drawpad.move(shape1Square,225,-400)
drawpad.move(shape2Rectangle,-300, -400)
drawpad.move(t,225,-350)
drawpad.move(rl,100,-70)
drawpad.move(ll,-125,-255)
drawpad.move(lz,-260,-350)
drawpad.move(rz,0, -20)

def animate():
    global direction
    # Gets Coordinates
   #Square
    x1, y1, x2, y2 = drawpad.coords(shape1Square)
    if y1 <1:
        drawpad.move(shape1Square,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
        direction = 0
    drawpad.move(shape1Square,0,direction)
    # Wait for 1 millisecond, then recursively call our animate function
    
    #Rectangle
    x1, y1, x2, y2 = drawpad.coords(shape2Rectangle)
    if y1 <1:
        drawpad.move(shape2Rectangle,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
       direction = 0
    drawpad.move(shape2Rectangle,0,direction)
   
    #The T
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = drawpad.coords(t)
    if y4 <1:
        drawpad.move(t,0,direction)
    if y4 < drawpad.winfo_height(): 
        direction = 1
    else:
        direction = 0
    #Move our oval object by the value of direction
    drawpad.move(t,0,direction)
    # Wait for 1 millisecond, then recursively call our animate function
  
    #Right L
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = drawpad.coords(rl)  
    if y2 <1:
        drawpad.move(rl,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
       direction = 0
    drawpad.move(rl,0,direction)
    
    #Left L
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = drawpad.coords(ll)  
    if y2 <1:
        drawpad.move(ll,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
       direction = 0
    drawpad.move(ll,0,direction)
    
    #Left zig zag
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = drawpad.coords(lz)  
    if y2 <1:
        drawpad.move(lz,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
       direction = 0
    drawpad.move(lz,0,direction)
    
    
    #Right zig zag
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = drawpad.coords(rz)  
    if y2 <1:
        drawpad.move(rz,0,direction)
    if y2 < drawpad.winfo_height(): 
        direction = 1
    else:
       direction = 0
    drawpad.move(rz,0,direction)
    drawpad.after(1, animate)
    
#Key movements 
def key(event):
    x1,y1,x2,y2 = drawpad.coords(shape1Square)
    global shape1Square
    if event.char =="s"and y2<500:
        drawpad.move(shape1Square,0,4)
    elif event.char =="a"and y2<500:
        drawpad.move(shape1Square,-4,0)
    elif event.char =="d"and y2<500:
        drawpad.move(shape1Square,4,0)
# Kick off our animation
root.bind_all('<Key>', key)
animate()
root.mainloop()