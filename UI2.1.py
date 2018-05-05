import tkinter as tk
import time

#setup makes main window
def startup():
    global output,main,enterbut,inpt,text
    text = ''
    main = tk.Tk()
    main.geometry("850x700")
    main.config(background ='#deface')

    #Big output text box. Disabled so cannot be typed in.
    #rel-x,y,height,width are relative placement for window
    output = tk.Label(main)
    output.place(relx =0.2, rely = 0.02, relheight=0.6, relwidth=0.6)

    #Input box
    #calls 'enter' on key press return/enter key
    inpt =  tk.Text(main, height = 1)
    inpt.bind("<Return>", lambda x: enter(inpt,inpt.get('1.0','end-1c')))
    inpt.place(relx =0.2, rely = 0.65,  relwidth=0.5)
    #enter is called with the .get() which takes from the ext box.
    # 1.0 is line.character, so line-1.position=0
    # end is end if text box, -1c is less 1 character (can be written as -1character)
    # 'end-1c' as oppose to 'end' ommits end \n from typed enter key



    #button that calls 'enter' same as above, save for not having the -1c after 'end' as no \n is typed (hope this makes sense)
    enterbut = tk.Button(main, text='Enter', background = 'light blue', height = 1, command = lambda:( enter(inpt,inpt.get('1.0','end')) ))
    enterbut.place(relx = 0.71, rely = 0.645, relwidth = 0.09)


#write fucntion takes text and the textbox it's from 
def enter(inpt,txt):
    cleanOutput()
    global text
    for i in txt:
        #Types to the end of textbox with value i
        text += i
        output.config(text = text)
        
        inpt.delete('end-2c','end-1c')
        #sleep for that cool typing effect
        time.sleep(0.05)
        #tkinter is shit
        main.update()
    #scrolls output to bottom (without its not possible to scroll at all, its odd)   
    #makes sure input is empt but is currently buggy not sure why, seems to automatically lead with a \n or ' ' weird ass shit
    inpt.delete('0.0','end')
    #disable output so cannot be typed in
    
       
def write(txt):
    global text
    cleanOutput()
    txt+='\n'
    inpt.config(state = 'disabled')
    for i in txt:
        text += i
        output.config(text = text)
        time.sleep(0.05)
        #tkinter is shit
        main.update()
    
    inpt.config(state = 'normal')
    

def cleanOutput():
    global text
    if text.count('\n')>25:
        cutof = text.index('\n')+1
        print(cutof)
        text = text[cutof:]
        #cleanOutput()

        


startup()

write('This is how to just make some text appear.')

tk.mainloop()

#Bugs:
# 1) Weird leading space stuff
# 2) Can type \n with enter key when box is empty, tried to fix but tripped up by (1)
# 3) Can type shit when machine is displaying text with write(text,w)
