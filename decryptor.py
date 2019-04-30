def decryptor(phrase):
     translation =" "
     for letter in phrase:
        if letter.lower() in "€":
            translation = translation + "a"
        elif letter.lower() in "&":
             translation = translation + "b"
        elif letter.lower() in "¥":
             translation = translation + "i"
        elif letter.lower() in "£":
             translation = translation + "o"
        elif letter.lower() in "@":
             translation = translation + "u"
        elif letter.lower() in "9":
             translation = translation + "s"
        elif letter.lower() in "2":
              translation = translation + "d"
        elif letter.lower() in "π":
              translation = translation + "e"
        elif letter.lower() in "8":

              translation = translation + "c"

        elif letter.lower() in "#":

              translation = translation + "f"

        elif letter.lower() in "$":

              translation = translation + "g"

        elif letter.lower() in "w":

              translation = translation + "h"

        elif letter.lower() in "0":

              translation = translation + "j"

        elif letter.lower() in "(":

              translation = translation + "k"

        elif letter.lower() in "}":

              translation = translation + "l"

        elif letter.lower() in "5":

              translation = translation + "m"

        elif letter.lower() in "!":

              translation = translation + "n"

        elif letter.lower() in "?":

              translation = translation + "p"

        elif letter.lower() in "3":

              translation = translation + "r"

        elif letter.lower() in "[":

              translation = translation + "s"

        elif letter.lower() in "{":

              translation = translation + "t"

        elif letter.lower() in ")":

              translation = translation + "v"

        elif letter.lower() in "6":

              translation = translation + "w"

        elif letter.lower() in "]":

              translation = translation + "x"

        elif letter.lower() in "7":

              translation = translation + "y"

        elif letter.lower() in "4":

              translation = translation + "z"

        else:
              translation = translation + letter
     return translation
print (decryptor(input("enter the encrypted phrase to decrypt: ")))
