# -*- coding: utf-8 -*-
"""
Vocabulary magoosh knock-off

Author: Alex Larsen

"""

import csv
import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Vocabulary")
        self.grid()
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        file = tk.Menu(menu)
        file.add_command(label = 'Exit', command=self.client_exit)
        menu.add_cascade(label= 'File', menu=file)
        level = tk.Menu(menu)
        level.add_command(label = 'Level 1',command=Level(file="lvl1base.csv"))
        level.add_command(label = 'level 2',command=Level(file="lvl2base.csv"))
        menu.add_cascade(label= 'Level', menu=level)

    def client_exit(self):
            root.destroy()

class Level(object):
    def __init__(self,file):
        self.file = file
        self.terms = []
        self.newword1 = 0
        self.done = [0]
        self.review = [0]
        self.review_2 = [0]
        self.failed = [0]
        self.leng = 0
        
    def insert(self):
        with open(self.file,'r') as csvfile:
            words = csv.reader(csvfile)
            words = list(words)
        self.leng = len(words[0])-1
        for learn in words[1:]:
            term = Term()
            term.word = learn[0]
            term.definition = learn[1]
            term.mock1 = learn[2]
            term.mock2 = learn[3]
            term.mock3 = learn[4]
            self.terms.append(term)
            
    def clear():
            for clrd in app.grid_slaves():
                try:
                    clrd.grid_forget()
                except NameError:
                    continue
            
    def test(self):
        
            
class Term(object):
    def __init__(self):
        self.word = None
        self.definition = None
        self.mock1 = None
        self.mock2 = None
        self.mock3 = None
        self.unsure = 'Not Sure'

        
root = tk.Tk()
root.geometry("379x220")
app = Window(root)
root.mainloop()   
