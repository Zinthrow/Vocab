# -*- coding: utf-8 -*-
"""
Vocabulary magoosh knock-off

Author: Alex Larsen

"""
import csv
import random
from tkinter import *
import time
#import os
#import sys




vocab1 = "lvl1base.csv"
vocab2 = "lvl2base.csv"

def lvla(file):
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        reader = list(reader)
        for row in reader:
            return len(row) - 1

a = lvla(vocab1)


global newword1
global review12
global review1
global done1
global failed1
'''
newword1 = 0

done1 = [0,1,2,3,4,5,6,7,8,10]
review1 = [0]
review12 = [0]
failed1 = [0]
'''

class Window(Frame):


    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.grid()
        self.init_window()


    def init_window(self):

        self.master.title("Vocabulary")

        self.grid()

        menu = Menu(self.master)

        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = 'Exit', command=self.client_exit)
        menu.add_cascade(label= 'File', menu=file)

        level = Menu(menu)
        level.add_command(label = 'Level 1', command=level1(self,vocab1))
        level.add_command(label = 'level 2', command=level1(self,vocab2))
        menu.add_cascade(label= 'Level', menu=level)




    def client_exit(self):
            root.destroy()


class level1(self, vocab):

    with open(vocab,'r') as csvfile:
        reader = csv.reader(csvfile)
        reader = list(reader)

    def lvla(file):
        with open(file,'r') as csvfile:
            reader = csv.reader(csvfile)
            reader = list(reader)
            for row in reader:
                return len(row) - 1

    a = lvla(vocab1)

    def __init__(self):

        self.newword1 = 0

        self.done1 = [0]
        self.review1 = [0]
        self.review12 = [0]
        self.failed1 = [0]


    def donesort():
        global done1
        done1 = sorted(done1)


    def lvlcomplete(): #cleans up widgets and sorts done1 to see if program done
        donesort()
        global done1
        if done1 == list(range(a+1)):
            done1 = [0]
            cleer()
            stats = Text(self, width=30, height = 1, font= "Helvetica 20")
            stats.grid()
            stats.insert(END,"Nyce mate")
            raise NameError
            #timer
        else:
            None

    def cleer():

        for clrd in app.grid_slaves():
            try:
                clrd.grid_forget()
            except NameError:
                continue





    def clmock():
        definition.grid_forget()
        mock1.grid_forget()
        mock2.grid_forget()
        mock3.grid_forget()
        notsure.grid_forget()


    def must_learn():
        clmock()
        global newword1
        global review12
        global review1
        global done1
        global failed1

        revdef = Button(self, text = reader[1][chooseword()],width = 30, font =('serif', 15), background = "pink")
        revdef.grid()

        failed1.append(newword1)
        if newword1 in review1:
            review1.remove(newword1)
        elif newword1 in review12:
            review12.remove(newword1)

        continu = Button(self, text = "Continue", width = 30, font =('bold', 15), command= self.level1)
        continu.grid()

        newword1 = random.randint(1,a)


    def chooseword():
        global newword1
        while newword1 in done1:
            newword1 = random.randint(1,a)
        return newword1


    def teste():
        print (newword1)
        print (done1)
        print (failed1)
        print (review1)
        print (review12)


    def learned():
        clmock()
        global newword1
        global review12
        global review1
        global done1
        global failed1

        revdef = Button(self, text = reader[1][chooseword()],width = 30, font =('serif', 15), background = "lightgreen")
        revdef.grid()

        if newword1 in failed1:
            failed1.remove(newword1)
            review1.append(newword1)
        elif newword1 in review1:
            review1.remove(newword1)
            review12.append(newword1)
        elif newword1 in review12:
            review12.remove(newword1)
            done1.append(newword1)
        else:
            done1.append(newword1)


        continu = Button(self, text = "Continue", width = 30, font =('bold', 15), command= self.level1)
        continu.grid()

        newword1 = random.randint(1,a)

#--------------------------------------------------------------------------------------------------------------------
    lvlcomplete()
    cleer()
    teste()

    word = Button(self, text = reader[0][chooseword()], width = 35, font =('bold', 15), background = "lightcyan")
    word.grid()

    #defines buttons with definiton and randomizes them
    definition = Button(self, text = reader[1][chooseword()],width = 30, font =('serif', 15), command=learned)
    mock1 = Button(self, text = reader[2][chooseword()],width = 30, font =('serif', 15), command=must_learn)
    mock2 = Button(self, text = reader[3][chooseword()],width = 30, font =('serif', 15), command=must_learn)
    mock3 = Button(self, text = reader[4][chooseword()],width = 30, font =('serif', 15), command=must_learn)
    randbutton = [definition, mock1, mock2, mock3]
    randbutton = random.sample(randbutton, 4)
    for butn in randbutton: #randomly prints buttons for difficulty
        butn.grid()

    notsure = Button(self, text = reader[5][2],width = 30, font =('serif', 15), command=must_learn)
    notsure.grid()


    teste()



    print ("")
    print ("")

    lvlcomplete()
root = Tk()

root.geometry("379x220")

app = Window(root)



root.mainloop()