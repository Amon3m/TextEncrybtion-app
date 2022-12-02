from tkinter import*
import string
import sys
import re
from tkinter import messagebox

gui_enc =  Tk()
gui_enc.title("Encryption Tool")
gui_enc.geometry('630x490')
gui_enc.resizable(False, False)
gui_enc.configure(background="#23ada6")

##gui-----encryption


plaintext_widget1 = Label(gui_enc, text="Enter the plaintext", height=2, bg="#23ada6", fg="#e91e63",
                          font=('arial', 25, 'bold'), bd=2)

plaintext_widget1.place(x=7, y=80, height=38)

plaintext = StringVar()
plaintext_input1 = Entry(gui_enc, width=30, bd=5, textvariable=plaintext)
plaintext_input1.place(x=35, y=122)

plaintext_widget2 = Label(gui_enc, text="Enter the key a", height=2, bg="#23ada6", fg="#e91e63",
                          font=('arial', 25, 'bold'), bd=5)
plaintext_widget2.place(x=7, y=160, height=38)

key = StringVar()
key_input2 = Entry(gui_enc, width=30, bd=5, textvariable=key)
key_input2.place(x=35, y=210)

plaintext_widget = Label(gui_enc, text="Enter the key b", height=2, bg="#23ada6", fg="#e91e63",
                         font=('arial', 25, 'bold'), bd=5)
plaintext_widget.place(x=7, y=250, height=38)

key2 = StringVar()
key_input2 = Entry(gui_enc, width=30, bd=5, textvariable=key2)
key_input2.place(x=35, y=300)


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


##-----------rail

def rail():
    def main():
        print("RailFenceCipher")

        plaintext_value = plaintext.get().upper()
        print()

        key_1 = int(key.get())
        print()
        cipherText = cipher(plaintext_value, key_1)
        print("Ciphered Text: " + cipherText)
        messagebox.showinfo("Ciphertext : ", "Ciphertext :" + cipherText)
        decipherText = decipher(cipherText, key_1)
        print("Deciphered Text: " + decipherText)

        return

    def cipher(plaintext_value, key_1):
        result = ""

        matrix = [["" for x in range(len(plaintext_value))] for y in range(key_1)]

        increment = 1
        row = 0
        col = 0

        for c in plaintext_value:
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1

            matrix[row][col] = c

            row += increment
            col += 1

        for list in matrix:
            result += "".join(list)

        return result

    def decipher(cipherText, key_1):
        result = ""

        matrix = [["" for x in range(len(cipherText))] for y in range(key_1)]

        idx = 0
        increment = 1

        for selectedRow in range(0, len(matrix)):
            row = 0

            for col in range(0, len(matrix[row])):
                if row + increment < 0 or row + increment >= len(matrix):
                    increment = increment * -1

                if row == selectedRow:
                    matrix[row][col] += cipherText[idx]
                    idx += 1

                row += increment

        matrix = transpose(matrix)
        for list in matrix:
            result += "".join(list)

        return result

    def transpose(m):
        result = [[0 for y in range(len(m))] for x in range(len(m[0]))]

        for i in range(len(m)):
            for j in range(len(m[0])):
                result[j][i] = m[i][j]

        return result

    main()


ceaserenc_ptn =Button (gui_enc,text="ceaser encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=ceaser)
ceaserenc_ptn.place(x=320,y=40)


affineenc_ptn =Button (gui_enc,text="affine encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=affine)
affineenc_ptn.place(x=320 , y= 160)

vigenerenc_ptn =Button (gui_enc,text="vigener encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=veg)
vigenerenc_ptn.place(x=320 , y= 280)

##-------------

RailFenceCipher_ptn=Button (gui_enc,text="RailFence encryption ",height=2, font =("Arial", 20 ),bg ="#e91e63", fg = "white" ,borderwidth=5,command=rail)
RailFenceCipher_ptn.place(x=320 , y= 390)



gui_enc.mainloop()




