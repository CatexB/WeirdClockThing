from tkinter import *
import time

def tick():
    seconds_in_EST = time.time() - 21600 - 18000
    time_in_BP_hours = round(seconds_in_EST // 2880) % 30
    time_in_BP_minutes = round(seconds_in_EST // 28.80) % 100
    time_in_BP_seconds = round(seconds_in_EST // 2.88) % 10
    clock_text = time_in_BP_hours ,":", time_in_BP_minutes , ":", time_in_BP_seconds
    clock.config(text=clock_text)
    clock.after(200,tick)

root = Tk()
clock = Label(root, font = ("times", 100, "bold"), bg = "white")
clock.grid(row=0,column=1)
tick()
root.mainloop()
