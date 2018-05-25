import random
import tkinter as tk
import time
from random import randint
class UI():
    #setup makes main window
    def __init__(self, main):
        self.main = main
       ##self.output = tk.Label(main, anchor = 'nw', justify = 'left')
        self.inpt =  tk.Text(main, height = 1,fg='#22ee22', background = '#003000')
        self.enterbut = tk.Button(main, text='Enter',fg='#22ee22', background = '#000100', height = 1, command = lambda:( self.enter(self.inpt,self.inpt.get('1.0','end')) ))
        self.text = ''

        self.situation = ["You stand in an empty room. There is a door ahead of you and a door behind you", ["Try north door", "Try south door", "Other"]]
    
   
        
        self.main.geometry("850x700")
        self.main.config(background ='#000800')

        #Big output text box. Disabled so cannot be typed in.
        #rel-x,y,height,width are relative placement for window
        #self.output = tk.Label(main, anchor = 'nw', justify = 'left')
        self.output = tk.Label(main, anchor = 'nw', justify = 'left',  font = ('Courier New', 9), fg='#22ee22', bg='#000800')
        self.output.place(relx =0.2, rely = 0.02, relheight=0.6, relwidth=0.8)

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
        txt = self.cleanInput(txt)
        self.cleanOutput()
        if isinstance(txt,str):
           
            
            txt = txt.replace('\n','')

            if txt == 't':
                ui.talkWindow(jeremy,C1)
            if txt == 'g':
                ui.gunWindow(None,None)
            
            ui.write('\n')
            txt = txt+'\n'
            for i in txt:
                #Types to the end of textbox with value i
                self.text += i
                self.output.config(text = self.text)

                self.inpt.delete('end-2c','end-1c')
                #sleep for that cool typing effect
               ## time.sleep(0.03)
                #tkinter is shit
                self.main.update()
            #scrolls output to bottom (without its not possible to scroll at all, its odd)   
            #makes sure input is empt but is currently buggy not sure why, seems to automatically lead with a \n or ' ' weird ass shit
            Interpret(txt,jeremy)
            self.inpt.delete('0.0','end')
            #disable output so cannot be typed in
        else:
            pass
           
    def write(self,txt):
        txt = str(txt)
        txt = self.cleanInput(txt)
        self.cleanOutput() 
        txt+='\n'
        self.inpt.config(state = 'disabled')
        for i in txt:
            self.text += i
            self.output.config(text = self.text)
           ## time.sleep(0.05)
            #tkinter is shit
            self.main.update()
        self.inpt.config(state = 'normal')
        

    def cleanOutput(self):
        while self.text.count('\n')>23:
            cutof = self.text.index('\n')+1
            self.text = self.text[cutof:]

    def cleanInput(self,txt):
        if isinstance(txt,str):
            if len(txt)>0:
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
    def gunWindow(ui,player,enemy):
        gunUi = GunUi(main,player,enemy)




class TalkUi():
    def __init__(self, main,player,npc):
        self.text =''
        self.main = tk.Toplevel(main) 
        self.main.geometry("600x500")
        self.main.config(background ='#001100')

        self.output = tk.Label(self.main, anchor = 'nw', justify = 'left')
        self.output.place(relx =0.2, rely = 0.02, relheight=0.6, relwidth=0.6)

        self.talkBTN = tk.Button(self.main, text='Talk', background = 'light blue', height = 2, command = lambda:(self.TalkEnter(self.inpt,self.inpt.get('1.0','end'),npc) ))
       # self.
        
        self.inpt =  tk.Text(self.main, height = 1)
        self.inpt.bind("<Return>", lambda x: self.TalkEnter(self.inpt,self.inpt.get('1.0','end-1c'),npc))
        self.inpt.bind("<space>", lambda x:self.inpt.delete('0.0','end+2c'))
        self.inpt.place(relx =0.36, rely = 0.65,  relwidth=0.25)
        self.conversationBegin(npc)

        self.mood = [' angry at ',' unhapy with ',' taken aback by ',' fine with ',' happy with ',' enthusiastic with ', ' ecstatic at ']
        
        self.prevWord = 'start'

    def conversationBegin(self,npc):
        self.TalkWrite('You enter conversation with a '+npc.desc)
        self.TalkWrite(npc.name+ ':    ' + npc.talk['start'][0])
        self.inConversation = True



    def reply(self,npc,word):
        if self.inConversation:
            if word in npc.talk:
                if npc.interest + npc.talk[word][1][0] < 7:
                    npc.interest += npc.talk[word][1][0]
                else:
                    npc.interest = 6
                if npc.interest + npc.talk[word][1][0] < 0:
                    self.TalkWrite('That seems to have struck a nerve with %s, they turn away. This conversation is clearly over.'%npc.name)
                    self.inConversation  = False
                else:    
                    self.TalkWrite(npc.name+ ' seems' +self.mood[npc.interest] +'your response')
                    self.TalkWrite(npc.name+ ':    ' + npc.talk[word][0])
                    self.prevWord = word
                
            if word not in npc.talk:
                if npc.talk[self.prevWord][1][1] != 0:
                    npc.interest += npc.talk[self.prevWord][1][1]
                    if npc.interest >-1:
                        self.TalkWrite(npc.name+ ' seems' +self.mood[npc.interest] +'your response')
                    else:
                        self.TalkWrite(npc.name +' has had enough of you. This conversation is clearly over')
                        self.inConversation = False
                else:
                    self.TalkWrite(npc.name + ' didn\'t understand you, but they didn\'t seem to care. They are still' + self.mood[npc.interest] +'you.')





    def TalkEnter(self,inpt,txt,npc):
        
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
            time.sleep(0.01)
            #tkinter is shit
            self.main.update()
        txt = txt.replace('\n','')
        self.reply(npc,txt)
        self.inpt.delete('0.0','end')

                    
    def TalkWrite(self,txt):
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
        if isinstance(txt,str):
            if len(txt)>0:
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

class GunUi():
    def __init__(self, main,player,enemy):
        self.text =''
        self.main = tk.Toplevel(main) 
        self.main.geometry("600x500")
        self.main.config(background ='#000000')
        self.main.focus_set()
        self.playerbtns = [[],[],[],[]]
        self.enemybtns = [[],[],[],[]]

        self.info = tk.Label(self.main,bg ='black',fg = '#22ee22', text = 'Arrows to move, \n space to skip moving,\n space to target, space to untarget,\n enter to attack, shift+r to reset')
        self.info.place(y = 150, x = 205)

        self.playerHits = tk.Label(self.main,bg ='black',fg = '#22ee22', text = 'Total Hits: 0\nDirect Hits: 0\nDamage Percentage: -%')
        self.playerHits.place(x = 50,y=320)
        self.enemyHits = tk.Label(self.main,bg ='black',fg = '#22ee22',text = 'Total Hits: 0\nDirect Hits: 0\nDamage Percentage: -%')
        self.enemyHits.place(x = 400,y=320)
        
        self.playerGridSize = 4
        for j in range (self.playerGridSize):
            for i in range(self.playerGridSize):
                self.topRow = tk.Button(self.main,height = 2, width = 4,bg = '#000000')
                self.topRow.place(y = 150+(40*j), x = 50+(37*i))
                self.playerbtns[j].append(self.topRow)
        self.enemyGridSize = 4
        for j in range (self.enemyGridSize):
            for i in range(self.enemyGridSize):
                self.topRow = tk.Button(self.main,height = 2, width = 4, bg = '#000000')
                self.topRow.place(y = 150+(40*j), x = 400+(37*i))
                self.enemybtns[j].append(self.topRow)


        self.enemyCharacter = [randint(0,self.enemyGridSize-1),randint(0,self.enemyGridSize-1)]
        self.numberEnemyMove = []

        
        self.moving = True
        self.attackPhase = False
        self.playerPos = [0,0]
        self.targetPos = [0,0]
        self.moves = []
        self.enemyMoves = []
        self.numberEnemyMove =  0
        self.targeted = []
        self.playerbtns[self.playerPos[0]][self.playerPos[1]].config(background = 'green')

        self.playerCanTarget = 4
        
        self.enemyMovement = 3
        self.enemyCanTarget = 4
        
        self.playerDarkGreenHits = 0
        self.playerLightGreenHits = 0

        self.enemyDarkBlueHits = 0
        self.enemyLightBlueHits = 0

        

        
##        self.me = tk.Button(self.main,height = 1, width = 2)
##        self.me.place(x = 5,y=10)
        #self.talkBTN = tk.Button(self.main, text='Talk', background = 'light blue', height = 2, command = lambda:(self.TalkEnter(self.inpt,self.inpt.get('1.0','end'),npc) ))
       # self.
        
        #self.inpt =  tk.Text(self.main, height = 1)
        #self.inpt.bind("<Return>", lambda x: self.TalkEnter(self.inpt,self.inpt.get('1.0','end-1c'),npc))
        #self.inpt.bind("<space>", lambda x:self.inpt.delete('0.0','end+2c'))
        #self.inpt.place(relx =0.36, rely = 0.65,  relwidth=0.25)


        #self.btns[0][3].config(background = 'black')

##
        self.main.bind("<Left>", lambda x:self.PlayerMove([0,-1]))
        self.main.bind("<Right>", lambda x:self.PlayerMove([0,1]))
        self.main.bind("<Up>", lambda x:self.PlayerMove([-1,0]))
        self.main.bind("<Down>", lambda x:self.PlayerMove([1,0]))
        self.main.bind("<space>",lambda x:self.PlayerTarget())
        self.main.bind("<Return>",lambda x:self.EnemyMove())
        self.main.bind("<R>",lambda x:self.Reset()) ## To Remove ToDO


    def Reset(self):
        if len( self.enemyMoves)>0: 
            self.enemyCharacter = [self.enemyMoves[-1][0],self.enemyMoves[-1][1]]
        else:
            self.enemyCharacter = [randint(0,self.enemyGridSize-1),randint(0,self.enemyGridSize-1)]
        self.numberEnemyMove = []
         
        for lst in self.enemybtns:
            for btn in lst:
                btn.config(bg='#000000')
        for lst in self.playerbtns:
            for btn in lst:
                btn.config(bg='#000000')
            
        self.moving = True
        self.attackPhase = False
        self.targetPos = [0,0]
        self.moves = []
        self.enemyMoves = []
        self.numberEnemyMove =  0
        self.targeted = []
        self.playerbtns[self.playerPos[0]][self.playerPos[1]].config(background = 'green')

       
        
        self.playerDarkGreenHits = 0
        self.playerLightGreenHits = 0

        self.enemyDarkBlueHits = 0
        self.enemyLightBlueHits = 0

        
    def PlayerMove(self,direction):
        if not self.attackPhase:
            if len(self.moves) >= 3:
                self.moving = False
            if self.moving:
                if self.playerPos[0] + direction[0] >= 0 and self.playerPos[0] + direction[0] < self.playerGridSize and self.playerPos[1] + direction[1] >= 0 and self.playerPos[1] + direction[1] < self.playerGridSize:      
                    self.playerbtns[self.playerPos[0]][self.playerPos[1]].config(background = '#62ff3f')
                    self.playerPos[0]+=direction[0]
                    self.playerPos[1]+=direction[1]
                    self.moves.append(direction)
                    self.playerbtns[self.playerPos[0]][self.playerPos[1]].config(background = 'green')
                    if len(self.moves) == 3:
                        self.enemybtns[0][0].config(bg = 'blue')
                    self.main.update()
            else:   
                if self.targetPos[0] + direction[0] >= 0 and self.targetPos[0] + direction[0] < self.playerGridSize and self.targetPos[1] + direction[1] >= 0 and self.targetPos[1] + direction[1] < self.playerGridSize:
                    if [self.targetPos[0],self.targetPos[1]] not in self.targeted:
                        self.enemybtns[self.targetPos[0]][self.targetPos[1]].config(background = '#000000')
                    self.targetPos[0]+=direction[0]
                    self.targetPos[1]+=direction[1]
                    if [self.targetPos[0],self.targetPos[1]] not in self.targeted:
                        self.enemybtns[self.targetPos[0]][self.targetPos[1]].config(background = 'blue')
                    self.main.update()
                
    def PlayerTarget(self):
        if not self.attackPhase:
            if self.moving:
                self.moving = False
                self.enemybtns[0][0].config(bg = 'blue')
            else:
                if self.targetPos not in self.targeted and len(self.targeted) <self.playerCanTarget:
                    self.enemybtns[self.targetPos[0]][self.targetPos[1]].config(background = 'red')
                    self.targeted.append(self.targetPos[:])
                elif self.targetPos in self.targeted:
                    self.enemybtns[self.targetPos[0]][self.targetPos[1]].config(background = 'blue')
                    self.targeted.remove(self.targetPos[:])
            self.main.update()


    
                        
    def PlayerAttack(self):
        if self.attackPhase:
            for item in self.targeted:
                for i in range(len(self.enemyMoves)):
                    if self.enemyMoves[i] ==item and i <len(self.enemyMoves)-1:
                        self.enemyLightBlueHits +=1
                        self.enemybtns[self.enemyMoves[i][0]][self.enemyMoves[i][1]].config(bg = 'gold')
                    elif self.enemyMoves[i] ==item and i == len(self.enemyMoves)-1:
                        self.enemyDarkBlueHits+=1
                        self.enemybtns[self.enemyMoves[i][0]][self.enemyMoves[i][1]].config(bg = 'orange')
                

                if item not in self.enemyMoves:
                    self.enemybtns[item[0]][item[1]].config(bg = 'red')
                    
                self.main.update()
                time.sleep(0.5)
        



                                    
    def EnemyAttack(self):
        if self.attackPhase:
            targets = []
            for i in range(self.enemyCanTarget):
                for i in range(self.playerGridSize**2):
                    target = [randint(0,self.playerGridSize-1),randint(0,self.playerGridSize-1)]
                    if target not in targets:
                        break
                if target not in targets:
                    targets.append(target)
                    if self.playerbtns[target[0]][target[1]]["background"] == 'green':
                        self.playerbtns[target[0]][target[1]].config(bg = 'gray')
                        self.playerDarkGreenHits+=1
                    elif self.playerbtns[target[0]][target[1]]["background"] == '#62ff3f': # light green
                        self.playerbtns[target[0]][target[1]].config(bg = 'dark gray')
                        self.playerLightGreenHits+=1
                    else:
                        self.playerbtns[target[0]][target[1]].config(bg = 'red')
                
                self.main.update()
                time.sleep(1)
            
            
    def EnemyMove(self):
        self.attackPhase = True
        for i in self.enemybtns:
            for btn in i:
                btn.config(bg='#000000')
        
        self.enemyMoves.append(self.enemyCharacter)
        
      
        self.enemybtns[self.enemyCharacter[0]][self.enemyCharacter[1]].config(bg = 'blue')
        self.main.update()
        time.sleep(1)
        
        enemyPos = self.enemyCharacter[:]
        self.numberEnemyMove = 0
        if randint(0,1): # move less than maximum
            move = randint(0,self.enemyMovement)
        else:
            move = self.enemyMovement
        for i in range(move):
            rand = randint(0,3)
            directions = [[0,1],[0,-1],[1,0],[-1,0],[0,1],[0,-1],[1,0],[-1,0]] # will randomly pick one of first 4, then cycle until valid
            direction = directions[rand][:]
            for j in range(4):
                
                if enemyPos[0] + direction[0] >= 0 and enemyPos[0] + direction[0] < self.enemyGridSize and enemyPos[1] + direction[1] >= 0 and enemyPos[1] + direction[1] < self.enemyGridSize and(enemyPos[0]+direction[0]!=self.enemyCharacter[0] or enemyPos[1]+ direction[1]!=self.enemyCharacter[1]):
                    self.numberEnemyMove+=1
                    enemyPos[0]+=direction[0]
                    enemyPos[1]+=direction[1] # enemy
                    for item in self.enemyMoves:
                        self.enemybtns[item[0]][item[1]].config(bg = '#7caeff')#light blue
                    self.enemybtns[enemyPos[0]][enemyPos[1]].config(bg = 'blue')
                    self.enemyMoves.append(enemyPos[:])
                    self.main.update()
                    time.sleep(1)
                    break
                else:
                    rand+=1
                    direction = directions[rand][:]
        for item in self.enemyMoves:
            self.enemybtns[item[0]][item[1]].config(bg = '#7caeff')
        self.enemybtns[self.enemyMoves[-1][0]][self.enemyMoves[-1][1]].config(bg = 'blue')
        self.PlayerAttack()
        self.EnemyAttack()  
        self.Damage()


    def Damage(self):

        if len(self.moves) == 0:
            self.playerDamagePercent =self.playerDarkGreenHits
        else:
            self.playerDamagePercent = (self.playerDarkGreenHits*(1-len(self.moves)/6) + self.playerLightGreenHits/6)#len(self.moves)*(1-(1-len(self.moves)/6)) # Fuckin headache right
        
##        if len(str(self.playerDamagePercent)) > 5:
##            self.playerDamagePercent = str(self.playerDamagePercent)[:6]
        
        
        newPText = 'Total Hits: %s\nDirect Hits: %s\nDamage Percentage: %.2f%s'%((self.playerLightGreenHits+self.playerDarkGreenHits),self.playerDarkGreenHits,(self.playerDamagePercent*100),'%')

        self.playerHits.config(text =newPText)

        if self.numberEnemyMove == 0:
            self.playerDamagePercent =self.playerDarkGreenHits
        else:
            self.enemyDamagePercent = (self.enemyDarkBlueHits*(1-self.numberEnemyMove/6) + self.enemyLightBlueHits/6)

##        if len(str(self.enemyDamagePercent)) > 5:
##            self.enemyDamagePercent =str(self.enemyDamagePercent)[:6]
        newEText = 'Total Hits: %s\nDirect Hits: %s\nDamage Percentage: %.2f%s'%((self.enemyDarkBlueHits+self.enemyLightBlueHits),self.enemyDarkBlueHits,(self.enemyDamagePercent*100),'%')
        self.enemyHits.config(text =newEText)


class Place(object):
    def __init__(self, name, quality = 3, furnishings = [], objects = [], characters = [],search = ["an empty room"], investigation = ["There is nothing of note here."]):
        self.doors = []
        self.name = name
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array
        self.quality = quality
        self.furnishings = furnishings
        self.objects = objects
        self.characters = characters

        self.search = search

        self.investigation = investigation
        #should be of the form [canBeInvestigated, Description, leadsTo]
        #'cept obviously you still get a description if you can't

        for furnishing in self.furnishings:
            furnishing.room = self
            
    def showAll(self):
        temp = []
        tempTemp = []
        for furnishing in self.furnishings:
            tempTemp.append(furnishing.name)
        temp.append(tempTemp)
        
        tempTemp = []
        for anObject in self.objects:
            tempTemp.append(anObject.name)
        temp.append(tempTemp)

        tempTemp = []
        for character in self.characters:
            tempTemp.append(character.desc)
        temp.append(tempTemp)

        tempTemp = []
        for door in self.doors:
            tempTemp.append(door.name)
        temp.append(tempTemp)

        return temp

    def showAllObjects(self):
        temp = []
        tempTemp = []
        for furnishing in self.furnishings:
            tempTemp.append(furnishing)
        temp.append(tempTemp)
        
        tempTemp = []
        for anObject in self.objects:
            tempTemp.append(anObject)
        temp.append(tempTemp)

        tempTemp = []
        for character in self.characters:
            tempTemp.append(character)
        temp.append(tempTemp)

        tempTemp = []
        for door in self.doors:
            tempTemp.append(door)
        temp.append(tempTemp)

        return temp

    def showAllInvObjects(self):
        objList = [[],[]]
        for item in jeremy.inventory:
            objList[0].append(item.name)
            objList[1].append(item)
        return(objList)

    def showAllObjectsAndNames(self):
        temp1 = self.showAll()
        temp2 = self.showAllObjects()
        invObjects = self.showAllInvObjects()
        temp3 = []
        for i in range(len(temp1)):
            temp3.append([temp1[i],temp2[i]])
        return temp3,[invObjects]
        
            
    def showDoors(self):
        for door in self.doors:
            ui.write(door.viewDoors())
            
    def setDoors(self, otherRooms, direction=2):
        for otherRoom in otherRooms:
            self.doors.append(Door("D" + self.name + otherRoom.name, self, otherRoom, direction))

    def setDoorDescs(self):    
        for door in self.doors:
            door.setDescriptor()


    def DescribeRoom(self):
            
        roomDescription = ""
        roomDescription += "The room is " + self.search + ". "
        randomSense = random.randint(0,3)
        if randomSense == 0:
            roomSight = []
            f = open("senses\\sights1.txt", "r")
            for row in f:
                roomSight.append(row)
            f.close()

            if self.quality == 1:
                roomDescription += roomSight[0]
            elif self.quality == 2:
                roomDescription += roomSight[1]
            elif self.quality == 3:
                roomDescription += roomSight[2]
            elif self.quality == 4:
                roomDescription += roomSight[3]
            elif self.quality == 5:
                roomDescription += roomSight[4]

        if randomSense == 1:
            roomSound = []
            f = open("senses\\sounds1.txt", "r")
            for row in f:
                roomSound.append(row)
            f.close()

            if self.quality == 1:
                roomDescription += roomSound[0]
            elif self.quality == 2:
                roomDescription += roomSound[1]
            elif self.quality == 3:
                roomDescription += roomSound[2]
            elif self.quality == 4:
                roomDescription += roomSound[3]
            elif self.quality == 5:
                roomDescription += roomSound[4]

        if randomSense == 2:
            roomFeel = []
            f = open("senses\\feels1.txt", "r")
            for row in f:
                roomFeel.append(row)
            f.close()

            if self.quality == 1:
                roomDescription += roomFeel[0]
            elif self.quality == 2:
                roomDescription += roomFeel[1]
            elif self.quality == 3:
                roomDescription += roomFeel[2]
            elif self.quality == 4:
                roomDescription += roomFeel[3]
            elif self.quality == 5:
                roomDescription += roomFeel[4]
            
                
        if randomSense == 3:
            roomSmell = []
            f = open("senses\\smells1.txt", "r")
            for row in f:
                roomSmell.append(row)
            f.close()
            
            if self.quality == 1:
                roomDescription += roomSmell[0]
            elif self.quality == 2:
                roomDescription += roomSmell[1]
            elif self.quality == 3:
                roomDescription += roomSmell[2]
            elif self.quality == 4:
                roomDescription += roomSmell[3]
            elif self.quality == 5:
                roomDescription += roomSmell[4]
        
        if len(self.furnishings) > 0:
            roomDescription += "The room is furnished with "
            for furnishing in self.furnishings:
                roomDescription += "a " +furnishing.basicDesc + ", "

        if len(self.objects) > 0:
            roomDescription += "In the room, there is "
            for roomObject in self.objects:
                if roomObject.hidden == False:
                    roomDescription += roomObject.basicDesc

        for door in self.doors:
            roomDescription += " There is a door to the " + door.name[:-5] + "."
        return roomDescription
            
        
class Door(object):
    def __init__(self, doorID, room1, room2, direction, locked=[False, None], opened=False, seeThrough = True, description = 'A basic, nondescript door. It looks quite old.'):
        self.doorID = doorID
        self.room1 = room1
        self.room2 = room2
        self.name = ""
        self.description = description
        self.opened = opened
        self.locked = locked
        #if it's locked, and if so, what's used to unlock it
        
        self.seeThrough = seeThrough
        #If door is open, can player see into the connected room

        self.direction = direction
        #the direction RELATIVE TO ROOM1

##all mentioned direction relative to the centre of the room
##0 is south
##2 is north
##1 is west
##3 is east
##4 is above
##5 is below
##others might be added at some point if jake yaks at me enough
##
##and obviously for an overworld this either ain't gonna be necessary or will need to be changed, but we'll get to that


##    def setDoors(self):
##        self.room1.doors.append(self)
##        self.room2.doors.append(self)
    def viewDoors(self):
        return("This " + self.name + " connects " + self.room1.search + " and " + self.room2.search + ".")
    def goThrough(self, currentRoom):
        return self.room2
    def goBackThrough(self, currentRoom):
        return self.room1
    
    def setDescriptor(self):
##        if self == self.room1.doors[0]:
##            self.name = "north door"
##        elif self == self.room1.doors[1]:
##            self.name = "south door"
##        elif self == self.room1.doors[2]:
##            self.name = "west door"
##        elif self == self.room1.doors[3]:
##            self.name = "east door"
##        else:
##            self.name = "forbidden door"
##        print("Door " + self.doorID)
##        print("Room one's doors:")
##        for door in self.room1.doors:
##            print(door.doorID)
##        print("Room two's doors:")
        for door in self.room2.doors:
            #print(door.doorID)
            if door.room1 == self.room2 and door.room2 == self.room1:
                if door.direction == 2:
                    self.direction = 0
                    
                    self.name = "south door"
                elif door.direction == 0:
                    self.direction = 2

                    self.name = "north door"
                elif door.direction == 1:
                    self.direction = 3

                    self.name = "east door"
                elif door.direction == 1:
                    self.direction = 1

                    self.name = "west door"
                elif door.direction == 4:
                    self.direction = 5

                    self.name = "trap door"
                elif door.direction == 5:
                    self.direction = 4

                    self.name = "hatch door"
                else:
                    self.name = "forbidden door"

        if self.direction == 2:
            self.name = "north door"

    def Open(self, openTool,traveling):

        if self.opened == True:
            ui.write("The door is already open.")
            
        elif self.opened == False and self.locked[0] == False:
            self.opened = True
            ui.write("The " + self.name + " is not locked. You open it.")
             
        elif self.locked[0] == True and self.opened == False:
            if openTool is not None and openTool != '':
                if openTool.name == self.locked[1]:
                    self.locked = False
                    self.opened = True
                    ui.write("The " + self.name + " is locked. You open it using the " + openTool.name + ".")
                else:
                    ui.write("You can't unlock this with the " + openTool.name)
            else:
                ui.write("The door is locked, or perhaps it is only stuck. You can\'t get it open anyhow.")
                
        if self.opened and not traveling:                
            if jeremy.currentRoom.name != self.room1.name and self.seeThrough:
                ui.write('Through this door you can make out %s.'%self.room1.search)
            elif jeremy.currentRoom.name != self.room2.name and self.seeThrough:
                ui.write('Through this door you can see %s.'%self.room2.search)
            else:
                ui.write('It isn\'t clear where this leads.')
            ui.write('You stay standing in the doorway.')

    def Close(self):
        if self.opened == True:
            self.opened = False
            ui.write("You close the " + self.name)
        elif self.opened == False:
            ui.write("The " + self.name + " is already closed.")
            

class gameObject(object):
    def __init__(self, basicDesc, inspectDesc, hidden = False):
        self.basicDesc = basicDesc
        #a description that displays when you look at it

        self.inspectDesc = inspectDesc
        #a description that displays when you inspect it
        self.hidden = hidden
        #in case it's locked away and shouldn't be found immediately

        self.usable = []
        #gonna need to talk a lot of this over with jake when we get to integration

    def getDesc(self):
        #print(self.basicDesc)
        
        return self.basicDesc

class roomFurnishing(gameObject):
    def __init__(self, name, basicDesc, inspectDesc, interactive=[False,[]], containedObjects=[], opened=[False,None], locked=[False, None]):
        super(roomFurnishing, self).__init__(basicDesc, inspectDesc)
        self.name = name

        self.investigation = []
        #as with the place investigation, but on a single furnishing within a room
        self.interactive = interactive
        self.containedObjects = containedObjects
        self.room = None
        for item in self.containedObjects:
            item.hidden = True

        self.opened = opened
        
        if len(self.containedObjects) > 0:
            self.interactive[0] = True
            self.interactive[1].append('open')
            self.opened = [True,False]
            
        
            
            
        
        self.locked = locked
        
    def Open(self, openTool):
        if self.opened[0] == True:
            if self.opened[1] == False:
                if self.locked[0] == False:
                    self.opened[1] = True
                    ui.write("The " + self.basicDesc + " is not locked. You open it.")
                    
            elif self.locked[0] == True:
                if openTool.name == self.locked[1]:
                    self.locked = False
                    self.opened[1] = True
                    ui.write("The " + self.name + " is locked. You open it using the " + openTool.name + ".")
                else:
                    ui.write("You can't unlock this with the " + openTool.name)
            elif self.opened[1] == True:
                ui.write("The door is already open.")
                
            if self.opened[1] == True:
                if len(self.containedObjects) == 0:
                    ui.write("There was nothing inside.")
                else:
                    ui.write("The " + self.basicDesc + " contains:")
                    for item in self.containedObjects:
                        item.hidden = False
                        self.room.objects.append(item)
                        ui.write(item.basicDesc)
        else:
            ui.write('The ' + self.basicDesc + ' cannot be opened.') 
                    
    def Close(self):
        if self.opened[0] == True:
            if self.opened[1] == True:
                for item in self.containedObjects:
                    item.hidden = True
                    self.room.objects.remove(item)
                self.opened[1] = False
                ui.write("You close the "+ self.basicDesc)
            else:
                ui.write("This " + self.basicDesc + " is already closed.")
        else:
            ui.write("This " + self.basicDesc + " cannot be closed.")

    

class inventoryObject(gameObject):
    def __init__(self, name, basicDesc, inspectDesc, expendable = [False], droppable=True, equippable = [False], taken=["No-one","You pick up the"]):
        super(inventoryObject,self).__init__(basicDesc, inspectDesc)

        self.name = name

        self.taken = taken
        #include things about ownership, a description when you pick it up, etc...

        self.droppable = droppable
        #removing itself from the bag, and so on...

        self.expendable = expendable
        #if it's expendable, and if so, how many uses it has

        self.equippable = equippable
        #currently using a simple numerical value for quality



class Character(object):
    def __init__(self, name, startingRoom, inventory):
        self.name = name
        self.inventory = inventory
        self.currentRoom = startingRoom
        #an array of inventory objects
        
        basicShirt = inventoryObject(name ="basic shirt", basicDesc="a basic synth-cloth shirt", inspectDesc="There's a small rip in the armpit...", equippable=[True,"clothesTorso"])
        basicLegs = inventoryObject(name= "basic legwear", basicDesc="basic synth-cloth legwear", inspectDesc="This could probably do with being washed.", equippable=[True, "clothesLegs"])
        basicShoes = inventoryObject(name="basic shoes", basicDesc="basic synthetic fabric and rubber shoes", inspectDesc="You can feel a hole in your sock. Ugh.", equippable=[True, "footwear"])
        
        self.inventory.append(basicShirt)
        self.inventory.append(basicLegs)
        self.inventory.append(basicShoes)

        #in case we decide to add stats later

        self.equipped = {
            "clothesTorso" : basicShirt,
            "clothesLegs" : basicLegs,
            "armwear" : None,
            "headgear" : None,
            "footwear" : basicShoes,
            "armourTorso" : None,
            "armourLegs" : None,
            "accessories" : [],
            "weaponLeft" : None,
            "weaponRight" : None,
            "weaponBoth" : None
            }
        #this is more for a fantasy setting and it hasn't been tested cuz I wrote it at 00:37

    def getName(self):
        return self.name

    def whatsMine(self):
        for item in self.equipped:
            if self.equipped[item] == None or self.equipped[item] == []:
                pass
            else:
                ui.write(self.equipped[item].basicDesc[0].upper()+self.equipped[item].basicDesc[1:])


 


class nonPlayerCharacter(Character):
    def __init__(self, ID, name, desc, talk, interest, startingRoom, inventory = []):
        super(nonPlayerCharacter,self).__init__(name,startingRoom, inventory)
        self.ID = ID
        self.desc = desc
        self.talk = talk
        self.interest = interest

class playerCharacter(Character):
    def __init__(self, name, startingRoom, inventory = []):
        super(playerCharacter,self).__init__(name, startingRoom, inventory)
        #this should really be in the Character class but I want to make sure it's working first

    def UseItem(self, item):
        #the actual use
        if item.expendable[0] == True:
            if item.expendable[1] == 1:
                self.inventory.remove(item)
            else:
                item.expendable[1] = item.expendable[1] -1
            #if the item's expendable
            #a confirmation message should probably be put in here at some point

    def Inspect(self,item,using):
        if isinstance(item, inventoryObject):
            ui.write("This " + item.name + " belongs to " + item.taken[0] + ".")
            ui.write(item.inspectDesc[0].upper()+item.inspectDesc[1:])
            if len(set(item.equippable[1]).intersection({"weaponRight","weaponLeft"})) > 0:
                ui.write('It can easily be held in one hand, the %s looks like it could be used as a weapon.'%item.name) # todo add weapon type here for description
            if "weaponBoth" in item.equippable[1]:
                ui.write('It is quite heavy, looks like you\'ll need both hands to use this. The %s would make a mighty weapon though.'%item.name)
            if "clothesTorso" in item.equippable[1]:
                ui.write('The %s is quite thin and lightweight, it won\'t provide much in the way of protection. It does make a fine shirt though.'%item.name)
            if "clothesLegs" in item.equippable[1]:
                ui.write('It is not very thick or heavy, it won\'t be much use as protection, but the %s looks to be a good fit as trousers.'%item.name)
            if "armwear" in item.equippable[1]:
                ui.write('This looks like it would fit snugly on your arm, would look quite good there too.')
            if "headgear" in item.equippable[1]:
                ui.write('You feel it would for your head quite well, it\'s almost begging to be put on.')
            if "footwear" in item.equippable[1]:
                ui.write('Looks like these would make some pretty good shoes, they seem they seem about the right size for you.'%item.name)
            if "armourTorso" in item.equippable[1]:
                ui.write('It looks really quite sturdy, the %s looks like it could offer some serious protection for your upper body.'%item.name)
            if "armourLegs" in item.equippable[1]:
                ui.write('These look like some heavy duty trousers, the %s could be used to protect your lower body in combat.'%item.name)
            if "accessories" in item.equippable[1]:
                ui.write('The %s won\'t be much good in the way of utility, you\'re sure it would look quite pretty on you none the less.'%item.name)
                
        elif isinstance(item, roomFurnishing):
            ui.write(item.inspectDesc[0].upper()+item.inspectDesc[1:])
            if item.opened[0]:
                if item.opened[1]:
                    ui.write('The %s is open'%item.name)
                    if len(item.containedObjects) > 0:
                        ui.write('It contains:')
                        for thing in item.containedObjects:
                            ui.write(thing.name[0].upper()+thing.name[1:])
                    else:
                        ui.write('The %s is empty.'%item.name)
                            
                else:
                    ui.write('The %s is closed'%item.name)
                    
                    if item.locked[0]:
                        ui.write('It appears to be locked.')
                    else:
                        ui.write('It doesn\'t seem to be locked in any way')
                    
            if item.interactive[0] == True:
                for interaction in item.interactive[1]:
                    ui.write("It looks like this can be " + interaction + "ed.")
                    
           
        elif isinstance(item, Door):
            ui.write(item.description)
            ui.write('It is to your %s'%item.name[:-5])
            if item.opened:
                ui.write('The door is wide open')
                if self.currentRoom.name != item.room1.name and item.seeThrough:
                    ui.write('You can see this door leads to %s.'%item.room1.search)
                elif self.currentRoom.name != item.room2.name and item.seeThrough:
                    ui.write('You can see this door leads to %s.'%item.room2.search)
                else:
                    ui.write('It isn\'t clear where this leads')

            else:
                ui.write('The door is closed')
                if not item.locked[0]:
                    ui.write('It doesn\'t appear to be locked. It looks as if it could be opened with a heafty pull.')
                else:
                    ui.write('It seems to be locked. That or it\'s rusted shut.')
                ui.write('You aren\'t sure where it leads.') # ToDo change this for previously visited rooms
                

    def TakeItem(self, item):
        if item in self.currentRoom.objects:
            if item.taken[0] == "No-one" or item.taken[0] == "you":
                item.taken[0] = "you"
                self.inventory.append(item)
                
                self.currentRoom.objects.remove(item)
                for furnishing in self.currentRoom.furnishings:
                    if item in furnishing.containedObjects:
                        furnishing.containedObjects.remove(item)
                        
                ui.write(item.taken[1][0].upper()+item.taken[1][1:] +' '+ item.name + ".")
            else:
                ui.write("That's not yours.")
        elif item in self.inventory:
            ui.write("That's already in your inventory")
        else:
            ui.write("That's not in the room.")

    def EquipItem(self,item):
        if item in self.inventory:
            if self.equipped[item.equippable[1][0]] == None:
                self.equipped[item.equippable[1][0]] = item
            elif self.equipped[item.equippable[1][0]] == [] or isinstance(self.equipped[item.equippable[1][0]], list):
                #NOTE: THIS MIGHT NOT WORK
                self.equipped[item.equippable[1][0]].append(item)
            else:
                self.equipped[item.equippable[1][0]] = item
                #I'll put a swap confirmation message here when I'm bothered enough by it
        else:
            ui.write("That item is not in your inventory.")

    def DropItem(self, item):
        if item.droppable == False:
            ui.write("You need this for something.")
        else:
            self.inventory.remove(item)
            currentRoom.objects.append(item)
                
    def DisplayInventory(self):
        ui.write("You have in your possession: ")
        for item in self.inventory:
            ui.write(item.basicDesc[0].upper()+item.basicDesc[1:])
            

    def MoveRooms(self, door):
        #self.currentRoom.doors[door]
        for aDoor in self.currentRoom.doors:
            if aDoor.doorID == door:
                aDoor.Open(None,True) 
                if aDoor.opened:
                    self.currentRoom = aDoor.room2
                    self.showLocation()
                
                
    def showLocation(self):
        ui.write("You are in " + self.currentRoom.search)

    def SearchRoom(self):
        ui.write(self.currentRoom.DescribeRoom())

    def Talk(self, other):
        ui.talkWindow(self,other)
        
aSmallRock = inventoryObject("small rock", "a small rock", "hard stone", [False], True, [True, ["weaponRight","weaponLeft"]])
chestOfDrawers = roomFurnishing(name="chest of drawers",basicDesc="chest of drawers", inspectDesc="A weathered wooden chest of 4 drawers.", containedObjects=[aSmallRock]) 
R1 = Place("R1", 3, [chestOfDrawers], [],[], "a simple yet comfortable bedroom")
R2 = Place("R2",4, [],[], [],"a lavishly decorated mezzanine", "a painting of yourself")
R3 = Place("R3",5, [], [aSmallRock],[])

R1.setDoors([R2])
R2.setDoors([R1, R3], 3)
R3.setDoors([R2], 1)

R1.setDoorDescs()
R2.setDoorDescs()
R3.setDoorDescs()

##R1.showDoors()
##R2.showDoors()
##R3.showDoors()

jeremy = playerCharacter("jeremy", R1)

TalkC1 = {  'start':['Well hello there. Can I interest you in some lemons?',[0,-1]],
            'lemons':['Oh yes, fresh yellow lemons from my home. My wife picks them. Care to buy any?',[0,0]],
            'yes':['Very good sir. Goodbye',[+1,-2]],
            'no':['Well i\'m sorry to hear that. Have a good day',[-3,-6]],
            'wife':['Oh yes, i love my wife so very much',[+4,0]],
            'home':['it\'s a small house. I dont much care for it',[-1,-1]]}

C1 = nonPlayerCharacter('C1','John','a small man', TalkC1,3, R1)
#jeremy.searchRoom(None)


jeremy.showLocation()
#jeremy.moveRooms("DR1R2")
#jeremy.showLocation()
a = R1.showAllObjectsAndNames()
b = R2.showAllObjectsAndNames()
c = R3.showAllObjectsAndNames()
##print('R1')
##for i in a:
##    print(i)
##print('R2')
##for i in b:
##    print(i)
##print('R3')
##for i in c:
##    print(i)

def Execute(text, player):
    action = {}

    #text in form {'verb':Object,'using/do': object}
    
    error = False

    if 'error' in text:
        error = True
        ui.write(text['error'])
    else:    
        for item in text:
            action[item] = MatchInput({item:text[item]},player)
        ui.write(action)
        
        if error in action:
            error = True
        for key in action:
            if isinstance(action[key],dict):
                error = True
            
    if not error:
        if 'using' not in action:
            action['using'] = None
        allowed = {Place:['search'],
                   Door:['search','open','close','move'],
                   roomFurnishing:['open','close','search'],
                   inventoryObject:['search','using','take','give','equip'],
                   nonPlayerCharacter:['attack','talk'],
                   playerCharacter:['search'],
                   str:['open','search']} # inventory
        
        
        for key in action:
            allow = False
            for thing in allowed:
                if key in allowed[thing] and isinstance(action[key],thing):
                    allow = True
                    
                    if key == 'search'  :
                        
                        if action[key] == player.currentRoom:
                            ui.write('You search the room.')
                            player.SearchRoom()
                        elif action[key] == 'inventory' or action[key] == player:
                            ui.write('You look in your bag.')
                            player.DisplayInventory()
                        else:
                            ui.write('You look closely at the %s.'%action[key].name)
                            player.Inspect(action[key],action['using'])
                            
                    elif key == 'move'  :
                        ui.write('You try to go through the %s.'%action[key].name)
                        player.MoveRooms(action[key].doorID)
                        
                    elif key == 'attack'  :
                        ui.write('You try to attack at the %s!'%action[key].name)
                        action[key].Attack(action['using'])
                        
                    elif key == 'talk'  :
                        ui.write('You try to talk to %s.'%action[key].name)
                        action[key].Talk(action['using'])
                        
                    elif key == 'take'  :
                        ui.write('You try to take the %s.'%action[key].name)
                        player.TakeItem(action[key])
                        
                    elif key == 'open'  :
                        if action[key] == 'inventory':
                            ui.write('You look in your bag.')
                            player.DisplayInventory()
                        else:
                            ui.write('You try to open the %s.'%action[key].name)
                            action[key].Open(action['using'],False)
                            
                    elif key == 'close'  :
                        ui.write('You try to close the %s.'%action[key].name)
                        action[key].Close()

                    elif key =='equip':
                        ui.write('You try to equipt the %s.'%action[key].name)
                        player.EquipItem(action[key])
                    
                    elif key == 'using' and 'act' in action  :
                        action['on'].GeneralUse(action['using']) # This one maybe should be the other way round?
                    elif key == 'using'  :
                        pass
                    elif key == 'act'  :
                        pass
                    else:
                        print('Execute error')

            if not allow and action[key] is not None :
                ui.write('You cannot %s that.'%key)
                        
                            
    else:
        ui.write('You cannot do this.')

##                  disallowed = {'search':False, 'move':False, 'attack':False, 'talk':False, 'open':False, 'close':False, 'using':False, 'act':False,'equip':False,'take':False}
##            if isinstance(action[key],Place):
##                disallowed['search'] = True
##            elif isinstance(action[key], Door):
##                disallowed['open'] = True
##                disallowed['close'] = True
##                disallowed['move'] = True
##            elif isinstance(action[key], roomFurnishing):
##                disallowed['open'] = True
##                disallowed['close'] = True
##                disallowed['search'] = True
##            elif isinstance(action[key], inventoryObject):
##                disallowed['search'] = True
##                disallowed['using'] = True
##            elif isinstance(action[key], nonPlayerCharacter):
##                disallowed['attack'] = True
##                disallowed['talk'] = True
            #we can change these as we see fit, but in terms of solutions this should be fine, right?
                
        
    

def MatchInput(text,player):

    
    #need to add room and player to things
    #look: around, about, room
    #should default to player
    
    room = player.currentRoom
   
    things,inventoryThings = room.showAllObjectsAndNames()
    #print(inventoryThings)
    #print(text,things)
   
    #print()
   # print(text,things)
    things.append([['around','room','about'],[room,room,room]])
    things.append([['self','myself','me'],[player,player,player]])
    things.append([['inventory','bag'],['inventory','inventory']])
    whereLooking = 'sight'
    for key in text:
        if 'my ' in text[key]:
            things = inventoryThings            
            text[key] = text[key].replace('my ','')
            whereLooking = 'your inventory'
        
    similar = ''
    

    action = {}                  

    done = False
    
    #print(things)
        
    for key in text:
        action[key] = ''
        for thingList in things:
            for i in range(len(thingList[0])):
                if text[key] == thingList[0][i]: # if exact match with name
                    action[key] = thingList[1][i]
                    break  #this might not work bug

                elif text[key] in thingList[0][i] and similar == '': #Will catch any matching word
                    action[key] =  thingList[1][i]
                    similar = key
                elif text[key] in thingList[0][i] and similar != '':# Unless more than one object matches
                    action[similar] = ''

    for key in action:
        if action[key] == '':
            break
        else:
            done = True
            return(action[key])
            
      
    if not done:
        for key in action:
            #if key not in ['using','take','give']
            thingType = [] 
            if action[key] == '':
                for thingList in things:
                    for i in range(len(thingList[0])):
                        thingList[0][i] = thingList[0][i].split()
                        if thingList[0][i][-1] in text[key]:
                            thingType.append([key,thingList[1][i],thingList[0][i]])
                            
                        
                            
            if len(thingType)!= 0:
                
                desc = []
                for i in range(len(thingType)):
                    desc.append('')
                    for x in thingType[i][2]:
                        desc[i] += x+' '
                
                if len(thingType) == 1:
                    ui.write('There is only one %s in %s: the %s.'%(thingType[0][2][-1],whereLooking,desc[0])) # This is broken , bug
                    action[thingType[0][0]] = thingType[0][1]
                    return(action[key])
                else:
                    ui.write('There is more than one of these in %s:'%whereLooking)
                    for item in desc:
                        ui.write('There is a %s'%item)
                    return({'error':'Ambiguous object'})
            else:
                ui.write('there is no %s in %s!'%(text[key].split()[-1],whereLooking))
                # Check inventory for object
                invThings = [[],[]]
                invObjects = [[],[]]
                
                for i in range(len(inventoryThings[0][0])):
                    invThings[0].append(inventoryThings[0][0][i].split()[-1])
                    invThings[1].append(inventoryThings[0][1][i])
                    if invThings[0][i] in text[key]:
                        invObjects[0].append(invThings[0][i])
                        invObjects[1].append(invThings[1][i])
                if len(invObjects[0]) == 1:
                    ui.write('There is a %s in your inventory: the %s.'%(invObjects[0][0],invObjects[0][0]))
                    action[key] = invObjects[1][0]
                
                    return(action[key])

                else:         
                    return({'error':'Object not recognised'})
        





def Interpret(text,player):

    text,verbs = Simplify(text)
    

    objVerbs = ['take','give','equip'] # remember to add above too
    objVerb = ''

    verbs.remove('using')
    using = 'using'
    
    currentVerb = ''
    verbNumber=0
    usingNumber=0
    words = text.split()
    do = {}


    for word in words:
        for verb in verbs: # Finds verb in sentence
            if word == verb:
                verbNumber+=1
                do[verb] = ''
                currentVerb = verb
                continue
                
        if word == using: # Finds 'using' in sentence
            usingNumber+=1
            do[using] = ''
            currentVerb = using
            
        if word not in verbs and word != using and currentVerb != '': # The nouns
            if do[currentVerb] == '': #nouns set as values of key being previous verb
                do[currentVerb]+=word
            else:
                do[currentVerb] += ' '+word # add space if not first word

    
    ###---Dirty fix for Use X on Y---###
    
    if usingNumber == 1 and verbNumber == 0 and words[0] == using:
        do['act'] = ''
        temp = do[using].split()
        do[using] = ''
        beforeOn = True
        for word in temp:

            if word == 'on':
                
                beforeOn = False
                
            if word != 'on' and beforeOn:
                if do[using] == '':
                    do[using] +=word
                else:
                    do[using] +=' '+word
            elif word != 'on' and not beforeOn:
                if do['act'] == '':
                    do['act'] +=word
                else:
                    do['act'] += ' '+word
    
        verbNumber+=1

        
    ###---Dirty fix for transfer object to/from X from/to Y---###
    for verb in objVerbs:
        if verb in do:
            objVerb = verb
   
    if objVerb != '' :
        do['to/from'] = ''
        temp = do[objVerb].split()
        do[objVerb] = ''
        beforeTF = True
        for word in temp:
            if word in ['to','from']:
               
                beforeTF = False
                
            if word not in ['to','from'] and beforeTF:
                if do[objVerb] == '':
                    do[objVerb] +=word
                else:
                    do[objVerb] +=' '+word
            elif word not in ['to','from'] and not beforeTF:
                if do['to/from'] == '':
                    do['to/from'] +=word
                else:
                   do['to/from'] += ' '+word
        if do['to/from'] == '':
            del do['to/from']
        
    
    for key in do:
        do[key] = do[key].replace('on ','') # remove garbage word 'on', used in dirty fix
        do[key] = do[key].replace('to ','')
        do[key] = do[key].replace('from ','')
        #do[key] = do[key].replace('in ','')
        if do[key] == '':
            if key == 'act':
                do[key] = 'self'
            else:
                Execute({'error':'What are you trying to %s?'%key},player)
                return()
                
   
    if verbNumber >1 or usingNumber>1:
        Execute({'error':'All that at once?'},player)
    elif verbNumber == 0:
        Execute({'error':'What are you trying to do?'},player)
    else:
        Execute(do,player) #sucess!

                
        
def Simplify(text):
    
    toRemove = []
    fillerWords = ['','in','the','attempt','through','teh','a','try','trying','at','near','for','behind','under','while','and','by','toRemove']
    punctuation = [',','.','?','!','\'',';',':']
             
    using = ['use','using','with','activate','activating','fire','firing','turn','turning']
    
    search = ['search','look','find','explore','inspect','observe','see']
    
    move = ['move','go','travel','walk','climb','enter']
    
    attack = ['attack', 'assault', 'hit', 'smash','fight','kill']
    talk = ['talk','speak','talk to']
    
    take = ['take','grab','remove','carry','obtain','pick up','pick','steal']
    close = ['close','shut','block']
    inspect = []
    
    open_ = ['open', 'unlock','unblock'] #open is keyword, uses open_ instead

    equip = ['equipt','put on','wear','hold']

    

    verbs = ['using','search','move','attack','talk','take','open','close','equip']
    words = {'using':using,'search':search,'move':move,'attack':attack,'talk':talk,'take':take,'open':open_,'close':close,'equip':equip}

    
                
    
        
    text = text.lower()
    text = text.split()
    sentence = ''

    
    for i in range(len(text)):
        for verb in verbs:
            if text[i] in words[verb]: # ***The good bit***
                text[i] = verb  #replaces synonms of verbs with general case of verb from verbs array
            elif i < len(text) -1:
                if text[i] + ' ' + text[i+1] in words[verb]:
                    text[i] = verb
                    text[i+1] = 'toRemove'

        
        if text[i] in fillerWords:
            toRemove.append(text[i]) # get rid of garbage words
            
        if text[i][-1] in punctuation:
            text[i] = text[i][:-1] # get rid of punctuation
            
        
                
    for word in toRemove:
        text.remove(word) #remove garbage words
        
    for word in text:
        sentence+=word+' ' #make array of words into sentence
    
    sentence = sentence[:-1] #remove trailing ' '

    #Special cases
    if sentence in ('inventory','inv'):
        sentence = 'open inventory'
     
    return(sentence,verbs)


 

#TO MOVE ROOMS YOU NEED THE DOOR CODE

main.mainloop()
    
#TODO: Change dialogue for objects so it doesn't sound so weird and ham-fisted by making a location in the room for them to exist in.
#Maybe work on making random descriptors for rooms. 5 senses!
#making sure the program's fully modular to save on work when we make it work with the interpreter
#scavenge from the existing file reader so I can get file reading working here too. I'll probably need multiple files.
#basic gameplay loop will obviously need to be fixed but that's partially Jake's problem, lol

        
