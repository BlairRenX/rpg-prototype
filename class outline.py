class Place(object):
    def __init__(self):
        self.doors = []
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array

        self.investigation = []
        #should be of the form [canBeInvestigated, Description, leadsTo]
        #'cept obviously you still get a description if you can't

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
        
    

aSmallRock = inventoryObject("small rock","A small rock. It feels oddly warm.", "A roughly oval stone. Its smooth surface has been polished.", [True, 1])
aLargeRock = inventoryObject("fist-sized stone", "A roughly fist-sized rock. Its heft is reassuring.",
                             "A jagged stone that has been chipped down to a rough-hewn point. It could easily be made into a spear.")
jeremy = playerCharacter("Jeremy", [1,2], [aLargeRock])
jeremy.inspectItem(aLargeRock)

jeremy.takeItem(aSmallRock)

print("\n")

jeremy.displayInventory()
print("\n")
jeremy.inspectItem(aSmallRock)



    
    

        
