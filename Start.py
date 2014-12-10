from Tkinter import *
import random
root = Tk()


# Create the canvas widget
drawpad = Canvas(root, width = 500,height=500, background='grey')
drawpad.grid(row=0, column=1)

#create the shapes

currShape = ""


def CreateObj(t):
    global currShape
    if t == "t":
        tpoints = [140, 350, 140, 375, 165, 375, 165, 400, 190, 
        400, 190, 375, 215, 375, 215, 350]
        currShape = drawpad.create_polygon(tpoints, outline='black', 
            fill='purple', width=2)
        drawpad.move(currShape,225,-350)
        currShapeF = "t"
    elif t == "rl":
        rlpoints = [355, 95, 355,170, 400, 170, 400, 
            145, 380,145, 380,95]
        currShape = drawpad.create_polygon(rlpoints, outline='black', 
            fill='orange', width=2)
        drawpad.move(currShape,100,-70)
        currShapeF = "rl"
    elif t == "ll":
        llpoints =[430, 305, 430, 330, 475, 330, 475, 255,
            450, 255, 450, 305]
        currShape = drawpad.create_polygon(llpoints, outline='black', 
            fill='dark blue', width=2)
        drawpad.move(currShape,-125,-255)
        currShapeF = "ll"
    elif t == "lz":
        lzpoints = [355, 375, 355, 400, 405, 400, 405, 375, 430, 375,
            430, 350, 380, 350, 380, 375]
        currShape = drawpad.create_polygon(lzpoints, outline='black', 
            fill='red', width=2)
        drawpad.move(currShape,-260,-350)
        currShapeF = "lz"
    elif t == "rz":
        rzpoints = [15, 45, 15, 70, 65, 70, 65, 45, 90, 45,
            90, 20, 40, 20, 40, 45]
        currShape = drawpad.create_polygon(rzpoints, outline='black', 
            fill='green', width=2)
        drawpad.move(currShape,0, -20)
        currShapeF = "rz"
    elif t == "shape1Square":
        currShape = drawpad.create_rectangle(0,500,50,450, outline='black', fill = 'yellow', width = 2)
        drawpad.move(currShape,225,-400)
        currShapeF = "shape1Square"
    elif t == "shape2Rectangle":
        currShape = drawpad.create_rectangle(475,500,500,400, outline = 'black', fill = 'DeepSkyBlue2', width = 2)
        drawpad.move(currShape,-300, -400)
        currShapeF = "shape2Rectangle"
    else:
        return False


shapes = ['t', 'rl', 'll', 'lz', 'rz', 'shape1Square', 'shape2Rectangle']
currShapeF = ""
widths = {}
widths['t']=150
widths['rl']=100
widths['ll']=100
widths['lz']=150
widths['rz']=150
widths['shape1Square']=100
widths['shape2Rectangle']=50




#drawpad.move(shape1Square,225,-400)
#drawpad.move(shape2Rectangle,-300, -400)
#drawpad.move(t,225,-350)
#drawpad.move(rl,100,-70)
#drawpad.move(ll,-125,-255)
#drawpad.move(lz,-260,-350)
#drawpad.move(rz,0, -20)


def animate():
    global direction
    global currShape
    # Gets Coordinates of currShape
    if currShape != "":
        l = list(drawpad.coords(currShape))
        print l
        if l[3] <1:
            drawpad.move(currShape,0,direction)
        if l[3] < drawpad.winfo_height(): 
            direction = 1
        else:
            direction = 0
            currShape = ""
        drawpad.move(currShape,0,direction)
    # Wait for 1 millisecond, then recursively call our animate function
    else:
        CreateObj(random.choice(shapes))
    drawpad.after(1, animate)

#Key movements 
def key(event):
    print 'key'
    global drawpad
    vals = list(drawpad.coords(currShape))
    print vals
    global currShape
    if event.char =="s" and vals[0]>50:
        drawpad.move(currShape,0,50)
    elif event.char =="a" and vals[2]>50:
        drawpad.move(currShape,-50,0)
    elif event.char =="d" and vals[0]>50:
        drawpad.move(currShape,50,0)
# Kick off our animation
root.bind_all('<Key>', key)
#CreateObj(random.choice(shapes))
animate()
root.mainloop()