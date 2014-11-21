from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width = 500,height=500, background='grey')
drawpad.grid(row=0, column=1)

#create the shapes
Shape1square = drawpad.create_rectangle(0,500,50,450, outline='black', fill = 'yellow', width = 2)
Shape2Rectangle = drawpad.create_rectangle(475,500,500,400, outline = 'black', fill = 'DeepSkyBlue2', width = 2)

tpoints = [140, 350, 140, 375, 165, 375, 165,400, 190, 
    400, 190, 375, 215, 375, 215, 350]
drawpad.create_polygon(tpoints, outline='black', 
    fill='purple', width=2)
rlpoints = [355, 70, 355,170, 400, 170, 400, 
    145, 380,145, 380,70]
drawpad.create_polygon(rlpoints, outline='black', 
    fill='orange', width=2)
llpoints =[430, 305, 430, 330, 475, 330, 475, 230,
450, 230, 450, 305]
drawpad.create_polygon(llpoints, outline='black', 
    fill='dark blue', width=2)
lzpoints = [355, 375, 355, 400, 405, 400, 405, 375, 430, 375,
430, 350, 380, 350, 380, 375]
drawpad.create_polygon(lzpoints, outline='black', 
    fill='red', width=2)
rzpoints = [15, 45, 15, 70, 65, 70, 65, 45, 90, 45,
90, 20, 40, 20, 40, 45]
drawpad.create_polygon(rzpoints, outline='black', 
    fill='green', width=2)
root.mainloop()