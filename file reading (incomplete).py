import tkinter as tk
import time

import csv
import ast

class UI():
    #setup makes main window
    def __init__(self, main):
        self.main = main
        self.output = tk.Label(main, anchor = 'nw', justify = 'left')
        self.inpt =  tk.Text(main, height = 1)
        self.enterbut = tk.Button(main, text='Enter', background = 'light blue', height = 1, command = lambda:( self.enter(self.inpt,self.inpt.get('1.0','end')) ))
        self.text = ''

        self.situation = ["You stand in an empty room. There is a door ahead of you and a door behind you", ["Try north door", "Try south door", "Other"]]
    
   
        
        self.main.geometry("850x700")
        self.main.config(background ='#deface')

        #Big output text box. Disabled so cannot be typed in.
        #rel-x,y,height,width are relative placement for window
        self.output = tk.Label(main, anchor = 'nw', justify = 'left')
        self.output.place(relx =0.2, rely = 0.02, relheight=0.6, relwidth=0.6)

        #Input box
        #calls 'enter' on key press return/enter key
        
        self.inpt.bind("<Return>", lambda x: self.enter(self.inpt,self.inpt.get('1.0','end-1c')))
        self.inpt.place(relx =0.2, rely = 0.65,  relwidth=0.5)
        #enter is called with the .get() which takes from the ext box.
        # 1.0 is line.character, so line-1.position=0
        # end is end if text box, -1c is less 1 character (can be written as -1character)
        # 'end-1c' as oppose to 'end' ommits end \n from typed enter key



        #button that calls 'enter' same as above, save for not having the -1c after 'end' as no \n is typed (hope this makes sense)
        
        self.enterbut.place(relx = 0.71, rely = 0.645, relwidth = 0.09)


    #write fucntion takes text and the textbox it's from 
    def enter(self,inpt,txt):
        ###enter.input_entered = True
        self.txt = self.cleanInput(txt)
        self.cleanOutput()
        
        for i in txt:
            #Types to the end of textbox with value i
            self.text += i
            self.output.config(text = self.text)
            
            self.inpt.delete('end-2c','end-1c')
            #sleep for that cool typing effect
            time.sleep(0.05)
            #tkinter is shit
            self.main.update()
        #scrolls output to bottom (without its not possible to scroll at all, its odd)   
        #makes sure input is empt but is currently buggy not sure why, seems to automatically lead with a \n or ' ' weird ass shit

        jeremy.nextSitch(self.txt)
        self.inpt.delete('0.0','end')
        #disable output so cannot be typed in
        
           
    def write(self,txt):
        #global text
        self.txt = self.cleanInput(txt)
        self.cleanOutput()
        self.txt+='\n'
        self.inpt.config(state = 'disabled')
        for i in txt:
            self.text += i
            self.output.config(text = self.text)
            time.sleep(0.01)
            #tkinter is shit
            self.main.update()
        self.inpt.config(state = 'normal')
        

    def cleanOutput(self):
        #global text
        if self.text.count('\n')>25:
            cutof = self.text.index('\n')+1
            self.text = self.text[cutof:]

    def cleanInput(self,txt):
        n = 0
        for i in range(len(txt)):
            if txt[i] != '\n':
                n+=1
            else:
                n = 0
                
            if n > 80:
                n = 0
                txt = txt[:i] + '\n' + txt[i:]
        return(txt)

    def displayCurrent(self):
        
        self.write(self.situation[0])
        self.write('\nOptions:')
        for option in self.situation[1]:
            self.write('\n')
            self.write(option)
        self.write('\n')

    def getNewSitch(self, newSitch):
        print(newSitch)
        self.situation = newSitch
        jeremy.sitchOptions = self.situation[1]
        self.displayCurrent()

##UI.enter.input_entered = False
##UI.startup()
##
class Situation:
    def __init__(self, ID, desc, options, leadsTo, leadsFrom):
        self.desc = desc
        self.options = options
        #same as in situation handler
        self.ID = ID
        #probably going to be a bit clunky but I want to have it anyway
        self.leadsTo = leadsTo
        self.leadsFrom = leadsFrom

                    
class SituationHandler:
    def __init__(self):
        self.sitchOptions = ui.situation[1]

        self.sitches = []
        temp = []

        f = open("situations2.txt", "r")
        for row in f:
            row = row.strip()
            row = row.split("|")
            #because the arrays have commas in them.
            #yes it's ugly, no I won't change it
            row[2] = ast.literal_eval(row[2])
            row[3] = ast.literal_eval(row[3])
            row[4] = ast.literal_eval(row[4])
            #the arrays get made into strings so this de-strings em
            row = {row[0]:row[1:]}
            temp.append(row)
            print(row)
        f.close()
##        temp = f.read()
##        #temp = ast.literal_eval(temp)
##        print(temp)
##        f.close()

        #for item in temp:
            #self.sitches.append(Situation(item[0], item[1], item[2], item[3], item[4]))
            
    def nextSitch(self, argument):
        temp = argument.lower()
        temp = temp.strip()
        ui.write("\n")
        
        if temp == self.sitchOptions[0].lower():
            ui.getNewSitch(self.sitch0)
        elif temp == self.sitchOptions[1].lower():
            ui.getNewSitch(self.sitch1)
        elif temp == self.sitchOptions[2].lower():
            ui.getNewSitch(self.sitch2)
        else:
            ui.write("Invalid input.")
        ui.write("\n")

main = tk.Tk()
ui = UI(main)
UI.displayCurrent(ui)

jeremy = SituationHandler()
#main.mainloop()


#Bugs:
# 1) Weird leading space stuff
# 2) Can type \n with enter key when box is empty, tried to fix but tripped up by (1)
# 3) Can type shit when machine is displaying text with write(text,w)
