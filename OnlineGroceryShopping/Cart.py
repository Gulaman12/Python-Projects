#By Angelo Terminez (ater906)
from Item import Item

class Cart:
	# the constructor
	def __init__(self):
		self.__items = []
	
	# This function gets the number of items in the shopping cart.
	def get_size(self):
		return len(self.__items)

	# This function adds an item into the shopping cart.
	def add_item(self, item):
		if item.getQuantity() > 0:
			print("Item -", item.getDescription(), "is added to the shopping cart.")
			item.setQuantity(item.getQuantity() - 1)
			x = Item(item.getCode(),item.getDescription(),item.getPrice(),item.getQuantity())
			self.__items += [x]
		else:
			print("Sorry, item", item.getCode(), "is out of stock.")
			print("Please select a different item.")

	
	# This function finds an item on sale based on the item code.
	def find_item(self, code):
		for item in self.__items:
			if item.getCode() == code:
				return item
			else:
				return None


	# This function removes an item from the shopping cart.
	def delete_item(self, item):
		if item != None:
			item.setQuantity(item.getQuantity() + 1)
			print("Item -" ,item.getDescription(), "is removed from the shopping cart.")
			for each in range(len(self.__items)):
				if item == self.__items[each]:
					self.__items.pop(each)
		else:
			print("No such item in the cart!")

    # This function clears everything in the shopping cart.
	def discard_all(self):
		for item in self.__items:
			item.setQuantity(item.getQuantity() + 1)
			self.__items.pop()
		print("All items are removed from the shopping cart")
	
	# This function prints out the items bought and calculates the total amount due.
	def check_out(self):
		quantity = 0
		for item in self.__items:
			item_price = item.getPrice()
			quantity += item_price
			print(item.getDescription() +" / $"+str(item.getPrice()))
		for each in range(len(self.__items)):
			self.__items.pop()
		return quantity
