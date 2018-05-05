
#recive input and cut into words
def recive():
    inpt = (input(":") + ".")
    print("You",inpt)
    word=[] 
    k = 0
    for j in range(len(inpt)):
        if inpt[j] == " ":
            word.append(inpt[k:(j)])
            k = j + 1
        elif  j == (len(inpt)-1):
            word.append(inpt[k:(j)])
    return(word)



#take words, find, understand and seperate verbs
def interpret(words):
    j = 0
    while j < len(words)-1:
        if (words[j]+' '+words[j+1]) in phrase:
            words[j] = (words[j]+' '+words[j+1])
            words.remove(words[j+1])
        j+=1
            

    
    print(words)
    world_verb = []
    world_object = []
    
    movement_verb = []
    direction_hold = ""
    direction = []
    dirCount = 0 #not used
    
    used_verb = []
    used_object = []
    
    object_verb = []
    game_object = []
    
    character_verb = []
    character_object = []
    

    additional = []
    itterator = 0
    for item in words:
        for i in range(len(world_actions)):
            if item in world_actions[i]:
                    
                if len(words) == 1:
                    world_verb.append(world_actions[i][0])
                    world_verb.append('surroundings')
                    world_object.append('surroundings')
                    
                elif words[itterator+1] in prepositions and words[itterator+2] not in prepositions:
                    world_verb.append(world_actions[i][0])
                    world_verb.append(words[itterator+2])
                    world_object.append(words[itterator+2])
                    
                elif words[itterator+1] in prepositions and words[itterator+2] in prepositions and words[itterator+3] not in prepositions:
                    world_verb.append(world_actions[i][0])
                    world_verb.append(words[itterator+3])
                    world_object.append(words[itterator+3])
                    
                elif words[itterator + 1] not in prepositions:
                    world_verb.append(world_actions[i][0])
                    world_verb.append(words[itterator+1])
                    world_object.append(words[itterator+1])
                    
                else:
                    next
                    


        
        for i in range(len(movement_actions)):
            if item in movement_actions[i]:
                if words[itterator+1] in prepositions and words[itterator+2] not in prepositions:
                    movement_verb.append(movement_actions[i][0])
                    movement_verb.append(words[itterator+2])
                    direction_hold = (words[itterator+2])
                    
                elif words[itterator+1] in prepositions and words[itterator+2] in prepositions and words[itterator+3] not in prepositions:
                    movement_verb.append(movement_actions[i][0])
                    movement_verb.append(words[itterator+3])
                    direction_hold = (words[itterator+3])
                    
                elif words[itterator + 1] not in prepositions:
                    movement_verb.append(movement_actions[i][0])
                    movement_verb.append(words[itterator+1])
                    direction_hold = (words[itterator+1])
                    
                else:
                    next


                
        for i in range(len(use_actions)):
            if item in use_actions[i]:
                if (len(words) - words.index(item)) < 3:
                    used_verb.append(use_actions[i][0])
                    used_verb.append(words[itterator+1])
                    used_object.append(words[itterator + 1])
                elif words[itterator + 1] not in prepositions and words[itterator+1] not in key_words[3][0]:
                    
                    if (len(words) - words.index(item)) > 2 and words[itterator + 2] in prepositions and words[itterator + 3] not in prepositions and not any(words[itterator+3] in sublist for sublist in key_words[2])and not any(words[itterator+3] in sublist for sublist in key_words[4]):
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+1])
                        used_object.append(words[itterator+1])
                        game_object.append(words[itterator+3])
                    elif (len(words) - words.index(item)) > 3 and words[itterator + 3] in prepositions and words[itterator + 4] not in prepositions and not any(words[itterator+4] in sublist for sublist in key_words[2])and not any(words[itterator+4] in sublist for sublist in key_words[4]):
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+1])
                        used_object.append(words[itterator+1])
                        game_object.append(words[itterator+4])
                    else:
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+1])
                        used_object.append(words[itterator + 1])
                        
                elif words[itterator+1] in prepositions and words[itterator+2] not in prepositions and words[itterator+2] not in key_words[3][0]:
                    
                    if  (len(words) - words.index(item)) > 3 and words[itterator + 3] in prepositions and words[itterator + 4] not in prepositions and not any(words[itterator+4] in sublist for sublist in key_words[2])and not any(words[itterator+4] in sublist for sublist in key_words[4]):
                        print(4.1)
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+2])
                        used_object.append(words[itterator+2])
                        game_object.append(words[itterator+4])
                    elif (len(words) - words.index(item)) > 4 and words[itterator + 4] in prepositions and words[itterator + 5] not in prepositions and not any(words[itterator+5] in sublist for sublist in key_words[2])and not any(words[itterator+5] in sublist for sublist in key_words[4]):
                        print(4.2)
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+2])
                        used_object.append(words[itterator+2])
                        game_object.append(words[itterator+5])
                    else:
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+2])
                        used_object.append(words[itterator+2])
                        
                elif words[itterator+1] in prepositions and words[itterator+2] in prepositions and words[itterator+3] not in prepositions and words[itterator+3] not in key_words[3][0]:
                    
                    if  (len(words) - words.index(item)) > 4 and words[itterator + 4] in prepositions and words[itterator + 5] not in prepositions and not any(words[itterator+5] in sublist for sublist in key_words[2])and not any(words[itterator+5] in sublist for sublist in key_words[4]):
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+3])
                        used_object.append(words[itterator+3])
                        game_object.append(words[itterator+5])
                    #might break
                    elif  (len(words) - words.index(item)) > 5 and words[itterator + 5] in prepositions and words[itterator + 6] not in prepositions and not any(words[itterator+6] in sublist for sublist in key_words[2])and not any(words[itterator+6] in sublist for sublist in key_words[4]):
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+3])
                        used_object.append(words[itterator+3])
                        game_object.append(words[itterator+6])
                    else:
                        used_verb.append(use_actions[i][0])
                        used_verb.append(words[itterator+3])
                        used_object.append(words[itterator + 3])
                    
                
                    
                else:
                    next

        for i in range(len(object_actions)):
            if item in object_actions[i]:
                if words[itterator+1] in prepositions and words[itterator+2] not in prepositions:
                    object_verb.append(object_actions[i][0])
                    object_verb.append(words[itterator+2])
                    game_object.append(words[itterator+2])
                    
                elif words[itterator+1] in prepositions and words[itterator+2] in prepositions and words[itterator+3] not in prepositions:
                    object_verb.append(object_actions[i][0])
                    object_verb.append(words[itterator+3])
                    game_object.append(words[itterator + 3])
                    
                elif words[itterator + 1] not in prepositions:
                    object_verb.append(object_actions[i][0])
                    object_verb.append(words[itterator+1])
                    game_object.append(words[itterator + 1])
                    
                else:
                    next


        for i in range(len(character_actions)):
            if item in character_actions[i]:
                if words[itterator+1] in prepositions and words[itterator+2] not in prepositions:
                    character_verb.append(character_actions[i][0])
                    character_verb.append(words[itterator+2])
                    character_object.append(words[itterator+2])
                    
                elif words[itterator+1] in prepositions and words[itterator+2] in prepositions and words[itterator+3] not in prepositions:
                    character_verb.append(character_actions[i][0])
                    character_verb.append(words[itterator+3])
                    character_object.append(words[itterator + 3])
                    
                elif words[itterator + 1] not in prepositions:
                    character_verb.append(character_actions[i][0])
                    character_verb.append(words[itterator+1])
                    character_object.append(words[itterator + 1])
                    
                else:
                    next

                        
##        for k in range(len(all_directions)): #combine with movement
##            if item in all_directions[k]:
##                direction.append(item)
##                dirCount +=1
##
        
        
        additional.append(item)
        itterator +=1

        
    if direction_hold in all_directions:
        direction.append(direction_hold)
    elif len(direction_hold) > 1:
        direction.append(direction_hold)
        

    
        
    
    if len(game_object) > 0 and len(used_object) > 0:
        print('Use %s on %s' %(used_object,game_object))
    elif len(character_object) > 0 and len(used_object) > 0:
        print('Use %s on %s' %(used_object,character_object))
    elif len(game_object) == 0 and len (used_object) > 0:
        print('Use ', used_object)
    if len(world_object) > 0 and len(world_verb) > 0:
        print('%s the %s' %(world_verb[0],world_object))
    if len(character_object) > 0 and len(character_verb) > 0:
        print('%s the %s' %(character_verb[0],character_object))
    print(" ")
        
    
        
    instruction = [world_verb, world_object, movement_verb, direction, used_verb, used_object, object_verb, game_object, character_verb, character_object, additional]
    return(instruction)






#two word verbs
phrase = ['look around', 'take cover', 'pick up', 'look at', 'talk to',]



prepositions = ['the','teh', 'to','too' 'a','at','near','for','in','on','behind','under'] #'with' clash use[]
#self actions?

search = ['search','look','find','explore','look around'] #2 look around ect not at
hide = ['hide self','take cover','hide']#2 more
world_actions = [search,hide]

move = ['move','go','travel','walk',]
movement_actions = [move]


take = ['take','grab','remove','carry','obtain','pick up','pick']#2
open_ = ['open', 'unlock','unblock']
close = ['close','shut','block']
inspect = ['inspect','look at']#2
object_actions = [take,open_,close,inspect]

use=['use','with','try','activate','fire','using']
use_actions = [use]

attack = ['attack', 'assault', 'hit', 'smash','fight','kill']
talk = ['talk','speak','talk to'] #more
character_actions = [attack, talk]

all_directions = ['north','east','south','west','up','down','in','out','into','leave','forward','backward'] # add places?

key_words = [world_actions, movement_actions,object_actions, use_actions, character_actions]
print(" ")
print(" ")
received = recive()
interpreted = interpret(received)
print(interpreted)
