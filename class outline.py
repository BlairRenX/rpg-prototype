class Place(object):
    def __init__(self):
        self.doors = []
        #should be of the format [canBeEntered, Description, leadsTo]
        #and because a room can have multiple doors, it'll be a 2D array

        self.investigation = []
        #should be of the form [canBeInvestigated, Description, leadsTo]
        #'cept obviously you still get a description if you can't

class gameObject(object):
    def __init__(self):
        self.inspectDesc = ""
        #a description that displays when you inspect it

        self.usable = []
        #should be of the format [hasUse, Description, leadsTo]
        #once again, there'll probably be two descriptions, but we'll get to that

class roomFurnishing(gameObject):
    def __init__(self):
        super(roomFurnishing, self).__init__()

        self.investigation = []
        #as with the place investigation, but on a single furnishing within a room

class inventoryObject(gameObject):
    def __init__(self):
        super(inventoryObject,self).__init__()

        self.taken = []
        #include things about ownership, a description when you pick it up, etc...

        self.droppable = []
        #removing itself from the bag, and so on...
        

        
