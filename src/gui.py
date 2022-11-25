import tkinter.filedialog as filedialog
import os
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class GUI():
    def __init__(self):
        self.root = Tk()
        self.top_frame = Frame(self.root)
        self.middle_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)
        self.file_input = None
        self.file_on_leave = None
        self.file_output = None
        self.cur_dir = "/"

    def browseTimekeeper(self, frame):
        self.file_input = filedialog.askopenfilename(initialdir=self.cur_dir, title="Select file", filetypes=(("excel files", "*.xlsx *.xls"), ("all files", "*.*")))
        for wid in frame.winfo_children():
            if type(wid) == ttk.Entry:
                wid.delete(0, END)
                wid.insert(0, self.file_input)
        self.cur_dir = os.path.dirname(self.file_input)

    def browseOnLeaveFile(self, frame):
        self.file_on_leave = filedialog.askopenfilename(initialdir=self.cur_dir, title="Select file", filetypes=(("excel files", "*.xlsx *.xls"), ("all files", "*.*")))
        for wid in frame.winfo_children():
            if type(wid) == ttk.Entry:
                wid.delete(0, END)
                wid.insert(0, self.file_on_leave)
        self.cur_dir = os.path.dirname(self.file_on_leave)

    def browseOutputFile(self, frame):
        self.file_output = filedialog.askopenfilename(initialdir=self.cur_dir, title="Select file", filetypes=(("excel files", "*.xlsx *.xls"), ("all files", "*.*")))
        for wid in frame.winfo_children():
            if type(wid) == ttk.Entry:
                wid.delete(0, END)
                wid.insert(0, self.file_output)
        self.cur_dir = os.path.dirname(self.file_output)

    def begin(self):
        for wid in self.root.winfo_children():
            wid.destroy()

        if (self.file_input != None) and (self.file_on_leave != None) and (self.file_output != None):
            self.showMessage(2)
        else:
            self.showMessage(1)
        return

    def show(self):
        self.root.title("Timekeeping machine program")
        
        line1 = Frame(self.root, height=1, width=400, bg="grey80", relief='groove')
        line2 = Frame(self.root, height=1, width=400, bg="grey80", relief='groove')

        chamcong_path = Label(self.top_frame, text="Cham cong File Path:")
        chamcong_entry = ttk.Entry(self.top_frame, text="", width=50)
        browse1 = ttk.Button(self.top_frame, text="Browse", command=lambda: self.browseTimekeeper(self.top_frame))

        nghiphep_path = Label(self.middle_frame, text="Nghi phep File Path:")
        nghiphep_entry = ttk.Entry(self.middle_frame, text="", width=50)
        browse2 = ttk.Button(self.middle_frame, text="Browse", command=lambda: self.browseOnLeaveFile(self.middle_frame))

        output_path = Label(self.bottom_frame, text="Output File Path:")
        output_entry = ttk.Entry(self.bottom_frame, text="", width=50)
        browse3 = ttk.Button(self.bottom_frame, text="Browse", command=lambda: self.browseOutputFile(self.bottom_frame))

        begin_button = ttk.Button(self.bottom_frame, text='Begin!', command=self.begin)
        
        self.top_frame.pack(side=TOP)
        line1.pack(pady=10)
        self.middle_frame.pack(side=TOP)
        line2.pack(pady=10)
        self.bottom_frame.pack(side=BOTTOM)

        chamcong_path.pack(pady=5)
        chamcong_entry.pack(pady=5)
        browse1.pack(pady=5)

        nghiphep_path.pack(pady=5)
        nghiphep_entry.pack(pady=5)
        browse2.pack(pady=5)

        output_path.pack(pady=5)
        output_entry.pack(pady=5)
        browse3.pack(pady=5)

        begin_button.pack(pady=20, fill=X)
        self.root.mainloop()

    def getFiles(self):
        return self.file_input, self.file_on_leave, self.file_output

    def showMessage(self, state):
        self.root.title("Message")
        if state == 1:
            my_img = ImageTk.PhotoImage(Image.open("images/fail.jpg"))
            label = Label(self.root, text="Failed!", fg="#FF3800", font=("Arial", 25))
        elif state == 2:
            my_img = ImageTk.PhotoImage(Image.open("images/success.png"))
            label = Label(self.root, text="Success!", fg="#32CD32", font=("Arial", 25))
        messageLabel = Label(image=my_img)
        messageLabel.pack()
        label.pack()
        self.root.mainloop()
