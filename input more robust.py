def interpret(text):

    text = simplify(text)

    allVerbs = ['using','search','move','attack','talk','take','open','close','inspect']


    words = text.split()
    do = {}

    for word in words:
        for verb in allVerbs:
            if word == verb:
                do[verb] = ''
                currentVerb = verb
                continue
        if word not in allVerbs:
            do[currentVerb]+=word

    return(do)
    
                    
        
def simplify(text):
    
    toRemove = []
    fillerWords = ['to',',','.','in','the','teh','from','a','at','near','for','on','behind','under','while','and','by','my','around']
    
             
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
    print(interpret(input('Type: ')))

