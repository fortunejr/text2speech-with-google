# Importing required modules
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Creatin the tkinter window
gtt = Tk()
gtt.title('Text-To-Speech')
gtt.geometry('500x400')
gtt.configure(bg='ghost white')
# Adding the tkinter elements
msg = StringVar()
Label(gtt, text='TEXT TO SPEECH', font='arial 25 bold', bg='light blue').pack(side='bottom')
Label(gtt, text='Enter Text', font='arial 15 bold', bg='white smoke').pack(side='top')
entry_msg = Entry(gtt, textvariable=msg, width='50').place(x=20,y=100)

# Defining required funtions
def text2speech():
    Message = msg.get()
    speech = gTTS(text = Message)
    speech.save('gtts.mp3')
    playsound('gtts.mp3')

def exitgtt():
    gtt.destroy()

def reset():
    msg.set('')

# Creation and assignment of buttons
Button(gtt, text='PLAY', font='arial 15 bold', command=text2speech, width='4').place(x=25,y=140)
Button(gtt, text='RESET', font='arial 15 bold', command=reset, width='5').place(x=90,y=140)
Button(gtt, text='EXIT', font='arial 15 bold', command=exitgtt, width='4', bg = 'red').place(x=175,y=140)

# Executing of the window
gtt.mainloop()
