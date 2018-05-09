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
        for verb in verbs:
            if word == verb:
                verbNumber+=1
                do[verb] = ''
                currentVerb = verb
                continue
            
        if word == using:
            usingNumber+=1
            do[using] = ''
            currentVerb = using
            
        if word not in verbs and word != using and currentVerb != '':
            if do[currentVerb] == '':
                do[currentVerb]+=word
            else:
                do[currentVerb] += ' '+word
            
    if verbNumber >1 or usingNumber>1:
        return({'error':'mulitple commands'})
    else:
        return(do)
    
                    
        
def simplify(text):
    
    toRemove = []
    fillerWords = ['to','in','the','teh','from','a','at','near','for','on','behind','under','while','and','by','my','around']
    punctuation = [',','.','?','!','\'',';',':']
             
    using = ['use','using','with','try','trying','activate','activating','fire','firing','turn','turning']
    
    search = ['search','look','find','explore','look around']
    
    move = ['move','go','travel','walk','go over']
    
    attack = ['attack', 'assault', 'hit', 'smash','fight','kill']
    talk = ['talk','speak','talk to']
    
    take = ['take','grab','remove','carry','obtain','pick up','pick']
    close = ['close','shut','block']
    inspect = ['inspect','look at']
    
    open_ = ['open', 'unlock','unblock']

    verbs = ['using','search','move','attack','talk','take','open','close','inspect']
    words = {'using':using,'search':search,'move':move,'attack':attack,'talk':talk,'take':take,'open':open_,'close':close,'inspect':inspect}
                
    
        
    text = text.lower()
    text = text.split()
    sentence = ''
    
    for i in range(len(text)):
        if text[i] in fillerWords:
            toRemove.append(text[i])
        if text[i][-1] in punctuation:
            text[i] = text[i][:-1]
        for verb in verbs:
            if text[i] in words[verb]:
                text[i] = verb
                
    for word in toRemove:
        text.remove(word)
    for word in text:
        sentence+=word+' '
    sentence = sentence[:-1]
    return(sentence)


while True:
    print('\n')
    do = interpret(input('Type: '))
    for key in do:
        if key == 'using':
            using = ' ' + key + ' the ' + do[key]
        else:
            verb = key +' the '+ do[key]
    print('You try to ' + verb + using)



    

