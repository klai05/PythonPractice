# import tkinter as tk
#
# root = tk.Tk()
# canvas = tk.Canvas(width=300, height=300, background="white")
# canvas.pack(fill="both", expand=True)
#
# canvas.create_line(150,0,150,300)
# canvas.create_line(0, 150, 300, 150)
#
# canvas.create_text(200, 100, anchor="e", text="Hello, world", fill="#000000")
#
# root.mainloop()



from tkinter import *

class myFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=150, height=150)

        self.myCanvas.create_line(50, 0, 50, 100)
        self.myCanvas.create_line(0, 50, 1000, 50)
        self.myCanvas.create_text(50, 50, text = "Hi there!",
                                  anchor="e", width=25, justify="center")
        self.myCanvas.grid()

frame02 = myFrame()
frame02.mainloop()