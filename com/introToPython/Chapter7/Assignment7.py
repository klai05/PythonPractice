from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=1000, height=1000, bg="skyblue")
        self.myCanvas.grid()

        self.myCanvas.create_rectangle(0, 500, 1000, 1000, fill="green")
        # self.myCanvas.create_arc(100, 10, 1000, 1000, start=0, extent=180, fill="red")
        # self.myCanvas.create_arc(120, 30, 980, 980, start=0, extent=180, fill="orange")
        # self.myCanvas.create_arc(140, 50, 960, 960, start=0, extent=180, fill="yellow")
        # self.myCanvas.create_arc(160, 70, 940, 940, start=0, extent=180, fill="green2")
        # self.myCanvas.create_arc(180, 90, 920, 920, start=0, extent=180, fill="blue2")
        # self.myCanvas.create_arc(200, 110, 900, 900, start=0, extent=180, fill="skyblue")

        self.myCanvas.create_arc(100, 100, 900, 900, start=0, extent=180, fill="red")
        self.myCanvas.create_arc(120, 120, 880, 880, start=0, extent=180, fill="orange")
        self.myCanvas.create_arc(140, 140, 860, 860, start=0, extent=180, fill="yellow")
        self.myCanvas.create_arc(160, 160, 840, 840, start=0, extent=180, fill="green2")
        self.myCanvas.create_arc(180, 180, 820, 820, start=0, extent=180, fill="blue2")
        self.myCanvas.create_arc(200, 200, 800, 800, start=0, extent=180, fill="skyblue")

        my_circle_id = self.myCanvas.create_oval(120, 120, 140, 140, fill="orange")

        for count in range(10):
            increment = 10 * count
            self.myCanvas.coords(my_circle_id, 120 + increment, 120 - increment, 140 + increment, 140 - increment)
            self.myCanvas.update()
            sleep(1)


frame = MyFrame()
frame.mainloop()
