def interpret(text):

    text = simplify(text)

    verbs = ['search','move','attack','talk','take','open','close','inspect']
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
        do['on'] = ''
        temp = do[using].split()
        do[using] = ''
        beforeOn = True
        for word in temp:
            if word != 'on' and beforeOn:
                do[using] +=word
                beforeOn = False
            elif word != 'on' and not beforeOn:
                if do['on'] == '':
                    do['on'] +=word
                else:
                    do['on'] += ' '+word
        verbNumber+=1
    ###---End---###

    for key in do:
        do[key] = do[key].replace('on ','') # remove garbage word 'on', used in dirty fix
        if do[key] == '':
            return({'error':'no specified subject of %s'%key})
        
    if verbNumber >1 or usingNumber>1:
        return({'error':'mulitple commands detected'})
    elif verbNumber == 0:
        return({'error':'no command detected'})
    else:
        return(do) #sucess!
    
                    
        
def simplify(text):
    
    toRemove = []
    fillerWords = ['to','in','the','attempt','teh','from','a','try','trying','at','near','for','behind','under','while','and','by','my','around']
    punctuation = [',','.','?','!','\'',';',':']
             
    using = ['use','using','with','activate','activating','fire','firing','turn','turning']
    
    search = ['search','look','find','explore','look around']
    
    move = ['move','go','travel','walk','go over','climb']
    
    attack = ['attack', 'assault', 'hit', 'smash','fight','kill']
    talk = ['talk','speak','talk to']
    
    take = ['take','grab','remove','carry','obtain','pick up','pick','steal']
    close = ['close','shut','block']
    inspect = ['inspect','look at']
    
    open_ = ['open', 'unlock','unblock'] #open is keyword, uses open_ instead

    verbs = ['using','search','move','attack','talk','take','open','close','inspect']
    words = {'using':using,'search':search,'move':move,'attack':attack,'talk':talk,'take':take,'open':open_,'close':close,'inspect':inspect}
                
    
        
    text = text.lower()
    text = text.split()
    sentence = ''
    
    for i in range(len(text)):
        if text[i] in fillerWords:
            toRemove.append(text[i]) # get rid of garbage words
            
        if text[i][-1] in punctuation:
            text[i] = text[i][:-1] # get rid of punctuation
            
        for verb in verbs:
            if text[i] in words[verb]: # ***The good bit***
                text[i] = verb  #replaces synonms of verbs with general case of verb from verbs array
                
    for word in toRemove:
        text.remove(word) #remove garbage words
        
    for word in text:
        sentence+=word+' ' #make array of words into sentence
        
    sentence = sentence[:-1] #remove trailing ' '
     
    return(sentence)




while True:
  
    print('\n')
    do = interpret(input('Type: '))
    print(do)

    verb = ''
    using = ''
    if 'on' in do:
        print('You use the %s on the %s'%(do['using'],do['on']))
    elif 'error' not in do:
        for key in do:
            if key == 'using':
                using = ' ' + key + ' the ' + do[key]
            elif key == 'move':
                verb = key +' to the '+ do[key]
            else:
                verb = key +' the '+ do[key]
        
        print('You try to ' + verb + using)
    
        



    

