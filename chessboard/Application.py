import tkinter as tk
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from Chess_pgn_player_class import Chess_pgn_player_class
from tkinter import *


class Application(tk.Frame):
    current_page = []

    def __init__(self,*args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        global frames
        self.frames = {}

        self.new_page(page_one)

    def new_page(self, page):
        for F in [page]:
            frame = F(self.container, self)

            Application.current_page = np.str(page)
            #print(self.page)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page].tkraise()


class page_one(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, master=parent)
        #self.parent = parent
        tk.Label(self, text="Introduction", font='Helvetica 18 bold').pack(pady=10, padx=10)
        ttk.Label(self, text="This is an introductory page of a tool used to visualize chess attacking patterns.\n"\
                             "The following pages contain a selection of different preselected games, and a runnable simulation...Enjoy!" \
                  ,justify=tk.CENTER, font=7).pack(pady=0, padx=10)
        #intro_text.insert(tk.INSERT, "Hello.....")
        ttk.Button(self, text="Visit Page 2", command=lambda: controller.new_page(page_two)).pack(pady=100, padx=10)
        #text_sample = ttk.Entry(self)
        #text_sample.insert(tk.INSERT, "Hello.....")
        #text_sample.pack()

class page_two(tk.Frame):

    text = []
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent)

        tk.Label(self, text="Choose PGN", font='Helvetica 18 bold').pack(pady=10, padx=10)
        ttk.Button(self, text="BEGIN SIMULATION", command = lambda: [self.pass_entry_text(),controller.new_page(page_three)]).pack(pady=0, padx=10)
        self.option = tk.StringVar(self)
        options = ["C:/Users/Lord Colm/Desktop/Chess_CNN/PGNs/December4.pgn", "C:/Users/Lord Colm/Desktop/Chess_CNN/PGNs/Adams.pgn","C:/Users/Lord Colm/Desktop/Chess_CNN/PGNs/Akobian.pgn"]
        ttk.OptionMenu(self, self.option, options[1], *options).pack(pady=10, padx=10)
        ttk.Button(self, text="Open Folders...", command = lambda: [self.load_file(),controller.new_page(page_three)]).pack(pady=0, padx=10)
        ttk.Button(self, text="Test Graph Page", command = lambda: [controller.new_page(options_page)]).pack(pady=0, padx=10)


    def load_file(self):
        file =  filedialog.askopenfilename(initialdir="/", title="Select file", \
                                               filetypes=(("PGN files", "*.pgn"), ("all files", "*.*")))
        page_two.text = np.str(file)
        Chess_pgn_player_class.PGN_str = page_two.text
        print("PGN Location:",page_two.text)


    def pass_entry_text(self):
        page_two.text = np.str(self.option.get())
        Chess_pgn_player_class.PGN_str = page_two.text
        print("PGN Location:",page_two.text)


class page_three(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent)
        tk.Label(self, text="Simulation", font='Helvetica 18 bold').pack(pady=10, padx=10)


class page_four(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent)
        ttk.Button(self, text="page one", command = lambda : controller.show_frame(page_one)).pack()


class Graph_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,master=parent)
        ttk.Button(self, text="Return", command = lambda: controller.show_frame(page_one))


class options_page(tk.Frame):
    def __init__(self, parent, controller ):
        tk.Frame.__init__(self, master=parent)

        global a
        global phase
        global scale
        global scale1
        global entry
        global scroll


        phase = tk.IntVar()
        a = tk.IntVar()
        a.set(1)

        scale = ttk.Scale(self, from_=0,to=10, value=1, variable=a,  command= lambda x: self.updategraph())
        scale.grid(column=5, row=0, columnspan=1, rowspan=1)
        scale1 = ttk.Scale(self,orient=tk.VERTICAL, from_=0,to=10, value=1, variable=phase,  command= lambda x: self.updategraph())
        scale1.grid(column=5, row=5, columnspan=2, rowspan=3)
        scroll = ttk.Scrollbar(self, command= lambda: self.updategraph())
        scroll.grid(column=5, row=1, columnspan=1, rowspan=4)
        separator = ttk.Separator(self, orient='vertical')
        separator.grid(column=5, row=0)
        global fig
        global figur
        global t
        fig = Figure(figsize=(5, 5), dpi=100)
        t = np.arange(0, 3, .01)
        figur=fig.add_subplot(111)
        figur.plot(t, a.get() * np.sin(2 * np.pi * t))
        global canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=5, rowspan=5)
        canvas._tkcanvas.grid(column=0, row=0, columnspan=5, rowspan=5)

    def updategraph(self):

        a.set(scale.get())
        print(a.get())
        phase.set(scale1.get())
        canvas.flush_events()
        figur.cla()
        figur.plot(phase.get()*t, a.get() * np.sin(2 * np.pi * t ))
        canvas.draw()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200",)
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
