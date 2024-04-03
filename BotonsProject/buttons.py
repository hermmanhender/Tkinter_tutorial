import tkinter as tk
from tkinter import ttk

def greet():
  print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", comand=greet)
greet_buttom.pack(side="left", fill="y", expand=True)

quit_buttom = ttk.Button(root, text"Quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()
