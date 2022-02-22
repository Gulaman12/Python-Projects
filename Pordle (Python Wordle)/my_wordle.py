"""
Python Wordle aka PORDLE by Angelo Terminez
"""
import random
import re
from itertools import zip_longest

def word_files(): 
    words_file = open ('allowed_guesses.txt','r')
    wordle_file = open ('5letter_words.txt','r')
    words_list = []
    wordle_list = []
    for word,wordle in zip_longest(words_file.read().splitlines(),wordle_file.read().splitlines()):
        if wordle != None:
            wordle_list += [wordle]
        words_list += [word]
    words_file.close()
    wordle_file.close()
    return words_list,wordle_list
    
def generate_wordle(wordles): #Creates and returns a random wordle
    random_word = random.choice(wordles)
    return random_word

def valid_guess(words,guess): #Checks if word is an actual word.
    if guess.lower() in words:
        return True
    else:
        return False

def make_guess(attempt,words): #Asks user to guess, validates guess, returns the valid guess
    while True:
        guess = input("Guess " + str(attempt) + ": ")
        if len(guess) == 5 and re.match('^[a-zA-Z]*$',guess) and valid_guess(words,guess):
            break
        else:
            print("Must be a real word. Invalid guess. Try again.")
    return guess

def check_progress(progress): #Checks if user has won game
    win = 0
    for tick in progress:
        if tick == (u'\u2713'):
            win += 1
    return win

def game_table(users_guess,progress,game_board): 
    print("-" * 13)
    progress = " ".join(progress)
    users_guess = " ".join(users_guess)
    game_board += ["| " + users_guess + " |","| " + progress + " |"]
    for each in game_board:
        print(each)
    print("-" * 13)
    result = check_progress(progress)
    return result

def play_game():
    winner = 5
    words,wordles = word_files()
    game_board = []
    wordle = (generate_wordle(wordles)).upper()
    wordle_letters = list(wordle)
    print(wordle)
    print("-" * 21 + "\nLETS GUESS THE WORDLE\n" + "-" * 21)
    for attempt in range(1,7): # You have 6 tries
        progress =[]
        users_guess = list((make_guess(attempt,words)).upper())
        for letter in range(0,len(wordle)):
            if wordle_letters[letter] == users_guess[letter]:
                progress += [(u'\u2713')]
            elif users_guess[letter] in wordle:
                progress += [(u'\u25CF')]
            else:
                progress += [(u'\u00D7')]
        result = game_table(users_guess,progress,game_board)
        if result == winner:
            print('*** Congratulations ! You won ! ***')
            break
        elif result != winner  and attempt == 6:
            print('*** You lose! The Wordle was', wordle ,'***' )
    
def check_prompt(prompt,play_type):
    match prompt:
        case 1:
            play_game()
            play_type = 1 #Ask user with different menu
            display_menu(play_type)
        case 2:
            print(
            '''
                     === HOW TO PLAY PORDLE ===
            The Aim of the Game is to guess the 5 letter
            word within 6 attempts. After each attempt you
            will also be given hints on your progress.
            (\u2713) = means the letter is in the word and
                  in the correct spot
            (\u25CF) = means the letter is in the word but
                  in the wrong spot.
            (\u00D7) = means the letter is not in the word,
                  in any spot.
            ''')
        case 3:
            print("Goodbye.")
            quit()
        case _:
            print("Try again. Please select a valid option number.")

def display_menu(play_type):
    exit = 3
    prompt = ""
    while prompt != exit:
        if play_type == 0:
            print("1. PLAY PORDLE")
            print("2. RULES")
            print("3. EXIT")
        else:
            print("Do you wish to play again?")
            print("1. YES")
            print("2. NO")
        try:
            prompt = int(input("Enter selection: "))
        except ValueError:
            print("Try again. Please select a valid option number.")
            display_menu(play_type)
        if play_type != 0 and prompt == 2:
            check_prompt(exit,play_type)
        check_prompt(prompt,play_type)

play_type = 0
display_menu(play_type)
