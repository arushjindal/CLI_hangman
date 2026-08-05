import os
import subprocess

word = "cradle"
wroguel = 7
diag = "_______\n|       \n|       \n|       \n|       \n|____________\n\n"
domain = "abcdefghijklmnopqrstuvwxyz"
availletters = []
for letter in domain: 
    availletters.append(letter)
prev_guessresult = ""
     
gameover = False
hangman_indices = [14, 23, 32, 31, 33, 40, 42]


def check_compw():
    out = True
    for letter in word:
        if letter in availletters:
            out = False
            break

def draw_hangman():
    print(diag)


def edit_hangman():
    global wroguel
    global diag
    index = 6 - wroguel
    hangman_index = hangman_indices[index]
    if wroguel == 6:
        diag = diag[0:hangman_index] + ("|") + diag[hangman_index + 1:]
    if wroguel == 5:
        diag = diag[0:hangman_index] + ("O") + diag[hangman_index + 1:]
    if wroguel == 4:
        diag = diag[0:hangman_index] + ("|") + diag[hangman_index + 1:]
    if wroguel == 3:
        diag = diag[0:hangman_index] + ("/") + diag[hangman_index + 1:]
    if wroguel == 2:
        diag = diag[0:hangman_index] + ("\\") + diag[hangman_index + 1:]
    if wroguel == 1:
         diag = diag[0:hangman_index] + ("/") + diag[hangman_index + 1:]
    if wroguel == 0:
        diag = diag[0:hangman_index] + ("\\") + diag[hangman_index + 1:]



    



def word_display():
    print("\nYour Word:")
    for letter in word:
        if letter in availletters: 
            print("_" , end = " ")
        else:
            print(letter , end = " ")
    print("\n")


def letters_available():
    print("Letters Available: ")
    for letter in availletters:
        print(letter + " ", end = "")
    print("\n")



def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


def gameitr():
    global wroguel
    global prev_guessresult
    global gameover
    clear_screen()
    print(prev_guessresult + '\n')
    draw_hangman()
    print ("No. of Wrong Guesses Left :", wroguel)
    word_display()

    if gameover == False:
        letters_available()
        guess = input("Enter your Letter: ")
        if guess in availletters:   
                availletters.remove(guess)


        if guess in word:
            prev_guessresult = "Right Guess!!"
            if check_compw() == True:
                gameover = True
                prev_guessresult = "CONGRATULATIONS!! YOU WON!!"
        else:
            prev_guessresult = "Wrong Guess!!"
            wroguel = wroguel - 1
            edit_hangman()
            if wroguel == 0:
                gameover = True
                prev_guessresult = "!! YOU GOT HUNG :("

def main():
    while True:
        if gameover == True:
            break
        else:
            gameitr()
    gameitr()

main()
