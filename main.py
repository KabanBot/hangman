from palabras import words
import random
import string

def get_word():
   #words
   word=random.choice(words)
   while '-' in word or ' ' in word or '_' in word or '.'in word:
       word=random.choice(words)
   return word.upper()
   
#print(get_word())
# palabra=get_word(3)
# print (get_word(3))
# print(palabra)

#Obtener datos random de una lista 

def play():
    word = get_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6

    print(word,word_letters,alphabet,used_letter, sep="\n") 

    print("[DEVELOPER] The word is: ",word)
    print("[USER] The word is: ", " - " * len(word_letters))
    while len(word_letters):
        print ("You have ",lives," left and you have used these letters: "," ".join(used_letter))
        
        letter_list=""
        for letter in word:
            if letter in word_letters:
                letter_list += letter +" "
            else:
                letter_list += "_" 
            
        letter_list = {[letter if letter in used_letter else "-" for letter in word]}

        #getting user input
        user_letter = input("Guess a letter: ").upper()
        if (user_letter in alphabet - used_letter): #Letter is valid
            used_letter.add(user_letter)
            if (user_letter in word_letters):
                word_letters.remove(user_letter)
        elif (user_letter in used_letter):
            print("You have already the letter, try again")
        else:
            print("Invalid character. Please try again")
    
    if (lives == 0):
        print("You lose, the word was: ",word)
    else:
        print("You won, the word is: ",word)