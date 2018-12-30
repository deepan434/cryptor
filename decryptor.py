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
        elif letter in "@":
             translation = translation + "u"
        elif letter in "9":
             translation = translation + "s"
        elif letter in "2":
              translation = translation + "d"
        elif letter in "π":
              translation = translation + "e"
        else:
              translation = translation + letter
     return translation
print (decryptor(input("enter the encrypted phrase to decrypt: "$
