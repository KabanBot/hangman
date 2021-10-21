from words import words
import random
import string
from colorama import init, Fore
init()

def get_valid_word():
   #words
   word=random.choice(words)
   while '-' in word or ' ' in word or '_' in word or '.'in word:
       word=random.choice(words)
   return word.upper()


def play():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 6

    print(Fore.GREEN + "\n ~ J U E G O ~ D E L ~ A H O R C A D O ~")
    print(Fore.BLUE + "\n[DEVELOPER] The word is:",word)
    print(Fore.WHITE + "[USER] The word is: ","_ " * len(word_letters),'\n')


    while len(word_letters) > 0 and lives > 0:
        # getting user input
        print(Fore.LIGHTMAGENTA_EX + "\nYou have",lives,"left and you have have used these letters:",
        ' '.join(used_letter)
        )

        # letter_list = ""
        # for letter in word:
        #     if letter in used_letter:
        #         letter_list += letter + " "
        #     else:
        #         letter_list += '_ '

        letter_list = [letter if letter in used_letter else '_' for letter in word]

        print(Fore.CYAN + "Current word:",' '.join(letter_list),'\n')


        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letter: # Si la letra que introduce es valida

            used_letter.add(user_letter) # Agregala a las letras usadas
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(Fore.RED + "\nYou lose a live, the letter is not in the word LOL")
        elif user_letter in used_letter:
            print(Fore.WHITE+"\nYou have already the letter, try again")
        else:
            print(Fore.RED +"\nInvalid character.Please try again")

    if lives == 0:
        print(Fore.RED + "\nYou lose, the word was:", word)
    else:
        print(Fore.CYAN + "\nYou won, the word is", word,"!!! 😁")



print(play())


