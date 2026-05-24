#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk


root = tk.Tk()
root.geometry("300x300")

frame1 = tk.Frame(root, width=200, height=150, background="Blue")
frame1.grid(row=0, column=0)

frame2 = tk.Frame(root, width=200, height=150, background="Red")
frame2.grid(row=1, column=0)

frame3 = tk.Frame(root, width=100, height=150, background="Green")
frame3.grid(row=0, column=1)

frame4 = tk.Frame(root, width=100, height=150, background="Yellow")
frame4.grid(row=1, column=1)

root.mainloop()