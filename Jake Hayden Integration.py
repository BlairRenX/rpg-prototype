import random
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
        if txt != None:
            txt = txt.replace('\n','')

            if txt == 't':
                ui.talkWindow(jeremy,C1)
            txt = self.cleanInput(txt)
            self.cleanOutput()
            txt = txt+'\n'
            for i in txt:
                #Types to the end of textbox with value i
                self.text += i
                self.output.config(text = self.text)

                self.inpt.delete('end-2c','end-1c')
                #sleep for that cool typing effect
                time.sleep(0.03)
                #tkinter is shit
                self.main.update()
            #scrolls output to bottom (without its not possible to scroll at all, its odd)   
            #makes sure input is empt but is currently buggy not sure why, seems to automatically lead with a \n or ' ' weird ass shit

            #jeremy.nextSitch(self.txt)

            self.inpt.delete('0.0','end')
            #disable output so cannot be typed in
        else:
            pass
           
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
                if npc.interest + npc.talk[word][1][0] < 7:
                    npc.interest += npc.talk[word][1][0]
                else:
                    npc.interest = 6
                if npc.interest + npc.talk[word][1][0] < 0:
                    self.write('That seems to have struck a nerve with %s, they turn away. This conversation is clearly over.'%npc.name)
                    self.inConversation  = False
                else:    
                    self.write(npc.name+ ' seems' +self.mood[npc.interest] +'your response')
                    self.write(npc.name+ ':    ' + npc.talk[word][0])
                    self.prevWord = word
                
            if word not in npc.talk:
                if npc.talk[self.prevWord][1][1] != 0:
                    npc.interest += npc.talk[self.prevWord][1][1]
                    if npc.interest >-1:
                        self.write(npc.name+ ' seems' +self.mood[npc.interest] +'your response')
                    else:
                        self.write(npc.name +' has had enough of you. This conversation is clearly over')
                        self.inConversation = False
                else:
                    self.write(npc.name + ' didn\'t understand you, but they didn\'t seem to care. They are still' + self.mood[npc.interest] +'you.')





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

class Place(object):
    def __init__(self, name, quality = 3, furnishings = [], objects = [], search = ["an empty room"], investigation = ["There is nothing of note here."]):
        self.doors = []
        self.name = name
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array
        self.quality = quality
        self.furnishings = furnishings
        self.objects = objects

        self.search = search

        self.investigation = investigation
        #should be of the form [canBeInvestigated, Description, leadsTo]
        #'cept obviously you still get a description if you can't
    def showDoors(self):
        for door in self.doors:
            ui.write(door.viewDoors())
            
    def setDoors(self, otherRooms):
        for otherRoom in otherRooms:
            self.doors.append(Door("D" + self.name + otherRoom.name, self, otherRoom))

    def describeRoom(self):
            
        roomDescription = ""
        roomDescription += "The room is " + self.search[0] + ". "
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
        #print(roomDescription)
        return roomDescription
            
        
class Door(object):
    def __init__(self, name, room1, room2):
        self.name = name
        self.room1 = room1
        self.room2 = room2
##    def setDoors(self):
##        self.room1.doors.append(self)
##        self.room2.doors.append(self)
    def viewDoors(self):
        return("This door connects " + self.room1.search[0] + " and " + self.room2.search[0] + ".")
    def goThrough(self, currentRoom):
        return self.room2
    def goBackThrough(self, currentRoom):
        return self.room1

class gameObject(object):
    def __init__(self, description, inspectDesc, hidden = False):
        self.basicDesc = description
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
    def __init__(self, description, inspectDesc):
        super(roomFurnishing, self).__init__(description, inspectDesc)

        self.investigation = []
        #as with the place investigation, but on a single furnishing within a room

class inventoryObject(gameObject):
    def __init__(self, objName, description, inspectDesc, taken=["No-one","You pick up the object."], expendable = [False], droppable=True, equippable = [False]):
        super(inventoryObject,self).__init__(description, inspectDesc)

        self.objName = objName

        self.taken = taken
        #include things about ownership, a description when you pick it up, etc...

        self.droppable = droppable
        #removing itself from the bag, and so on...

        self.expendable = expendable
        #if it's expendable, and if so, how many uses it has

        self.equippable = equippable
        #if it's a weapon, armour, etc...



class Character(object):
    def __init__(self, name, startingRoom, inventory):
        self.name = name
        self.inventory = inventory
        self.currentRoom = startingRoom
        #an array of inventory objects

        #in case we decide to add stats later

        self.equipped = {
            "clothesTorso" : "Basic synth-cloth shirt",
            "clothesLegs" : "Basic synth-cloth legwear",
            "armwear" : "None",
            "headgear" : "None",
            "footwear" : "Standard boots",
            "armourTorso" : "None",
            "armourLegs" : "None",
            "accessories" : ["None"],
            "weaponLeft" : "None",
            "weaponRight" : "None",
            "weaponBoth" : "None"
            }
        #this is more for a fantasy setting and it hasn't been tested cuz I wrote it at 00:37

    def getName(self):
        return self.name
    


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

    def useItem(self, item):
        #the actual use
        if item.expendable[0] == True:
            if item.expendable[1] == 1:
                self.inventory.remove(item)
            else:
                item.expendable[1] = item.expendable[1] -1
            #if the item's expendable
            #a confirmation message should probably be put in here at some point

    def inspectItem(self,item):
        if item in self.inventory:
            #can never be too careful
            ui.write("This " + item.objName + " belongs to " + item.taken[0] + ".")
            ui.write(item.inspectDesc)

    def takeItem(self, item):
        if item.taken[0] == "No-one" or item.taken[0] == "you":
            item.taken[0] = "you"
            self.inventory.append(item)
            #will need to remove it from the room, too
            ui.write(item.taken[1])
        else:
            ui.write("That's not yours.")

    def dropItem(self, item):
        if item.droppable == False:
            ui.write("You need this object for something.")
        else:
            self.inventory.remove(item)
            currentRoom.objects.append(item)
                
    def displayInventory(self):
        ui.write("You have in your possession: ")
        for item in self.inventory:
            ui.write(item.basicDesc)

    def moveRooms(self, door):
        #self.currentRoom.doors[door]
        for aDoor in self.currentRoom.doors:
            if aDoor.name == door:
                self.currentRoom = aDoor.room2
                
    def showLocation(self):
        ui.write("You are in " + self.currentRoom.search[0])

    def searchRoom(self):
        ui.write(self.currentRoom.describeRoom())

    def talk(self, other):
        ui.talkWindow(self,other)
        
aSmallRock = inventoryObject("a small rock", "a small rock", "hard stone")
chestOfDrawers = roomFurnishing("a chest of drawers", "a weathered wooden chest of 4 drawers.")
        
R1 = Place("R1", 3, [chestOfDrawers], [aSmallRock], ["a simple yet comfortable bedroom"])
R2 = Place("R2",4, [],[], ["a lavishly decorated mezzanine"], ["a painting of yourself"])
R3 = Place("R3",5, [], [aSmallRock])

R1.setDoors([R2])
R2.setDoors([R1, R3])
R3.setDoors([R2])
R1.showDoors()
R2.showDoors()
R3.showDoors()

jeremy = playerCharacter("jeremy", R1)

TalkC1 = {  'start':['Well hello there. Can I interest you in some lemons?',[0,-1]],
            'lemons':['Oh yes, fresh yellow lemons from my home. My wife picks them. Care to buy any?',[0,0]],
            'yes':['Very good sir. Goodbye',[+1,-2]],
            'no':['Well i\'m sorry to hear that. Have a good day',[-3,-6]],
            'wife':['Oh yes, i love my wife so very much',[+4,0]],
            'home':['it\'s a small house. I dont much care for it',[-1,-1]]}

C1 = nonPlayerCharacter('C1','John','a small man', TalkC1,3, R1)
jeremy.searchRoom()
main.mainloop()

jeremy.showLocation()
jeremy.moveRooms("DR1R2")
jeremy.showLocation()


#TO MOVE ROOMS YOU NEED THE DOOR CODE


    
#TODO: Change dialogue for objects so it doesn't sound so weird and ham-fisted by making a location in the room for them to exist in.
#Maybe work on making random descriptors for rooms. 5 senses!
#making sure the program's fully modular to save on work when we make it work with the interpreter
#scavenge from the existing file reader so I can get file reading working here too. I'll probably need multiple files.
#basic gameplay loop will obviously need to be fixed but that's partially Jake's problem, lol

        
