""" A library management system that allows user to borrow, return, search and display the list of books in the libraries system
    Author: Angelo Terminez (ater906) NetId: 8782051
"""

import datetime


# This function displays the introduction part of the main menu.
def display_main_intro():
	message = "-"*16 + " A Simple Library Program " + "-"*16
	print(message)

# This function displays the introduction part of the submenu.
def display_sub_intro():
	message = "-"*20 + " Lending Services " + "-"*20
	print(message)

# This function displays the separator between the menus.
def display_separator():
	lines = "-" * 58
	print(lines)

# This function displays the top level menu.
def display_main_menu():
	display_separator()
	print("1. Lending Services")
	print("2. Display All Books")
	print("3. Show Borrowing Records")
	print("4. Exit System")
	display_separator()

# This function displays the second level menu of lending.
def display_sub_menu():
	display_separator()
	print("1. Search a Book")
	print("2. Borrow a Book")
	print("3. Return a Book")
	print("4. Back to Main")
	display_separator()

# This function loads the book information from a file into a list.
# @param filename - the name of the input file
# @return - the list of books
def load_books(filename):
	infile = open(filename, "r")
	books_str = infile.read()
	infile.close() # Close the input file    
	books_list = books_str.split("\n")
	return books_list

# This function obtains the required attribute value of a book.
# @param item_list - the list contians the information of one book record. 
#		 option - 0 refers to the book code, 1 refers to the book title, 
#				  2 refers the upi status, and 3 refers to the due date.
# @return - the specific attribute value.
def get_attribute(item_list, option):
	if option == 0:
		attribute = item_list[0]
	elif option == 1:
		attribute = item_list[1]
	elif len(item_list) > 2 and option == 2:
		attribute = item_list[2]
	elif len(item_list) > 2 and option == 3:
		attribute = item_list[3]
	else:
		attribute = ""
	return attribute

# This function finds a book record from the list of books based on a given attribute value.
# @param books_list - the list of books. 
#		 option - 0 refers to the book code, 1 refers to the book title, 
#				  2 refers the upi status, and 3 refers to the due date.
#		 value - the value of the attribute to be found.
# @return - the index of the matching book record inside the list of books; 
#			it returns -1, if not found.
def find_book(books_list, option, value):
	index = 0
	found = False
	while not found and index < len(books_list):
		item = books_list[index]
		item_list = item.split(",")
		attribute = get_attribute(item_list, option)
		if attribute == value:
			found = True
		index = index +1
	if found:
		return index-1
	else:
		return -1

# This function obtains a valid book code from the user input. If an invalid code was
# provided, the function will continue asking for a valid book code until it gets one.
# @param books_list - the list of books.
# @return - the index of the matching book item inside the list of books.
def input_code(books_list):
	code = input("Enter book code: ")
	index = find_book(books_list, 0, code)
	while index == -1:
		print("Invalid book code.")
		code = input("Please try again: ")
		index = find_book(books_list, 0, code)
	return index

# This function calculates the due date of a borrowing, based on today's date plus 4 weeks (28 days).
# @return - the due date in a string of the format dd/mm/yyyy.
def get_due_date():
	duedate = datetime.date.today()+datetime.timedelta(days=28)
	date = duedate.strftime("%d/%m/%Y")
	return date

# This function changes upi status and date fields of a book record.
# @param books_list - the list of books.
#		 index - the index of the book record.
#		 upi - UPI of the borrower; if not borrowed, it stores "".
#		 date - return date of the borrowing; if not borrowed, it stores "".
def update_status(books_list, index, upi, date):
	item = books_list[index]
	item_list = item.split(",")
	new_item = item_list[0]+","+item_list[1]
	if (len(item_list) <= 2 and upi!=""):
		new_item =  new_item + "," + upi + ","+date
	books_list[index] = new_item
	

# This function obtains a valid menu option from the user input. If an invalid option was
# provided, the function will continue asking for a valid menu index until it gets one.
# @param start - the start value of the menu index.
#		 end - the end value of the menu index.
# @return - the menu index value.
def get_user_input(start,end):
	choice = int(input("Enter your choice: "))
	while (choice >end or choice < start):
		print("Invalid menu option.")
		choice = int(input("Please try again: "))
	return choice

# This function manages the top level menu.
def main_menu(books_list):
	display_main_menu()
	option = get_user_input(1,4)
	while option != 4:
		if option == 1:
			sub_menu(books_list)
			display_main_menu()
		elif option == 2:
			display_books(books_list)
		else:
			display_borrowing(books_list)
		option = get_user_input(1,4)
	print("Thank you for reading with us.")

# This function manages the second level menu on lending.
def sub_menu(books_list):
	display_sub_menu()
	option = get_user_input(1,4)
	while option != 4:
		if option == 1:
			search_book(books_list)
		elif option == 2:
			borrow_book(books_list)
		else:
			return_book(books_list)
		option = get_user_input(1,4)
	print("Back to main menu.")

# This function displays one book record in the required format.
def display_a_book(book):
	item_list = book.split(",")
	print("Code: " + item_list[0])
	print("Title: " + item_list[1])
	if len(item_list) > 2:
		print("Status: On Loan")
		print("Return Date: "+item_list[3])
	else:
		print("Status: Available")

# This is the main function of the libray system.
def main():
	books_list = load_books("books.txt")
	display_separator()
	display_main_intro()
	main_menu(books_list)
	display_separator()
	save_books(books_list, "books2.txt")

#################################################################################################
# The implementation of the above functions have already been given.                            #
# Please DO NOT MODIFY the content of the ABOVE functions, as they are used by other functions. #
# Please given the implementation of the following six functions to complete the program.       #
#################################################################################################

# This function displays all the books in the collection.
def display_books(books_list):
	## IMPLEMENT THIS METHOD
	display_separator()
	print ("List of books in collection")
	display_separator()
	separator = 24 * "*"
	for item_list in books_list:
		display_a_book(item_list)
		print (separator)
	display_separator()

# This function processes the searching of a book based on an input book title.	
def search_book(books_list):
	## IMPLEMENT THIS METHOD
	prompt = input("Enter the book title to search: ")
	book_title_searched = find_book(books_list, 1, prompt)
	if book_title_searched != -1: 
		print("Record found in the collection:")
		display_a_book(books_list[book_title_searched])
		display_separator()
	else:
		print ("Sorry, this book is not in the collection.")
		display_separator()
# This function processes the borrowing of a book based on the input book code.
def borrow_book(books_list):
	## IMPLEMENT THIS METHOD
	prompt = input_code(books_list)
	borrowing_book = books_list[prompt]
	split_prompt = borrowing_book.split(",")
	if prompt != -1:
		if len(split_prompt) != 4:
			print ("The book - \'", split_prompt[1], "\' is available.", sep = "")
			enter_upi = input("Enter the UPI to borrow: ")
			return_date = get_due_date()
			print ("Due date for returning the book is:", return_date)
			update_status(books_list, prompt, enter_upi, return_date)
		else:
			print ("Sorry, the book - \'", split_prompt[1], "\' is on loan. ", sep = "")
			print ("It will be returned by", split_prompt[3])
		display_separator()
	else:
		print ("Invalid book code.")
		try_again = input("Please try again: ")


# This function processes the returning of a book based on the input book code.
def return_book(books_list):
	## IMPLEMENT THIS METHOD
	prompt = input_code(books_list)
	returning_book = books_list[prompt]
	split_prompt = returning_book.split(",")
	if prompt != -1:
		if len(split_prompt) == 4:
			update_status(books_list, prompt, split_prompt[2], split_prompt[3])
			print ("Thank you for returning the book - \'", split_prompt[1],"\'.", sep = "")
			display_separator()
		else:
			print ("The book - \'", split_prompt[1], "\' has not been borrowed.", sep = "")
			display_separator()
	else:
		print ("Invalid book code.")
		try_again = input("Please try again: ")

# This function displays the borrowing records based on an input UPI.
def display_borrowing(books_list):
	## IMPLEMENT THIS METHOD
	prompt = input("Enter the UPI to retrieve: ")
	upi_value = 0
	search = find_book(books_list,2, prompt)
	if search != -1:
		for i in range(len(books_list)):
			book_index = books_list[i]		
			split_book_index = book_index.split(",")
			if len(split_book_index) == 4:
				attribute = get_attribute(split_book_index,2)
				if attribute == prompt:
					display_a_book(book_index)
					print (24 * "*")
					upi_value +=1
		print ("There are ",upi_value ," books borrowed by ", prompt, ".", sep = "")
	else:
		print ("There is no record of books borrowed by ", prompt, ".", sep = "")		
	display_separator()

# This function saves all the book records into a file.
# @param books_list - the list of books.
# 		 filename - the name of the file to be saved into.
def save_books(books_list, filename):
	## IMPLEMENT THIS METHOD
	output_file = open(filename, "w")
	new_book_list = books_list
	for i in range(len(new_book_list)):
		output_file.write(str(new_book_list[i])+"\n")
	output_file.close()

main()