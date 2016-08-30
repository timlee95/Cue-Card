#author Timothy Lee
#last modified: 14/7/2016

from tkinter import *
import tkinter as tki

from Card import *

class CardGUI():
        def __init__(self,Subject,ListofCards):

                #init cards
                self.CardList = ListofCards
                self.CurrCard = -1

                #setup window                
                self.root = tki.Tk()
                self.root.geometry('1000x500')
                self.root.title(Subject)

                #setup window widgets
                self.CardText = Label(self.root,text="Start",fg="black",font=("consolas", 24))
                
                self.Next = Button(self.root,text='>',command=self.displayNextTopic,font=("consolas", 16, "bold"))
                self.Previous = Button(self.root,text='<',command=self.displayPreviousTopic,font=("consolas", 16, "bold"))
                self.Show = Button(self.root,text='show',command=self.displayDefinition,font=("consolas", 16, "bold"))

                #place widgets
                self.Next.pack(side=RIGHT,fill='y')
                self.Previous.pack(side=LEFT,fill='y')
                self.Show.pack(side=BOTTOM)
            

                txt_frm = tki.Frame(self.root, width=200, height=200)
                txt_frm.pack(side=TOP)
                
                self.CardText.pack()
                
        #display the next card
        def displayNextTopic(self):
                self.CurrCard += 1

                #end of deck
                if self.CurrCard >= len(self.CardList):
                        self.CurrCard = len(self.CardList)
                        self.CardText.config(fg="black")
                        self.CardText['text']="Out of Cards..."
                else:
                        self.CardText.config(fg="red")
                        self.CardText['text']=self.CardList[self.CurrCard].topic
                        
                        
        #display the previous card
        def displayPreviousTopic(self):
                self.CurrCard -= 1
                if self.CurrCard <= -1:
                        self.CurrCard = -1
                        self.CardText.config(fg="black")
                        self.CardText['text']="Start"
                else:
                        self.CardText.config(fg="red")
                        self.CardText['text']=self.CardList[self.CurrCard].topic

        #display the definition
        def displayDefinition(self):
                if self.CurrCard == -1 or self.CurrCard >= len(self.CardList):
                        return
                else:
                        self.CardText.config(fg="blue")
                        self.CardText['text']= self.CardList[self.CurrCard].definition
                
