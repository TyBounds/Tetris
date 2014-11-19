from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width = 500,height=500, background='white')
drawpad.grid(row=0, column=1)
#create the shapes
Shape1square = drawpad.create_rectangle(0,500,50,450, outline='black', fill = 'blue', width = 2)
Shape2Rectangle = drawpad.create_rectangle(480,500,500,450, fill = 'DeepSkyBlue2')

points = [150, 100, 200, 120, 240, 180, 210, 
    200, 150, 150, 100, 200]
drawpad.create_polygon(points, outline='red', 
    fill='green', width=2)





root.mainloop()