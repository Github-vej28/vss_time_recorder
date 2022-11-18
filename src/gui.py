from tkinter import *
import tkinter.ttk as ttk

# window = Tk()
# greeting = ttk.Label(text="Hello, Tkinter")
# label = Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black"  # Set the background color to black
# )
# button = Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# entry = Entry(window)
# greeting.pack()
# label.pack()
# button.pack()
# entry.pack()
# name = entry.get()
# entry.delete(0)
# entry.insert(0, "Python")
# window.mainloop()

# print(name)

root = Tk()

inputLabel = Label(root, text="Input")
start_date = Label(root, text="Start date: ")

inputLabel.grid(row=)
start_date.grid()

root.mainloop()