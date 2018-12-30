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
        elif letter.lower() in "s":
             translation = translation + "9"
        elif letter.lower() in "d":
              translation = translation + "2"
        elif letter.lower() in "e":
              translation = translation + "π"
        else:
              translation = translation + letter
     return translation
print (encryptor(input("enter a phrase to encrypt: ")))
