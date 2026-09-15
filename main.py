#imports
import tkinter as tk
from functions import *

#window
root = tk.Tk()
root.title("Make Money")

Moneylabel = tk.Label(root, text= "Money: 0$")
Moneylabel.pack(pady=10)

EarnButton = tk.Button(root, text="Earn", command=lambda: earn(Moneylabel))
EarnButton.pack(pady=10)

root.mainloop()