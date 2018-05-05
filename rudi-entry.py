import tkinter as tk
import time
#setup makes main window
def startup():
    global output,main,enterbut,inpt
    
    main = tk.Tk()
    main.geometry("850x700")
    main.config(background ='#111111')

    #Big output text box. Disabled so cannot be typed in.
    #rel-x,y,height,width are relative placement for window
    output = tk.Text(main,state='disabled')
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
    enterbut = tk.Button(main, text='Enter', background = 'light gray', height = 1, command = lambda:( enter(inpt,inpt.get('1.0','end')) ))
    enterbut.place(relx = 0.71, rely = 0.645, relwidth = 0.09)


#write fucntion takes text and the textbox it's from 
def enter(inpt,txt):
    global text
    text = txt
    output.config(state = 'normal')
    for i in txt:
        #Types to the end of textbox with value i
        output.insert('end',i)
        #deletes from end if input box less 2 characters, to end of input box less 1 character
        #(this grabs the last character only as 'end' is the empty space after last character)
        inpt.delete('end-2c','end-1c')
        #sleep for that cool typing effect
        time.sleep(0.03)
        #tkinter is shit
        main.update()
    #scrolls output to bottom (without its not possible to scroll at all, its odd)   
    output.see('end')
    #makes sure input is empt but is currently buggy not sure why, seems to automatically lead with a \n or ' ' weird ass shit
    inpt.delete('0.0','end')
    #disable output so cannot be typed in
    output.config(state = 'disabled')
       
def write(text):
    output.config(state = 'normal')
    inpt.config(state = 'disabled')
    for i in text:
        output.insert('end',i)
        time.sleep(0.05)
        #tkinter is shit
        main.update()
    output.insert('end','\n')   
    output.see('end')
    output.config(state = 'disabled')
    inpt.config(state = 'normal')
    

def displayCurrent():
    global output
    situation = ["You stand in an empty room. There is a door ahead of you and a door behind you", ["Try north door", "Try south door", "Other"]]
    write(situation[0])
    write('\nOptions:')
    for option in situation[1]:
        write(option)
    write('\n')

startup()

displayCurrent()

tk.mainloop()

#Bugs:
# 1) Weird leading space stuff
# 2) Can type \n with enter key when box is empty, tried to fix but tripped up by (1)
# 3) Can type shit when machine is displaying text with write(text,w)
