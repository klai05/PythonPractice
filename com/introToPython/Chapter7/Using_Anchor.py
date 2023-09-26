from tkinter import *

class MyFrame(Frame):
   def __init__(self):
      Frame.__init__(self)

      self.myCanvas = Canvas(width=150, height=150)

      self.myCanvas.create_line(50, 0, 50, 200)
      self.myCanvas.create_line(0, 50, 2000, 50)
      self.myCanvas.create_text(50, 50, text="Hi there!",
         anchor="se")

      self.myCanvas.grid()

frame02 = MyFrame()
frame02.mainloop()