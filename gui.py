#%%
import tkinter as tk
from tkinter import *

def write_attack():
    print("You are using an attack!")

def write_object():
    print("What item do you want to use?")

def write_change():
    print("What pokemon do you want to send?")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

attack = tk.Button(frame, 
                   text="Attack", 
                   width=25,
                   height=3,
                   command=write_attack)
attack.pack()
change = tk.Button(frame,
                   text="Change",
                   width=25,
                   height=3,
                   command=write_change)
change.pack()
items = tk.Button(frame,
                   text="Items",
                   width=25,
                   height=3,
                   command=write_object)
items.pack()

run = tk.Button(frame,
                   text="Run",
                   width=25,
                   height=3,
                   command=quit)
run.pack()
root.mainloop()

# %%
