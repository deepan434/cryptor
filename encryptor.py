def encryptor(phrase):
     translation =" "
     for letter in phrase:
        if letter.lower() in "a":
            translation = translation + "€"
        elif letter.lower() in "b":
             translation = translation + "&"
        elif letter.lower() in "i":
             translation = translation + "¥"
        elif letter.lower() in "o":
             translation = translation + "£"
        elif letter.lower() in "u":
             translation = translation + "@"
        elif letter.lower() in "q":
             translation = translation + "9"
        elif letter.lower() in "d":
              translation = translation + "2"
        elif letter.lower() in "e":
              translation = translation + "π"
           
        elif letter.lower() in "c":

              translation = translation + "8"

        elif letter.lower() in "f":

              translation = translation + "#"

        elif letter.lower() in "g":

              translation = translation + "$"

        elif letter.lower() in "h":

              translation = translation + "ww"

        elif letter.lower() in "j":

              translation = translation + "0"

        elif letter.lower() in "k":

              translation = translation + "("

        elif letter.lower() in "l":

              translation = translation + "}"

        elif letter.lower() in "m":

              translation = translation + "5"

        elif letter.lower() in "n":

              translation = translation + "!"

        elif letter.lower() in "p":

              translation = translation + "?"

        elif letter.lower() in "r":

              translation = translation + "3"

        elif letter.lower() in "s":

              translation = translation + "["

        elif letter.lower() in "t":

              translation = translation + "{"

        elif letter.lower() in "v:

              translation = translation + ")"
 
        elif letter.lower() in "w":

              translation = translation + "6"

        elif letter.lower() in "x":

              translation = translation + "]"

        elif letter.lower() in "y":

              translation = translation + "7"

        elif letter.lower() in "z":

              translation = translation + "4"
        else:
              translation = translation + letter
     return translation
print (encryptor(input("enter a phrase to encrypt: ")))
