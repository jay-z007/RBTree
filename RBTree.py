
BLACK = 0
RED = 1

class Node(object):
	"""docstring for Node"""
	def __init__(self, color, data, left=None, right=None, parent=None):
		super(Node, self).__init__()
		self.color = color
		self.data = data 
		self.left = left
		self.right = right
		self.parent = parent

	def __repr__(self):
		#return "\033[1;31;40m ", self.data
		return str(self.data)+str(self.color)

class RBTree(object):
	"""docstring for RBTree"""
	def __init__(self, root=None):
		super(RBTree, self).__init__()
		self.root = root

	def insert(self, data):

		def BST_insert(root, new_node):
			if root == None:
				return new_node

			elif new_node.data < root.data:
				root.left = BST_insert(root.left, new_node)				
				root.left.parent = root

			elif new_node.data > root.data:
				root.right = BST_insert(root.right, new_node)
				root.right.parent = root
			
			return root

		node = Node(RED, data)
		self.root = BST_insert(self.root, node)
		
		self.fix_violations(self.root, node)# not working

	def delete(self, data):
		pass

	#check params
	# if pass by value doesnt work return the new parent
	def rotate_left(self, root, node):
		pass

	def rotate_right(self, root, node):
		pass

	def level_order_traverse(self, q=[]):
		if self.root == None:
			return
		else:
			q.append(self.root)
			
			while len(q) != 0:
				temp_node = q.pop()
				print temp_node,
				if temp_node.left is not None : q.append(temp_node.left)
				if temp_node.right is not None : q.append(temp_node.right)


	def fix_violations(self, root, node):

		def swap(item1, item2):
			temp = item1
			item1 = item2
			item2 = temp

		while node is not root and node.color is not BLACK and node.parent.color is RED:
			parent = node.parent
			grandparent = node.parent.parent

			# Case A - parent is left child of grandparent
			if parent is grandparent.left:
				uncle = grandparent.right
				
				# Case 1 - Uncle is red
				if uncle is not None and uncle.color is RED:
					uncle.color = BLACK
					parent.color = BLACK
					grandparent.color = RED
					node = grandparent
				else:
					# Case 2 - X is the right child of the parent
					if node is parent.right:
						self.rotate_left(root, parent)
						node = parent
						parent = node.parent

					# Case 3 - X is the left child of the parent
					self.rotate_right(root, grandparent)
					swap(parent.color, grandparent.color)
					node = parent

			# Case B - parent is right child of grandparent
			else:
				uncle = grandparent.left

				# Case 1 - Uncle is red
				if uncle is not None and uncle.color is RED:
					uncle.color = BLACK
					parent.color = BLACK
					grandparent.color = RED
					node = grandparent
				else:
					# Case 2 - X is the left child of the parent
					if node is parent.left:
						self.rotate_right(root, parent)
						node = parent
						parent = node.parent

					# Case 3 - X is the right child of the parent
					self.rotate_left(root, grandparent)
					swap(parent.color, grandparent.color)
					node = parent

		root.color = BLACK					


# def main():
# 	rbtree = RBTree()
# 	rbtree.insert(7)
# 	rbtree.insert(6)
# 	rbtree.insert(5)
# 	rbtree.insert(4)
# 	rbtree.insert(3)
# 	rbtree.insert(2)
# 	rbtree.insert(1)

# 	rbtree.level_order_traverse()

# if __name__ == '__main__':
# 	main()

"""
Node* BSTInsert(Node* root, Node *pt)
{
    /* If the tree is empty, return a new node */
    if (root == NULL)
       return pt;
 
    /* Otherwise, recur down the tree */
    if (pt->data < root->data)
    {
        root->left  = BSTInsert(root->left, pt);
        root->left->parent = root;
    }
    else if (pt->data > root->data)
    {
        root->right = BSTInsert(root->right, pt);
        root->right->parent = root;
    }
 
    /* return the (unchanged) node pointer */
    return root;
}
"""