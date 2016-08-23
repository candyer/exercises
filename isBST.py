# Given an array, represent a binary tree, start from root. e.g.[1,2,3,4,5]: 
#       1
#      / \
#     2   3
#    / \ 
#   4   5
# return True if this tree is binary search tree, False otherwise.


#solution 1-1  in-order traverse and check if the path is sorted order
def create_node(val):
  return {
      'val': val,
      'left': None,
      'right': None }

def create_tree(array, n=0, memo = None):
  if memo == None: memo = []
  if n >= len(array): return None
  node = create_node(array[n])
  node['left'] = create_tree(array, 2*n+1, memo)
  if node['val'] not in memo:
      memo.append(node['val'])
  node['right'] = create_tree(array, 2*n+2, memo)
  return memo

def isBST(array):
  if len(array) == 0: return True
  path = create_tree(array)
  for i in xrange(len(path)-1):
      if path[i+1] < path[i]:
          return False
  return True

# print isBST([20,19,18]) #False
# print isBST([8,5,11,2,7,10,12,1,3,6]) #True
# print isBST([])



#solution 1-2
def create_node(val):
  return {
      'val': val,
      'left': None,
      'right': None }

def create_tree(array, n=0):
  if n >= len(array): return None
  node = create_node(array[n])
  node['left'] = create_tree(array, 2*n+1)
  node['right'] = create_tree(array, 2*n+2)
  return node

def DFS(node, li=None):
  if li == None: li = []
  if node['left']:
      DFS(node['left'], li)
  li.append(node['val'])
  if node['right']:
      DFS(node['right'], li)
  return li

# a = [8,5,11,2,7,10,12,1,3,6] #True
# a = [7,6,5,4,3] # False
# node = create_tree(a)
# l = DFS(node)
# print all(a < b for a, b in zip(l, l[1:]))




#solution 2  Top-down
def create_node(val):
    return {
        'val': val,
        'left': None,
        'right': None }

def create_tree(array, n=0):
    if n >= len(array): return None
    node = create_node(array[n])
    node['left'] = create_tree(array, 2*n+1)
    node['right'] = create_tree(array, 2*n+2)
    return node

def DFS(node, mini=float('-inf'), maxi=float('inf')):
    if node == None: return True
    if mini < node['val'] < maxi:
        return DFS(node['left'], mini, node['val']) and DFS(node['right'], node['val'], maxi)
    return False

# a = [8,5,11,2,7,10,12,1,3,6] # True
# a = [8,5,11,2,7,10,12,1,3,7] # return False if there's duplicate
# a = [9,8,7,6,5] #False
# print DFS(create_tree(a))




#solution 3  Bottom-Up
def create_node(val):
	return {
		'val': val,
		'left': None,
		'right': None }

def create_tree(array, n=0):
	if n >= len(array): return None
	node = create_node(array[n])
	node['left'] = create_tree(array, 2*n+1)
	node['right'] = create_tree(array, 2*n+2)
	return node

def DFS(node):
	mini = maxi = node['val']
	if node['left']:
		status, mini1, maxi1 = DFS(node['left'])
		mini = mini1
		if status == False: return False, mini, maxi1
		if node['val'] <= maxi1 : return False, mini, maxi1

	if node['right']:
		status, mini2, maxi2 = DFS(node['right']) 
		maxi = maxi2
		if status == False: return False, mini2, maxi
		if node['val'] >= mini2: return False, mini2, maxi
	return True, mini, maxi

# a = [5,2,7,1,3,6] #True
# a = [8,5,11,2,7,10,12,1,3,6] # True
# a = [8,5,11,2,7,10,12,1,3,2] # False
# a = [9,8,7,6,5] #False
# a = [10,8,7,6,9] #False
# a = [10,8,11,6,9] #True
# a = [20,15,25,10,17,22,30,5,12] #True
# a = [20,15,25,10,17,22,30,5,21] #False
# print DFS(create_tree(a))[0]

