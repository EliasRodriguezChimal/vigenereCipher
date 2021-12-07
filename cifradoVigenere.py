# Cifrado Vigenere - Elías Rodríguez Chimal - 201730966
# Vigenere Cipher - Elias Rodriguez Chimal - 201730966

from tkinter import *
from tkinter import messagebox as MessageBox
import base64

root = Tk()

#Function to encrypt the string using the shift specified within the UI
def cifrar(cadena, shift):
    if cadena!="":
        listaCadCifrada = ""

        for i in range(len(cadena)):
            listaCadCifrada += chr(abs(ord(cadena[i]) + (ord(shift[i%len(shift)])%256)))

        

        resultText = Text(root, height=1, borderwidth=0)
        resultText.insert(1.0, listaCadCifrada)
        resultText.place(x=150, y=160)
        resultText['fg'] = 'white'
        resultText['background'] = '#0e0e0e'
        resultText.configure(state='disabled')

        buttonDes = Button(root, text="Descifrar texto", padx = 4, pady = 4, command = lambda: descifrar(listaCadCifrada, shift, 200, resultText, 1))
        buttonDes.place(x=150,y=240)

    else:
        MessageBox.showwarning('Atención', 'El campo "palabra clave" debe ser una cadena y ningún campo puede estar vacío.')


#Function to decrypt the string using the inverse process to 'encrypt' function.
def descifrar(cadena, shift, yPos, label, int):
    if cadena!="":
        listaCadDescifrada = ""

        for i in range(len(cadena)):
            listaCadDescifrada += chr(abs(ord(cadena[i]) - (ord(shift[i%len(shift)])%256)))

        resultText = Text(root, height=1, borderwidth=0)
        resultText.insert(1.0, listaCadDescifrada)
        resultText.place(x=150, y=yPos)
        resultText['fg'] = 'white'
        resultText['background'] = '#0e0e0e'

        buttonClean = Button(root, text="Limpiar campos", padx = 4, pady = 4, command = lambda: clean(resultText, label, int, buttonClean))
        buttonClean.place(x=425,y=yPos+40)

    else:
        MessageBox.showwarning('Atención', 'El campo "palabra clave" debe ser una cadena y ningún campo puede estar vacío.')

#Function to clean all the fields from the UI and let us introduce new data.
def clean(cadena, label, opc, buttonClean):
    if (opc==1):
        inputField.delete(0, 'end')
        shiftField.delete(0, 'end')
        cadena.destroy()
        label.destroy()
        buttonClean.destroy()
    else:
        inputFieldDes.delete(0, 'end')
        shiftFieldDes.delete(0, 'end')
        cadena.destroy()
        buttonClean.destroy()


#All the code related to the UI design.

root.geometry("820x500")
root['background'] = '#0e0e0e'

title = Label(root, text="CIFRADO VIGENERE")
title.place(x=370, y=10)
title['fg'] = 'white'
title['background'] = '#0e0e0e'

subtitle1 = Label(root, text="Cifrado y descifrado")
subtitle1.place(x=370, y=40)
subtitle1['fg'] = 'white'
subtitle1['background'] = '#0e0e0e'

inputFieldText = Label(root, text="Ingrese la cadena a cifrar: ")
inputFieldText.place(x=10, y=80)
inputFieldText['fg'] = 'white'
inputFieldText['background'] = '#0e0e0e'

inputField = Entry(root, width=100, borderwidth=4)
inputField.place(x=175, y=80)
inputField['fg'] = 'white'
inputField['background'] = '#0e0e0e'
inputField['highlightcolor'] = 'white'
inputField['highlightthickness'] = 1
inputField['highlightbackground'] = 'green'

shiftLabel = Label(root, text="Palabra clave: ")
shiftLabel.place(x=475, y=120)
shiftLabel['fg'] = 'white'
shiftLabel['background'] = '#0e0e0e'

shiftField = Entry(root, width=10, borderwidth=4)
shiftField.place(x=715, y=120)
shiftField['fg'] = 'white'
shiftField['background'] = '#0e0e0e'
shiftField['highlightcolor'] = 'white'
shiftField['highlightthickness'] = 1
shiftField['highlightbackground'] = 'green'

text = Label(root, text="La cadena resultante es: ")
text.place(x=10, y=160)
text['fg'] = 'white'
text['background'] = '#0e0e0e'

text2 = Label(root, text="La cadena descifrada es: ")
text2.place(x=10, y=200)
text2['fg'] = 'white'
text2['background'] = '#0e0e0e'

button = Button(root, text="Cifrar texto", padx = 4, pady = 4, command = lambda: cifrar(inputField.get(), shiftField.get()))
button.place(x=10,y=240)

subtitle2 = Label(root, text="Descifrado directo")
subtitle2.place(x=370, y=280)
subtitle2['fg'] = 'white'
subtitle2['background'] = '#0e0e0e'

inputFieldTextDes = Label(root, text="Ingrese la cadena a descifrar: ")
inputFieldTextDes.place(x=10, y=320)
inputFieldTextDes['fg'] = 'white'
inputFieldTextDes['background'] = '#0e0e0e'

inputFieldDes = Entry(root, width=100, borderwidth=4)
inputFieldDes.place(x=175, y=320)
inputFieldDes['fg'] = 'white'
inputFieldDes['background'] = '#0e0e0e'
inputFieldDes['highlightcolor'] = 'white'
inputFieldDes['highlightthickness'] = 1
inputFieldDes['highlightbackground'] = 'green'

shiftLabelDes = Label(root, text="Palabra clave: ")
shiftLabelDes.place(x=475, y=360)
shiftLabelDes['fg'] = 'white'
shiftLabelDes['background'] = '#0e0e0e'

shiftFieldDes = Entry(root, width=10, borderwidth=4)
shiftFieldDes.place(x=715, y=360)
shiftFieldDes['fg'] = 'white'
shiftFieldDes['background'] = '#0e0e0e'
shiftFieldDes['highlightcolor'] = 'white'
shiftFieldDes['highlightthickness'] = 1
shiftFieldDes['highlightbackground'] = 'green'

text = Label(root, text="La cadena resultante es: ")
text.place(x=10, y=400)
text['fg'] = 'white'
text['background'] = '#0e0e0e'

buttonDesD = Button(root, text="Descifrar texto", padx = 4, pady = 4, command = lambda: descifrar(inputFieldDes.get(), shiftFieldDes.get(), 400, text, 2))
buttonDesD.place(x=10,y=440)

creditos = Label(root, text="Creado por: Elías Rodríguez Chimal - 201730966")
creditos.place(x=550, y=440)
creditos['fg'] = 'white'
creditos['background'] = '#0e0e0e'

root.mainloop() 

