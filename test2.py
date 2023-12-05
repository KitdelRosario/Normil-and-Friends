import tkinter as tk
from tkinter import ttk

def on_add_click():
    text = text_input.get()
    if text:
        array.append(text)
        text_input.delete(0, tk.END)
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for item in array:
        listbox.insert(tk.END, item)

# main
array = []

root = tk.Tk()
root.title("Item Appender")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

text_input = ttk.Entry(mainframe, width=30)
text_input.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))

add_button = ttk.Button(mainframe, text="Add Item", command=on_add_click)
add_button.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

listbox = tk.Listbox(mainframe, width=50)
listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()