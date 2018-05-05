import tkinter as tk
import time
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
            time.sleep(0.05)
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
        self.displayCurrent()

##UI.enter.input_entered = False
##UI.startup()
##
class SituationHandler:
    def __init__(self):
        self.sitch1 = ["You sit down. The floor is smooth and cold, with the texture and colour of marble.", ["Stand Up", "Sleep"]]
        self.sitch2 = ["You try the north door. It is locked and will not budge.", ["Back to middle of room", "break it down"]]
        self.sitch3 = ["You try the south door. It slides open, accompanied by the hiss of pressurized gas.", ["Try other door", "Enter"]]
        
    def nextSitch(self, argument):
        temp = argument.lower()
        temp = temp.strip()
        ui.write("\n")
        
        if temp == "other":
            ui.getNewSitch(self.sitch1)
        elif temp == "try north door":
            ui.getNewSitch(self.sitch2)
        elif temp == "try south door":
            ui.getNewSitch(self.sitch3)
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
