"""Angelo Terminez (ater906)"""
def q2(size,values):
	probe_count_list = []
	worst_position_list = []
	capacity = [None] * size #creates the capacitity of hash table
	for key in values: # this will put the values in the hash table
		x = key % size
		if capacity[x] == None:
			capacity[x] = [key]
		else:
			x += 1
			if x > size-1:
				x=0
			while capacity[x] != None:
				if x > size-1:
					x = 0
				x += 1
			capacity[x] = [key]	
	for i in range(len(capacity)):#this will probe each value until it finds None,then add the probe count of each value into probe_count_list
		if capacity[i] == None:
			probe = 0
			probe_count_list += [probe]
		elif capacity[i] != None:
			probe = 0
			position = i
			position += 1
			if position >(size-1):
				position = 0
			while capacity[position-1]!= None:
				if position > (size-1):
					position = 0
				position +=1
				probe +=1
			probe_count_list += [probe]

	worst = max(probe_count_list) # this will give us the highest number in the list (worst count)
	for each in range(len(probe_count_list)): # this give us all the positions that have the highest probe count, then add the positions to worst_position_list
		if probe_count_list[each] == worst:
			worst_position_list += [each]
	
	worst_position_list.sort() # orders list smallest to biggest
	return worst_position_list 

#Example Input
values = [25, 32, 88, 10, 35, 11]
worst = q2(11, values)
print(worst)


