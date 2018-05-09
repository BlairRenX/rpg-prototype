class Place(object):
    def __init__(self, name, furnishings = [], objects = [], search = ["an empty room"], investigation = ["There is nothing of note here."]):
        self.doors = []
        self.name = name
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array
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
    def __init__(self, description, inspectDesc):
        self.basicDesc = description
        #a description that displays when you look at it

        self.inspectDesc = inspectDesc
        #a description that displays when you inspect it

        self.usable = []
        #should be of the format [hasUse, Description, leadsTo]
        #once again, there'll probably be two descriptions, but we'll get to that

    def getDesc(self):
        print(self.basicDesc)
        return self.basicDesc

class roomFurnishing(gameObject):
    def __init__(self, description, inspectDesc):
        super(roomFurnishing, self).__init__(description, inspectDesc)

        self.investigation = []
        #as with the place investigation, but on a single furnishing within a room

class inventoryObject(gameObject):
    def __init__(self, objName, description, inspectDesc, taken=["No-one","You pick up the object."], expendable = [False], droppable=True):
        super(inventoryObject,self).__init__(description, inspectDesc)

        self.objName = objName

        self.taken = taken
        #include things about ownership, a description when you pick it up, etc...

        self.droppable = droppable
        #removing itself from the bag, and so on...

        self.expendable = expendable
        #if it's expendable, and if so, how many uses it has



class Character(object):
    def __init__(self, name, stats, inventory):
        self.name = name
        self.inventory = inventory
        #an array of inventory objects

        self.stats = stats
        #in case we decide to add stats later

    def getName(self):
        return self.name


class nonPlayerCharacter(Character):
    def __init__(self, name, dialogue, stats):
        super(nonPlayerCharacter,self).__init__(name, stats)

        self.dialogue = dialogue
        #some sample dialogue for whatever reason

class playerCharacter(Character):
    def __init__(self, name, stats, inventory, startingRoom):
        super(playerCharacter,self).__init__(name, stats, inventory)
        self.currentRoom = startingRoom
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
            #will need to make it become an object of the room after it's dropped
                
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
            
aSmallRock = inventoryObject("a small rock", "rock...", "hard stone")
        
R1 = Place("R1")
R2 = Place("R2",[],[], ["a lavishly decorated mezzanine"], ["a painting of yourself"])
R3 = Place("R3",[], [aSmallRock])

R1.setDoors([R2])
R2.setDoors([R1, R3])
R3.setDoors([R2])
R1.showDoors()
R2.showDoors()
R3.showDoors()

jeremy = playerCharacter("jeremy", [1,2], [], R1)
jeremy.showLocation()
jeremy.moveRooms("DR1R2")
jeremy.showLocation()


#TO MOVE ROOMS YOU NEED THE DOOR CODE


    
    

        
