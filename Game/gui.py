import tkinter as tk
from tkinter import *


def trainer_gui():
    root = tk.Tk()
    def write_attack():
        global val
        val = 0
        print("You are using an attack!")
        root.destroy()

    def write_object():
        global val
        val = 1
        print("What item do you want to use?")
        root.destroy()

    def write_change():
        global val
        val = 2
        print("What pokemon do you want to send?")
        root.destroy()

    def write_change():
        global val
        val = 3
        print("What pokemon do you want to send?")
        root.destroy()

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
    return val

def attack_gui(moveset: list):
    moveset += [''] * (4 - len(moveset))
    root = tk.Tk()
    def first_move():
        global val
        val = 0
        root.destroy()

    def second_move():
        global val
        val = 1
        root.destroy()

    def third_move():
        global val
        val = 2
        root.destroy()

    def fourth_move():
        global val
        val = 3
        root.destroy()
        
    frame = tk.Frame(root)
    frame.pack()

    attack = tk.Button(frame,
                    text=moveset[0],
                    width=25,
                    height=3,
                    command=first_move)
    attack.pack()
    change = tk.Button(frame,
                    text=moveset[1],
                    width=25,
                    height=3,
                    command=second_move)
    change.pack()
    items = tk.Button(frame,
                    text=moveset[2],
                    width=25,
                    height=3,
                    command=third_move)
    items.pack()

    run = tk.Button(frame,
                    text=moveset[3],
                    width=25,
                    height=3,
                    command=fourth_move)
    run.pack()
    root.mainloop()
    return val