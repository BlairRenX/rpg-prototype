import tkinter as tk
import time
from random import randint
class UI():
    #setup makes main window
    def __init__(self, main):
        self.main = main
       ##self.output = tk.Label(main, anchor = 'nw', justify = 'left')
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

       # self.fightBTN = t

        #button that calls 'enter' same as above, save for not having the -1c after 'end' as no \n is typed (hope this makes sense)
        
        self.enterbut.place(relx = 0.71, rely = 0.645, relwidth = 0.09)


    #write fucntion takes text and the textbox it's from 
    def enter(self,inpt,txt):
        ###enter.input_entered = True
        txt = txt.replace('\n','')
       
        if txt == 't':
            ui.talkWindow(me,C1)
        txt = self.cleanInput(txt)
        self.cleanOutput()
        txt = txt+'\n'
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

        #jeremy.nextSitch(self.txt)
        
        self.inpt.delete('0.0','end')
        #disable output so cannot be typed in
        
           
    def write(self,txt):
        
        txt = self.cleanInput(txt)
        self.cleanOutput()
        txt+='\n'
        self.inpt.config(state = 'disabled')
        for i in txt:
            self.text += i
            self.output.config(text = self.text)
            time.sleep(0.05)
            #tkinter is shit
            self.main.update()
        self.inpt.config(state = 'normal')
        

    def cleanOutput(self):
        if self.text.count('\n')>25:
            cutof = self.text.index('\n')+1
            self.text = self.text[cutof:]

    def cleanInput(self,txt):
        if txt[0] == '\n':
            txt = txt[1:]
        n = 0
        for i in range(len(txt)):
            if txt[i] != '\n':
                n+=1
            else:
                n = 0
                
            if n > 80 and txt[i] == ' ': #arbriaty number
                n = 0
                txt = txt[:i] + '\n' + txt[i+1:]
            elif n > 95:
                n = 0
                txt = txt[:i] + '-\n' + txt[i:]
        return(txt)

    def talkWindow(ui,player,npc):
        talkUi = TalkUi(main,player,npc)




class TalkUi():
    def __init__(self, main,player,npc):
        self.text =''
        self.main = tk.Toplevel(main) 
        self.main.geometry("600x500")
        self.main.config(background ='#facade')

        self.output = tk.Label(self.main, anchor = 'nw', justify = 'left')
        self.output.place(relx =0.2, rely = 0.02, relheight=0.6, relwidth=0.6)

        self.talkBTN = tk.Button(self.main, text='Talk', background = 'light blue', height = 2, command = lambda:(self.enter(self.inpt,self.inpt.get('1.0','end'),npc) ))
       # self.
        
        self.inpt =  tk.Text(self.main, height = 1)
        self.inpt.bind("<Return>", lambda x: self.enter(self.inpt,self.inpt.get('1.0','end-1c'),npc))
        self.inpt.bind("<space>", lambda x:self.inpt.delete('0.0','end+2c'))
        self.inpt.place(relx =0.36, rely = 0.65,  relwidth=0.25)
        self.conversationBegin(npc)

        self.mood = [' angry at ',' unhapy with ',' taken aback by ',' fine with ',' happy with ',' enthusiastic with ', ' ecstatic at ']
        
        self.prevWord = 'start'

    def conversationBegin(self,npc):
        self.write('You enter conversation with a '+npc.desc)
        self.write(npc.name+ ':    ' + npc.talk['start'][0])
        self.inConversation = True



    def reply(self,npc,word):
        if self.inConversation:
            if word in npc.talk:
                if npc.intrest + npc.talk[word][1][0] < 7:
                    npc.intrest += npc.talk[word][1][0]
                else:
                    npc.intrest = 6
                if npc.intrest + npc.talk[word][1][0] < 0:
                    self.write('That seems to have struck a nerve with %s, they turn away. This conversation is clearly over.'%npc.name)
                    self.inConversation  = False
                else:    
                    self.write(npc.name+ ' seems' +self.mood[npc.intrest] +'your response')
                    self.write(npc.name+ ':    ' + npc.talk[word][0])
                    self.prevWord = word
                
            if word not in npc.talk:
                if npc.talk[self.prevWord][1][1] != 0:
                    npc.intrest += npc.talk[self.prevWord][1][1]
                    if npc.intrest >-1:
                        self.write(npc.name+ ' seems' +self.mood[npc.intrest] +'your response')
                    else:
                        self.write(npc.name +' has had enough of you. This conversation is clearly over')
                        self.inConversation = False
                else:
                    self.write(npc.name + ' didn\'t understand you, but they didn\'t seem to care. They are still' + self.mood[npc.intrest] +'you.')





    def enter(self,inpt,txt,npc):
        
        txt = txt.replace('\n','')
        if txt[-1] in ('?','.',' ','\n'):
            txt = txt[:-1]
        if txt[0] == ' ':
            txt = txt[1:]
        txt = self.cleanInput(txt)
        self.cleanOutput()
        txt = txt+'\n'
        for i in txt:
            self.text += i
            self.output.config(text = self.text)
            
            self.inpt.delete('end-2c','end-1c')
            time.sleep(0.03)
            #tkinter is shit
            self.main.update()
        txt = txt.replace('\n','')
        self.reply(npc,txt)
        self.inpt.delete('0.0','end')

                    
    def write(self,txt):
        txt = self.cleanInput(txt)
        self.cleanOutput()
        txt+='\n'
        self.inpt.config(state = 'disabled')
        for i in txt:
            self.text += i
            self.output.config(text = self.text)
            time.sleep(0.03)
            #tkinter is shit
            self.main.update()
        self.inpt.config(state = 'normal')

    def cleanOutput(self):
        if self.text.count('\n')>16:
            cutof = self.text.index('\n')+1
            self.text = self.text[cutof:]

    def cleanInput(self,txt):
        if txt[0] == '\n':
            txt = txt[1:]
        n = 0
        for i in range(len(txt)):
            if txt[i] != '\n':
                n+=1
            else:
                n = 0
                
            if n > 50 and txt[i] == ' ': #arbriaty number
                n = 0
                txt = txt[:i] + '\n' + txt[i+1:]
            elif n >65:
                n = 0
                txt = txt[:i] + '-\n' + txt[i:]
        return(txt)
    

    
   
    
    



            

main = tk.Tk()
ui = UI(main)

#ui.combatWindow()


class Player():
    def __init__(self):
        self.health = 20
        self.damage = 5
        self.acuracy = 80
         
    def talk(self, other):
        ui.talkWindow(self,other)
        
       
 
class Npc():
    def __init__(self,ID,name,desc,talk,intrest):
        self.ID = ID
        self.name = name
        self.desc = desc
        self.talk = talk
        self.intrest = intrest
       
        
   
        
  
        
       

        
me = Player()
TalkC1 = {  'start':['Well hello there. Can I intrest you in some lemons?',[0,-1]],
            'lemons':['Oh yes, fresh yellow lemons from my home. My wife picks them. Care to buy any?',[0,0]],
            'yes':['Very good sir. Goodbye',[+1,-2]],
            'no':['Well i\'m sorry to hear that. Have a good day',[-3,-6]],
            'wife':['Oh yes, i love my wife so very much',[+4,0]],
            'home':['it\'s a small house. I dont much care for it',[-1,-1]]}
C1 = Npc('C1','John','a small man', TalkC1,3)


#Bugs:
# 1) Weird leading space stuff
# 2) Can type \n with enter key when box is empty, tried to fix but tripped up by (1)
#

main.mainloop()
