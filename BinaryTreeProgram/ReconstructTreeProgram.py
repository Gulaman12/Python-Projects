"""Angelo Terminez (ater906)"""
from ListBinaryTree import ListBinaryTree 
def buildTree(inorder,preorder):
	preorderLetterList = []
	inorderLetterList = []
	for letter in preorder: #converts input into list of each letter
		preorderLetterList += [letter]
	for letter in inorder: #converts input into list of each letter
		inorderLetterList += [letter]
	#then i make variables for root, left subtree & right subtree
	root = preorderLetterList[0]
	inorder_left_subtree = inorderLetterList[:inorderLetterList.index(root)]
	preorder_right_subtree = preorderLetterList[len(inorder_left_subtree)+1:]
	
	binary_tree = ListBinaryTree(root)#root
	if len(inorder_left_subtree) > 1: #inserts 2 values left subtree only at left child side , if more then it will insert values at right child side
		binary_tree.insert_value_left(inorder_left_subtree[-1])
		left_root_node = binary_tree.get_left_subtree()
		if left_root_node.get_left_subtree() == None:
			left_root_node.insert_value_left(inorder_left_subtree[0])
		for each in range(len(inorder_left_subtree)-2,0,-1):
			left_root_node = binary_tree.get_left_subtree()
			insert_right = left_root_node.get_left_subtree()
			insert_right.insert_value_right(inorder_left_subtree[each])
	else:
		if len(inorder_left_subtree) == 0: #will execute line if left subtree has no value or 1 value, if value 1 will inserts left node
			binary_tree.get_left_subtree() == None
		else:
			binary_tree.insert_value_left(inorder_left_subtree)

	if len(preorder_right_subtree) >3: #will get the subtree(left&right) of the right node
		subtree_right = len(preorder_right_subtree)//2
		r_subtree_left = preorder_right_subtree[:subtree_right]
		r_subtree_right= preorder_right_subtree[subtree_right:]
		print(r_subtree_left)
		print(r_subtree_right)

		binary_tree.insert_value_right(r_subtree_left[0]) #inserts left child & right child the of right node
		right_root_node = binary_tree.get_right_subtree()
		if right_root_node.get_left_subtree() == None:
			right_root_node.insert_value_left(r_subtree_left[1])
			right_root_node.insert_value_right(r_subtree_right[0])
		for each in range(len(r_subtree_left)-1,1,-1): # for the left subtree of right node, if left subtree has 2 or more values it will add them to the right child side
			insert_right = right_root_node.get_left_subtree()
			insert_right.insert_value_right(r_subtree_left[each])

		right_root_node_lvl2 = right_root_node.get_right_subtree() #for the right subtree of right node, will add all values left child side of except the last value which is added right child side
		if right_root_node_lvl2.get_right_subtree() == None:
			right_root_node_lvl2.insert_value_right(r_subtree_right[len(r_subtree_right)-1])
		for each in range(len(r_subtree_right)-2,0,-1):
			right_root_node_lvl2.insert_value_left(r_subtree_right[each])
	else: #will execute line if right node has no value less than 4 values, if value 1 will insert right node, if 2 will insert left child for right node, if 3 will insert both left/right for right node
		if len(preorder_right_subtree) == 0:
			binary_tree.get_right_subtree() == None
		elif len(preorder_right_subtree) <=3 and len(preorder_right_subtree) >1:
			binary_tree.insert_value_right(preorder_right_subtree[0])
			right_root_node = binary_tree.get_right_subtree()
			right_root_node.insert_value_left(preorder_right_subtree[1])
			if len(preorder_right_subtree) ==3:
				right_root_node.insert_value_right(preorder_right_subtree[2])
		else:
			binary_tree.insert_value_right(preorder_right_subtree)
	print(binary_tree)#prints tree in list form

def main(): 
	print("Binary Tree reconstructed by ater906:")
	inorder_input = input("Please enter the inorder squence: ") #Inorder Input Examples: Hello105, eesrTreaaebt
	preorder_input = input("Please enter the preorder squence: ") #Inorder Input Examples: leHol105, Treesarebeat
	buildTree(inorder_input,preorder_input)
main()