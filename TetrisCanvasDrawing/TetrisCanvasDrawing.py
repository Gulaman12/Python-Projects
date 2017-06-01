""" Tessalates four shapes and with each variation of the tessalated shape it will correspond to a blue, red, green or yellow colour
    Author: Angelo Terminez (ater906) NetId: 8782051
"""

from tkinter import *

# ------Draws one of the four different tiles.------
def draw_tile(a_canvas, tile_type, colour_index, left, top, size):
	colours = ["yellow", "red", "green", "blue", "lightblue", "deep pink", "black", "orange", "purple"]
	if tile_type == 0:
		a_canvas.create_rectangle(left,top,left+size,top+(size*2), fill = colours[colour_index], outline = "grey")
		a_canvas.create_rectangle(left+size,top+size,left+(size*3),top+(size*2), fill = colours[colour_index], outline = "grey")
		a_canvas.create_line(left+size,top+size,left+size,top+(size*2), fill = colours[colour_index])
	elif tile_type == 1:
		a_canvas.create_rectangle(left,top,left+(size*2),top+size, fill = colours[colour_index], outline = "grey")
		a_canvas.create_rectangle(left+(size*2),top,left+(size*3),top+(size*2), fill = colours[colour_index], outline = "grey")
		a_canvas.create_line(left+(size*2),top,left+(size*2),top+size, fill = colours[colour_index])
	elif tile_type == 2:
		a_canvas.create_rectangle(left,top,left+(size*2),top+size, fill = colours[colour_index], outline = "grey")
		a_canvas.create_rectangle(left,top+size,left+size,top+(size*3), fill = colours[colour_index], outline = "grey")
		a_canvas.create_line(left,top+size,left+(size*2),top+size, fill = colours[colour_index])
	else:
		a_canvas.create_rectangle(left,top,left+size,top+(size*2), fill = colours[colour_index], outline = "grey")
		a_canvas.create_rectangle(left-size,top+(size*2),left+size,top+(size*3), fill = colours[colour_index], outline = "grey")
		a_canvas.create_line(left,top+(size*2),left+size,top+(size*2), fill = colours[colour_index])

#This function needs to be completed

# ------Process each symbol from a single line (string). ------
def process_single_line(a_canvas, line_of_pattern, left, top, size):
	#This function needs to be completed
	type0 = "blue"
	type1 = "red"
	type2 = "green"
	type3 = "yellow"
	for pattern in range(len(line_of_pattern)):
		tile = line_of_pattern[pattern]
		if tile == str(0):
			a_canvas.create_rectangle(left+(size*pattern),top,left+(size*pattern)+size,top+(size*2), fill = type0, outline = "grey")
			a_canvas.create_rectangle(left+(size*pattern)+size,top+size,left+(size*pattern)+(size*3),top+(size*2), fill = type0, outline = "grey")
			a_canvas.create_line(left+size+(size*pattern),top+size,left+size+(size*pattern),top+(size*2), fill = type0)
		elif tile == str(1):
			a_canvas.create_rectangle(left+(size*pattern),top,left+(size*pattern)+(size*2),top+size, fill = type1, outline = "grey")
			a_canvas.create_rectangle(left+(size*pattern)+(size*2),top,left+(size*pattern)+(size*3),top+(size*2), fill = type1, outline = "grey")
			a_canvas.create_line(left+(size*2)+(size*pattern),top,left+(size*2)+(size*pattern),top+size, fill = type1)
		elif tile == str(2):
			a_canvas.create_rectangle(left+(size*pattern),top,left+(size*pattern)+(size*2),top+size, fill = type2, outline = "grey")
			a_canvas.create_rectangle(left+(size*pattern),top+size,left+(size*pattern)+size,top+(size*3), fill = type2, outline = "grey")
			a_canvas.create_line(left+(size*pattern),top+size,left+(size*2)+(size*pattern),top+size, fill = type2)
		elif tile == str(3):
			a_canvas.create_rectangle(left+(size*pattern),top,left+(size*pattern)+size,top+(size*2), fill = type3, outline = "grey")
			a_canvas.create_rectangle(left+(size*pattern)-size,top+(size*2),left+(size*pattern)+size,top+(size*3), fill = type3, outline = "grey")
			a_canvas.create_line(left+(size*pattern),top+(size*2),left+size+(size*pattern),top+(size*2), fill = type3)

# ------Organise the processing of the pattern. ------ 
def process_pattern(a_canvas, size):
	left = 0
	top = 0
	list_of_lines = get_list_of_pattern_lines("TileMap.txt")
	for line_string in list_of_lines:
		if len(line_string) > 0:
			process_single_line(a_canvas, line_string, left, top, size)
			top += size

# ------Get the list of lines (strings) from the file. ------
def get_list_of_pattern_lines(filename):
	file_to_read = open(filename, "r")
	file_info = file_to_read.read()
	lines_list = file_info.split("\n")
	file_to_read.close()
	return lines_list

# ------Draws the four shapes on the right side of the canvas. ------ 
def draw_four_tiles(a_canvas, left, top, size):
	large_rect = (left, top, left + size * 5, top + size * 15)
	a_canvas.create_rectangle(large_rect, fill="MediumOrchid", outline="blue")
	left += size
	top += size * 2
	draw_tile(a_canvas, 0, 3, left, top, size)
	draw_tile(a_canvas, 1, 1, left, top + size * 5 // 2, size)
	draw_tile(a_canvas, 2, 2, left, top + size * 5, size)
	draw_tile(a_canvas, 3, 0, left + size, top + size * 17 //2, size)

# ------Draws the light blue background grid lines of the given size. ------ 
def draw_grid(a_canvas, size, right_hand_side, bottom):
	for row in range(size, bottom, size):
		a_canvas.create_line(-1, row, right_hand_side + 1, row,fill="lightblue")
		for col in range(size, right_hand_side, size):
			a_canvas.create_line(col, -1, col, bottom + 1, fill="lightblue")

# ------main function. ------
def main():
	size = 20
	canvas_width = 700
	canvas_height = 560
	root = Tk()
	root.title("A4 - ater906")
	geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
	root.geometry(geometry_string)
	a_canvas = Canvas(root)

	a_canvas.config(background="white")
	a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window
	#Draw the light blue background grid lines
	draw_grid(a_canvas, size, canvas_width, canvas_height)

	process_pattern(a_canvas, size)
	draw_four_tiles(a_canvas, canvas_width - size * 6, 40, size)

	root.mainloop()
main()