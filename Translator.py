#Giraffe Language
#All vowels become G
#-------------------

#For example:
#Dog = Dgg
#cat = cgt

def translate(phrase):
    translation = " "#empty string.
    for letter in phrase:
        if letter in "AEIOUaeiou": #a better way to type this is letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))