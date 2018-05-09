class Place(object):
    def __init__(self):
        self.doors = []
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array

        self.investigation = []
        #should be of the form [canBeInvestigated, Description, leadsTo]
        #'cept obviously you still get a description if you can't

class gameObject(object):
    def __init__(self, description):
        self.inspectDesc = description
        #a description that displays when you inspect it

        self.usable = []
        #should be of the format [hasUse, Description, leadsTo]
        #once again, there'll probably be two descriptions, but we'll get to that

    def getDesc(self):
        print(self.inspectDesc)
        return self.inspectDesc

class roomFurnishing(gameObject):
    def __init__(self, description):
        super(roomFurnishing, self).__init__(description)

        self.investigation = []
        #as with the place investigation, but on a single furnishing within a room

class inventoryObject(gameObject):
    def __init__(self, description, expendable = [False], taken=["You","You pick up the object"]):
        super(inventoryObject,self).__init__(description)

        self.taken = taken
        #include things about ownership, a description when you pick it up, etc...
        #null it's no-one's

        self.droppable = []
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
    def __init__(self, name, stats, inventory):
        super(playerCharacter,self).__init__(name, stats, inventory)

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
        if item is in self.inventory:
            #can never be too careful
            print("It belongs to" + item.taken[0])
            print(item.inspectDesc)
                
    def displayInventory(self):
        print("You have in your possession: ")
        for item in self.inventory:
            print(item.inspectDesc)
        
    

aSmallRock = inventoryObject("A small rock. It feels oddly warm.", [True, 1])
aLargeRock = inventoryObject("A roughly fist-sized rock. Its heft is reassuring.")
jeremy = playerCharacter("Jeremy", [1,2], [aSmallRock, aLargeRock])
jeremy.displayInventory()
jeremy.useItem(aSmallRock)
jeremy.displayInventory()

    
    

        
