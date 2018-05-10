def interpret(text):
    text = text.lower()
    words = text.split()
    verbs = []
    nouns = []
    use = []
    on = None
    gW = ['to','in','the','teh','from','a','at','near','for','on','behind','under']
    using = ['use','with','try','activate','fire','using','turn']
    for word in words:
        if word in gW:
            next
        else:
            if on == None:
                if word in using:
                    on ='using'
                    next
                else:
                    on = 'verb'
                    verbs.append(word)
                    next
            else:
                if on == 'using':
                    on = None
                    use.append(word)
                    next
                if on == 'verb':
                    on = None
                    nouns.append(word)

    if len(use) > 0:
        return('%s %s using %s'%(verbs[0],nouns[0],use[0]))
    else:
        return('%s %s'%(verbs[0],nouns[0]))
                    
        



while True:
    print('\n')
    print(interpret(input('Type: ')))
