from words import words
import random
import string
from colorama import init, Fore
init()


print("""
INSTRUCCIONES
El objetivo del juego es adivinar una palabra.
1. Debes ir ingresando las letras que crees que forme la palabra.
2. Si aciertas se escriben todas las palabras que contenga la palabra.
3. solamente tienes 6 vidas para terminar el juego.
¡¡SUERTE CON EL JUEGO!!
""")

dificultad = 0
def get_valid_word():
   
   #words
   word=random.choice(words)
   while '-' in word or ' ' in word or '_' in word or '.'in word:
       word=random.choice(words)
   return word.upper()

opcion = input ("Que dificultad quieres? Facil 6 vidas - Normal 3 vidad - Dificil 1 vida: ").lower()

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

    
    print(Fore.CYAN+"     _")                                             
    print(Fore.CYAN+"    | |")                                            
    print(Fore.CYAN+"    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")  
    print(Fore.CYAN+"    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ ")
    print(Fore.YELLOW+"    | | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print(Fore.GREEN+"    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print(Fore.GREEN+"                       __/ | ")                     
    print(Fore.GREEN+"                      |___/")
    
    print(Fore.BLUE + "\n[DEVELOPER] The word is:",word)
    print(Fore.WHITE + "[USER] The word is: ","_ " * len(word_letters),'\n')
    

    while len(word_letters) > 0 and lives > 0:
        # getting user input
        print(Fore.LIGHTMAGENTA_EX +"You have",lives,"left and you have have used these letters:",
        ' '.join(used_letter)
        )

        # letter_list = ""
        # for letter in word:
        #     if letter in used_letter:
        #         letter_list += letter + " "
        #     else:
        #         letter_list += '_ '

        letter_list = [letter if letter in used_letter else '_' for letter in word]

        print(Fore.CYAN+"Current word:",' '.join(letter_list),'\n')


        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letter: # Si la letra que introduce es valida

            used_letter.add(user_letter) # Agregala a las letras usadas
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(Fore.RED +"You lose a live, the letter is not in the word LOL")
        elif user_letter in used_letter:
            print(Fore.WHITE+"You have already the letter, try again")
        else:
            print(Fore.RED +"Invalid character.Please try again")

    if lives == 0:
        print(Fore.RED +"You lose, the word was:", word)
        opc=input("Did you want to play again? Yes|No  ").lower()
        if (opc == "yes"):
                print(play())
        elif  (opc == "no"):
            exit()
        else:
             print(Fore.RED +'Invalid Character')
    else:

        print(Fore.CYAN +"You won, the word is", word)
        opc=input("Did you want to play again? Yes|No  ").lower()
        if (opc == "yes"):
            print (play())
        elif  (opc == "no"):
            exit()
        else:
            print(Fore.RED +'Invalid Character')


print(play())