import random

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
            print(door.viewDoors())
            
    def setDoors(self, otherRooms):
        for otherRoom in otherRooms:
            self.doors.append(Door("D" + self.name + otherRoom.name, self, otherRoom))

    def describeRoom(self):
            
        roomDescription = ""
        roomDescription += "The room is " + self.search[0] + ". "
        randomSense = random.randint(0,3)
        #randomSense = 3
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
        print(roomDescription)
            
        
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
        print(self.basicDesc)
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
    def __init__(self, name, stats, inventory, startingRoom):
        self.name = name
        self.inventory = inventory
        self.currentRoom = startingRoom
        #an array of inventory objects

        self.stats = stats
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
    def __init__(self, name, dialogue, stats, startingRoom):
        super(nonPlayerCharacter,self).__init__(name, stats, inventory, startingRoom)

        self.dialogue = dialogue
        #some sample dialogue for whatever reason

class playerCharacter(Character):
    def __init__(self, name, stats, inventory, startingRoom):
        super(playerCharacter,self).__init__(name, stats, inventory, startingRoom)
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
            print("This " + item.objName + " belongs to " + item.taken[0] + ".")
            print(item.inspectDesc)

    def takeItem(self, item):
        if item.taken[0] == "No-one" or item.taken[0] == "you":
            item.taken[0] = "you"
            self.inventory.append(item)
            #will need to remove it from the room, too
            print(item.taken[1])
        else:
            print("That's not yours.")

    def dropItem(self, item):
        if item.droppable == False:
            print("You need this object for something.")
        else:
            self.inventory.remove(item)
            currentRoom.objects.append(item)
                
    def displayInventory(self):
        print("You have in your possession: ")
        for item in self.inventory:
            print(item.basicDesc)

    def moveRooms(self, door):
        #self.currentRoom.doors[door]
        for aDoor in self.currentRoom.doors:
            if aDoor.name == door:
                self.currentRoom = aDoor.room2
                
    def showLocation(self):
        print(self.currentRoom.search[0])

    def searchRoom(self):
        print(self.currentRoom.describeRoom())
            
aSmallRock = inventoryObject("a small rock", "a small rock", "hard stone")
chestOfDrawers = roomFurnishing("a chest of drawers", "a weathered wooden chest of 4 drawers.")
        
R1 = Place("R1", 3, [chestOfDrawers], [aSmallRock], ["a simple yet comfortable bedroom"])
R2 = Place("R2",[],[], ["a lavishly decorated mezzanine"], ["a painting of yourself"])
R3 = Place("R3",[], [aSmallRock])

R1.setDoors([R2])
R2.setDoors([R1, R3])
R3.setDoors([R2])
R1.showDoors()
R2.showDoors()
R3.showDoors()

jeremy = playerCharacter("jeremy", [1,2], [], R1)

jeremy.searchRoom()

#jeremy.showLocation()
#jeremy.moveRooms("DR1R2")
#jeremy.showLocation()


#TO MOVE ROOMS YOU NEED THE DOOR CODE


    
#TODO: Change dialogue for objects so it doesn't sound so weird and ham-fisted by making a location in the room for them to exist in.
#Maybe work on making random descriptors for rooms. 5 senses!
#making sure the program's fully modular to save on work when we make it work with the interpreter
#scavenge from the existing file reader so I can get file reading working here too. I'll probably need multiple files.
#basic gameplay loop will obviously need to be fixed but that's partially Jake's problem, lol

        
