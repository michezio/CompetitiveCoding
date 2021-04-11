global dp
dp = dict()

import copy

class Node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = []

	def addParent(self, parent):
		self.parent = parent

	def addChild(self, child):
		self.children.append(child)
		child.addParent(self)

	def removeLeaf(self, leaf):
		self.children.remove(leaf)

	def removeSelf(self):
		self.parent.removeLeaf(self)

	def isLeaf(self):
		return len(self.children) == 0

	def getKthParent(self, k):
		if (self, k) in dp.keys():
			return dp[(self, k)]
		if self.parent == None and k > 0:
			return 0
		elif k == 0:
			return self.value
		else:
			result = self.parent.getKthParent(k-1)
			dp[(self, k)] = result
			return result

	'''
	def getKthParent(self, k):
        if self.parent == None and k > 0:
            return 0
        parent = copy.copy(self.parent)
        k -= 1
        while k > 0:
            if (parent, k) in dp.keys():
                return dp[(parent,k)]
            parent = copy.copy(parent.parent)
            if parent == None and k > 0:
                dp[(parent,k)] = 0
                return 0
            k -= 1
        dp[(parent,k)] = parent.value
        return parent.value
    '''

tree = dict()

TEST = int(input())
for _ in range(TEST):
	nodes_n = int(input())
	for _ in range(nodes_n):
		x, y = map(int, input().split())
		if y == 0:
			root = Node(x)
			tree[x] = root
		else:
			node = Node(x)
			tree[x] = node
			tree[y].addChild(node)
	queries_n = int(input())
	for _ in range(queries_n):
		query = list(map(int, input().split()))
		#print("QUERY: ", *query)
		if query[0] == 0:
			_, y, x = query
			node = Node(x)
			tree[x] = node
			tree[y].addChild(node)
		elif query[0] == 1:
			_, x = query
			leaf = tree[x]
			leaf.removeSelf()
			tree.pop(x, None)
		elif query[0] == 2:
			_, x, k = query
			if x in tree.keys():
				kth = tree[x].getKthParent(k)
				print(kth)
			else:
				#print("Not Found")
				print(0)