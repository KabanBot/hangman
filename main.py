import palabras 
import random


def get_word():
   #words
   word=random.choice(palabras.words)
   while '-' in word or ' ' in word or '_' in word or '.'in word:
       word=random.choice(palabras.words)
   return word.upper()
   
#print(get_word())
# palabra=get_word(3)
# print (get_word(3))
# print(palabra)

#Obtener datos random de una lista 

def play():
    return "iniciar juego"

print(play())


