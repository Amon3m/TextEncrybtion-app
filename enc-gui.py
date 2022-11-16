from tkinter import*
import string
import sys
import re
from tkinter import messagebox

gui_enc =  Tk()
gui_enc.title("Encryption Tool")
gui_enc.geometry('630x390')
gui_enc.resizable(False, False)
gui_enc.configure(background="#23ada6")



##gui-----encryption





plaintext_widget1 = Label(gui_enc,text="Enter the plaintext",height=2,bg ="#23ada6", fg = "#e91e63", font =('arial', 25,'bold'), bd=2)
               
plaintext_widget1.place(x=7, y=50, height=38)


plaintext= StringVar()
plaintext_input1= Entry(gui_enc, width =30 ,bd=5,  textvariable =plaintext)
plaintext_input1.place(x=35, y=92)

plaintext_widget2= Label(gui_enc,text="Enter the key a",height=2,bg ="#23ada6", fg = "#e91e63", font =('arial', 25,'bold'),bd=5)
plaintext_widget2.place(x=7, y=130, height=38)

key= StringVar()
key_input2= Entry(gui_enc, width =30,bd=5 , textvariable =key)
key_input2.place(x=35, y=180)

plaintext_widget = Label(gui_enc,text="Enter the key b",height=2, bg ="#23ada6", fg = "#e91e63", font =('arial', 25,'bold'),bd=5)
plaintext_widget.place(x=7, y=220, height=38)

key2= StringVar()
key_input2= Entry(gui_enc, width =30,bd=5 , textvariable =key2)
key_input2.place(x=35, y=270)

##ceaser------------
def ceaser ():
    import string
    Alphabet = string.ascii_uppercase
    plaintext_value = plaintext.get().upper()
    key_1 = int(key.get())
    Encryption_ceaser = ""
    if key_1>26:
        key_1 %= 26
    for i in range(len(plaintext_value)):
        n=plaintext_value[i]
        index=Alphabet.find(n)
        c = (index+key_1)%26
        Encryption_ceaser += Alphabet[c]
    print( " Encryption ", Encryption_ceaser )
    messagebox.showinfo(" Encryption : "," Encryption : "+Encryption_ceaser )

##affine--------
def affine():
    import string 
    Alphabet=string.ascii_uppercase
    plaintext_value=plaintext.get() .upper()
    key_1=int( key.get())
    key_2=int( key2.get())
    if key_2> 26:
        key_2%26

    Encryption_Affine=""

    for i in range(len(plaintext_value)):
        n=plaintext_value[i]

        index=Alphabet.find(n)
        c=(key_1* index+key_2) %26
        Encryption_Affine +=Alphabet[c]

    for i in range(key_1):
        if key_1==[2,4,6,8,10,12,13,14,16,18,20,22,24]:
            key1=int( key.get())
    print( " Encryption ", Encryption_Affine)    
    messagebox.showinfo(" Encryption : "," Encryption : "+Encryption_Affine )



##veg

def veg():
    def main ():
       plaintext_value=plaintext.get().upper()
       plaintext_value =re.sub("[^A-Z]+","",plaintext_value)
       keyword = key.get().upper()
       key_1 = generateKey(plaintext_value, keyword)
       cipher_text = cipherText(plaintext_value, key_1)
       print("Ciphertext :", cipher_text)
       messagebox.showinfo("Ciphertext : ","Ciphertext :" +cipher_text)

    def generateKey(plaintext_value , key_1):
        key_1 = list(key_1)
        if len(plaintext_value ) == len(key_1):
            return (key_1)
        else:
            for i in range(len(plaintext_value ) -  len(key_1)):
                key_1.append(key_1[i ])
        return ("".join(key_1))


    def cipherText(plaintext_value , key_1):
        cipher_text = []
        for i in range(len(plaintext_value )):
            x = (ord(plaintext_value [i]) +ord(key_1[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return ("".join(cipher_text))


    if __name__ == "__main__":
     main()



ceaserenc_ptn =Button (gui_enc,text="ceaser encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=ceaser)
ceaserenc_ptn.place(x=320,y=40)


affineenc_ptn =Button (gui_enc,text="affine encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=affine)
affineenc_ptn.place(x=320 , y= 160)

vigenerenc_ptn =Button (gui_enc,text="vigener encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=veg)
vigenerenc_ptn.place(x=320 , y= 280)



gui_enc.mainloop()




