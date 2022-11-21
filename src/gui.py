from tkinter import *
from tkinter import filedialog
import os
import tkinter.ttk as ttk

class GUI():
    def __init__(self):
        self.root = Tk()
        self.file_input = None
        self.file_on_leave = None
    
    def removeWidget(self, widget):
        widget.grid_forget()
        return

    def browseFile(self, file_name):
        if file_name == "chamcong":
            self.file_input = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("excel files", "*.xlsx *.xls"), ("all files", "*.*")))
            file_name = os.path.basename(self.file_input)
            widget = self.root.grid_slaves(row=0, column=1)[0]
            self.removeWidget(widget)
            Label(self.root, text=file_name).grid(row=0, column=1)
            Button(self.root, text="Choose files", command=lambda: self.browseFile("chamcong")).grid(row=0, column=2)
        elif file_name == "nghiphep":
            self.file_on_leave = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("excel files", "*.xlsx *.xls"), ("all files", "*.*")))
            file_name = os.path.basename(self.file_on_leave)
            widget = self.root.grid_slaves(row=1, column=1)[0]
            self.removeWidget(widget)
            Label(self.root, text=file_name).grid(row=1, column=1)
            Button(self.root, text="Choose files", command=lambda: self.browseFile("nghiphep")).grid(row=1, column=2)

    def show(self):
        self.root.title("Get Input Files")
        chamcongLabel = Label(self.root, text="File cham cong: ")
        nghiphepLabel = Label(self.root, text="File nghi phep: ")
        chamcongButton = Button(self.root, text="Choose files", command=lambda: self.browseFile("chamcong"))
        nghiphepButton = Button(self.root, text="Choose files", command=lambda: self.browseFile("nghiphep"))
        submitButton = Button(self.root, text="Submit", command=self.root.destroy)

        chamcongLabel.grid(row=0, column=0)
        nghiphepLabel.grid(row=1, column=0)

        chamcongButton.grid(row=0, column=1)
        nghiphepButton.grid(row=1, column=1)
        submitButton.grid(row=2, columnspan=2)

        self.root.mainloop()

    def getInputFiles(self):
        return self.file_input, self.file_on_leave