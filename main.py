from words import words
import random
import string
dificultad = 0
def get_valid_word():
   #words
   word=random.choice(words)
   while '-' in word or ' ' in word or '_' in word or '.'in word:
       word=random.choice(words)
   return word.upper()

opcion = input ("Que dificultad quieres? Facil 6 vidas - Normal 3 vidad - Dificil 1 vida ").lower()

if opcion == 'facil':
    dificultad = 6
elif opcion == 'normal':
    dificultad = 3
elif opcion == 'dificil':
    dificultad = 1    

def play():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = dificultad

    print("     _")                                             
    print("    | |")                                            
    print("    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")  
    print("    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ ")
    print("    | | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                        __/ | ")                     
    print("                       |___/")
    print("")

    print("[DEVELOPER] The word is:", word)
    print("[USER] The word is: ","_ " * len(word_letters),'\n')


    while len(word_letters) > 0 and lives > 0:
        # getting user input
        print("You have",lives,"left and you have have used these letters:",
        ' '.join(used_letter)
        )

        # letter_list = ""
        # for letter in word:
        #     if letter in used_letter:
        #         letter_list += letter + " "
        #     else:
        #         letter_list += '_ '

        letter_list = [letter if letter in used_letter else '_' for letter in word]

        print("Current word:",' '.join(letter_list),'\n')


        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letter: # Si la letra que introduce es valida

            used_letter.add(user_letter) # Agregala a las letras usadas
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("You lose a live, the letter is not in the word LOL")
        elif user_letter in used_letter:
            print("You have already the letter, try again")
        else:
            print("Invalid character.Please try again")

    if lives == 0:
        print("You lose, the word was:", word)
        opc=input("Did you want to play again? Yes|No  ").lower()
        if (opc == "yes"):
                print(play())
        elif  (opc == "no"):
            exit()
        else:
             print('Invalid Character')
    else:
        print("You won, the word is", word)
        opc=input("Did you want to play again? Yes|No  ").lower()
        if (opc == "yes"):
            print (play())
        elif  (opc == "no"):
            exit()
        else:
            print('Invalid Character')
print(play())


