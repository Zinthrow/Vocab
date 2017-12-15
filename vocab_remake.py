# -*- coding: utf-8 -*-
"""
Vocabulary magoosh knock-off

Author: Alex Larsen

"""

import csv
import random
import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
        self.lvl = None

    def init_window(self):
        self.master.title("Vocabulary")
        self.grid()
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        file = tk.Menu(menu)
        file.add_command(label = 'Exit', command=self.client_exit)
        menu.add_cascade(label= 'File', menu=file)
        normal = tk.Menu(menu)
        normal.add_command(label = 'Level 1',command= lambda: self.initialize
                          ("lvl1normal.csv"))
        normal.add_command(label = 'level 2',command= lambda: self.initialize
                          ("lvl2normal.csv"))
        menu.add_cascade(label= 'Normal', menu= normal)
        hard = tk.Menu(menu)
        hard.add_command(label = 'Level 1',command= lambda: self.initialize
                          ("lvl1base.csv"))
        hard.add_command(label = 'level 2',command= lambda: self.initialize
                          ("lvl2base.csv"))
        hard.add_command(label = 'level 3',command= lambda: self.initialize
                          ("lvl3base.csv"))
        menu.add_cascade(label= 'Hard', menu=hard)

    def client_exit(self):
            root.destroy()
    
    def initialize(self, file):
        lvl = Level(file = file)
        self.lvl = lvl
        lvl.insert()
        self.test(lvl)
        
    def buttonmake(self, txt, backgrnd, com_option):
        if com_option != None:
            return tk.Button(self,text=txt,width=30,font =('bold', 15),
                             background=backgrnd,command= lambda: self.learned
                             (com_option))
        elif com_option == None:
            return tk.Button(self,text=txt,width=35,font =('bold', 15),
                             background=backgrnd)
        
    def populate(self):
        lvl = self.lvl
        lvl.clear('all')
        word = self.buttonmake(lvl.get_word('word'),"lightcyan",None)
        #tk.Button(self, text=lvl.get_word('word'), width = 35, font =
        #('bold', 15), background = "lightcyan")
        word.grid()
        definition = self.buttonmake(lvl.get_word('definition'),None, True)
        mock1 = self.buttonmake(lvl.get_word('mock1'),None, False)
        mock2 = self.buttonmake(lvl.get_word('mock2'),None, False)
        mock3 = self.buttonmake(lvl.get_word('mock3'),None, False)
        randbutton = [definition, mock1, mock2, mock3]
        randbutton = random.sample(randbutton, 4)
        for butn in randbutton:
            butn.grid()
    
        notsure = self.buttonmake(lvl.get_word('Not sure'),None, False)
        notsure.grid()
        self.counter()
        
    def counter(self):
        lvl = self.lvl
        complete = tk.Text(self, width=6, height = 1, font= "Helvetica 20")
        complete.tag_configure("center", justify="center")
        complete.grid(row = 8)
        complete_text = str(len(lvl.done))+str("/"+str(lvl.leng))
        complete.insert(tk.END, complete_text, "center")
        complete.config(state=tk.DISABLED)
        self.state()
        
    def state(self):
        lvl = self.lvl
        if lvl.newword in lvl.failed:
            tk.Label(self,text= "Working on it", height = 1,
                     font="Helvetica 15",background='pink').grid(row=7)
        elif lvl.newword in (lvl.review or lvl.review2):
            tk.Label(self,text= "Reviewing", height = 1,
                     font="Helvetica 15",background='lightyellow').grid(row=7)
        elif lvl.newword in lvl.done:
            tk.Label(self,text= "Learned!", height = 1,
                     font="Helvetica 15",background='lightgreen').grid(row=7)
        else:
            tk.Label(self,text= "New Word", height = 1,
                     font="Helvetica 15",background='gray').grid(row=7)
        
    def learned(self, option):
        lvl = self.lvl
        lvl.clear('mock')
        newword = lvl.newword
        review = lvl.review
        review2 = lvl.review
        failed = lvl.failed
        if option == True:
            revdef=self.buttonmake(lvl.get_word('definition'),'lightgreen',None)
            revdef.grid()
            if newword in failed:
                lvl.failed.remove(newword)
                lvl.review.append(newword)
            elif newword in review:
                lvl.review.remove(newword)
                lvl.review2.append(newword)
            elif newword in review2:
                lvl.review2.remove(newword)
                lvl.done.append(newword)
                lvl.terms.remove(newword)
            else:
                lvl.done.append(newword)
                lvl.terms.remove(newword)
        if option == False:
            revdef = self.buttonmake(lvl.get_word('definition'),'pink',None)
            revdef.grid()
            lvl.failed.append(newword)
            if newword in review:
                lvl.review.remove(newword)
            elif newword in review2:
                lvl.review2.remove(newword)
        if len(lvl.terms) != 0:    
            continu = tk.Button(self, text = "Continue", width = 30, font =
                                ('bold', 15),command=lambda: self.populate())
            continu.grid()
            tk.Label(self, height = 9).grid()
            self.counter()
            lvl.newword = random.SystemRandom().choice(lvl.terms)
            
            
        else:
            tk.Label(self,text= "well done", height = 9).grid()
            
    def test(self, lvl):
        lvl.newword = random.SystemRandom().choice(lvl.terms)
        self.populate()
        
class Term(object):
    def __init__(self):
        self.word = None
        self.definition = None
        self.mock1 = None
        self.mock2 = None
        self.mock3 = None
        self.unsure = 'Not Sure'

class Level(object):
    def __init__(self,file):
        self.file = file
        self.terms = []
        self.newword = None
        self.done = []
        self.review = []
        self.review2 = []
        self.failed = []
        self.leng = 0
        
    def insert(self):
        with open(self.file,'r') as csvfile:
            words = csv.reader(csvfile)
            words = list(words)
        self.leng = len(words)-1
        for learn in words[1:]:
            term = Term()
            term.word = learn[0]
            term.definition = learn[1]
            term.mock1 = learn[2]
            term.mock2 = learn[3]
            term.mock3 = learn[4]
            self.terms.append(term)
            
    def clear(self, option):
        if option == 'mock':
            for clrd in app.grid_slaves()[:-1]:
                try:
                    clrd.grid_forget()
                except NameError:
                    continue
        elif option == 'all':
            for clrd in app.grid_slaves():
                try:
                    clrd.grid_forget()
                except NameError:
                    continue

    def get_word(self, word_type):
        if word_type == 'word':
            return self.newword.word
        elif word_type == 'definition':
            return self.newword.definition
        elif word_type == 'mock1':
            return self.newword.mock1
        elif word_type == 'mock2':
            return self.newword.mock2
        elif word_type == 'mock3':
            return self.newword.mock3
        elif word_type == 'continue':
            return 'continue'
        else:
            return self.newword.unsure
                   
root = tk.Tk()
root.geometry("379x255")
app = Window(root)
root.mainloop()   
