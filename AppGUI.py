#author Timothy Lee
#last modified: 14/7/2016

from tkinter import *
import tkinter as tki

from Card import *
from CardGUI import *

class AppGUI():

        def __init__(self):
                self.root = tki.Tk()
                self.root.geometry('500x500')
                self.root.title("by. timlee95")

                RanMode = IntVar()
                
            # create a Frame for the Text and Scrollbar
                txt_frm = tki.Frame(self.root, width=250, height=250)
                txt_frm.pack(fill="both")
                # ensure a consistent GUI size
                txt_frm.grid_propagate(False)
                # implement stretchability
                txt_frm.grid_rowconfigure(0, weight=1)
                txt_frm.grid_columnconfigure(0, weight=1)

            # create a Text widget
                self.txtbox = tki.Text(txt_frm, borderwidth=3, relief="sunken")
                self.txtbox.config(font=("consolas", 12, "italic"), undo=True, wrap='word')
                self.txtbox.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
                self.txtbox.insert(END,'notes...')

            # create a Scrollbar and associate it with txt
                scrollb = tki.Scrollbar(txt_frm, command=self.txtbox.yview)
                scrollb.grid(row=0, column=1, sticky='nsew')
                self.txtbox['yscrollcommand'] = scrollb.set

            # create a Subject Text widget
                self.subbox = tki.Text(self.root,font=("consolas", 12,"italic"), height = 2,borderwidth=3, relief="sunken")
                self.subbox.insert(END,'subject...')
                self.subbox.pack(fill="x")

            # create a Button 
                self.Done = Button(self.root,text='done',font=("consolas", 16,"bold"),command=lambda:self.toCard())
                self.Done.pack(fil="x")
                    
        def toCard(self):
                Cards = []
                text = self.txtbox.get("1.0",END)
                lines = text.splitlines()
    
                CurrCard=None
                for i in range(len(lines)):
                    #Try/Except for blank lines
                        try:
                            #for First Topic
                                if lines[i][0] != "-" and CurrCard == None:
                                        CurrCard = Card(lines[i])
                            #for New Topic
                                elif lines[i][0] != "-" and CurrCard != None:
                                        Cards.append(CurrCard)
                                        CurrCard = Card(lines[i])
                            #for Definition
                                elif lines[i][0] == "-":
                                        try:
                                                CurrCard.definition += lines[i] + "\n"
                                        except AttributeError:
                                                pass
                                                
                        except IndexError:
                                pass
        #add last card
                Cards.append(CurrCard)               
                
                if Cards[0] is None:
                        return
                else:
                    #create Card GUI
                        C=CardGUI(self.subbox.get("1.0",END),Cards)
                        C.root.mainloop()
