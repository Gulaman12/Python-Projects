""" A two player game called Coin strip where the aim of the game is to get all the coins ($) to the left most side first. Invalid moves: a move that jumps over another coin
    Author: Angelo Terminez (ater906) NetId: 8782051
"""

import random

def create_game_string():
	game_string = " $ $ $ $ "
	randomize_string = 1
	while randomize_string < 8:
		random_string = jumble_game_line(game_string)
		randomize_string += 1
	return random_string

def jumble_game_line(game_line):
	initial_random_postion_of_coin = random.randrange(1,8,2)
	random_position = random.randrange (0,9)
	if random_position == initial_random_postion_of_coin:
		random_position += 1
	elif random_position == 1:
		random_position += 1
	elif random_position == 3:
		random_position += 1
	elif random_position == 5:
		random_position += 1
	elif random_position == 7:
		random_position += 1
	remove_initial_game_position = game_line[:initial_random_postion_of_coin]+ " " + (game_line[initial_random_postion_of_coin+1:])
	new_randomized_game_line = remove_initial_game_position[:random_position] + "$" + remove_initial_game_position[random_position+1:]
	return new_randomized_game_line

def display_game_string(game_string):
	print ()
	print ("    1     2     3     4     5     6     7     8     9    ")
	game_slots_empty = "||     |     |     |     |     |     |     |     |     ||"
	print (game_slots_empty)
	separator = "  |  "
	game_slots_filled = ("||  " + game_string[0] + separator + game_string[1] + separator + game_string[2] + separator + game_string[3] + \
	 separator + game_string[4] + separator + game_string[5] + separator + game_string[6] + separator + game_string[7] + separator + \
	 game_string[8] + "  ||")
	print (game_slots_filled)
	print (game_slots_empty)
	print ()

def get_user_position_num(player_num):
	player_number = "PLAYER NUMBER:" 
	print (player_number, player_num)
	prompt_1 = int(input("Enter position number: "))
	return prompt_1

def get_num_to_move():
	prompt_2 = int(input("Enter number to move: "))
	return prompt_2

def move_dollar_to_the_left(game_string, position_num, to_move):
	position_number = position_num - 1
	move_left = position_number - to_move
	remove_position_number = game_string[:position_number] + " " + game_string[position_number+1:]
	new_move_position = remove_position_number[:move_left] + "$" + remove_position_number[move_left+1:]
	return new_move_position

def get_next_player_num(player_num):
	next_player = player_num
	if next_player == 1:
		next_player +=1
	elif next_player ==2:
		next_player = next_player - 1
	return next_player

def congratulate_player(player_num):
	congratulatory_message = "** Y O U H A V E W O N **"
	length_of_border = len(congratulatory_message) * "="
	winner_of_player_number = "     PLAYER NUMBER: " + str(player_num)
	print ()
	print (length_of_border)
	print (congratulatory_message)
	print (winner_of_player_number)
	print (congratulatory_message)
	print (length_of_border)
	print ()

def display_menu():
	option_1 = "1. PLAY COIN STRIP"
	option_2 = "2. EXIT"
	print (option_1)
	print (option_2)
	prompt = int(input("Enter selection: "))
	if prompt == 1:
		return True
	else:
		return False

# CHECK IF THE GAME HAS FINISHED
def check_game_finished(game_string):
		 first_four_symbols = game_string[0:4]
		 if first_four_symbols == "$$$$":
					return True
		 return False
# PLAY ONE GAME OF COIN STRIP
def play_one_game():
		 player_num = 1
		 game_finished = False
		 game_string = create_game_string()
		 while game_finished == False:
					display_game_string(game_string)
					position_num = get_user_position_num(player_num)
					move_num = get_num_to_move()
					game_string = move_dollar_to_the_left(game_string,
																position_num, move_num)
					game_finished = check_game_finished(game_string)
					if game_finished:
							 display_game_string(game_string)
							 congratulate_player(player_num)
					else:
							 player_num = get_next_player_num(player_num)

def main():
	while display_menu () == True:
		play_one_game()
	print()
	print("BYE FROM COIN STRIP")
	
main()