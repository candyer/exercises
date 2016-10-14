# make a segment tree that return the sum of an interval
# and the update add one to each element between [begin,end]

from pprint import pprint
def create_node(begin, end):
	return {
		'begin': begin,
		'end': end,
		'left': None,
		'right': None,
		'val': None,
		'sum': None
	}

def build_segtree(array,begin,end):
	if not array: return None
	if begin > end: return None
	node = create_node(begin, end)
	if begin == end:  
		node['val'] = node['sum'] = array[begin-1]
		return node
	mid = (begin + end) / 2
	node['left'] = build_segtree(array, begin, mid)
	node['right'] = build_segtree(array, mid+1, end)
	node['sum'] = node['left']['sum'] + node['right']['sum']
	return node
# pprint(build_segtree([9,2,6,3],1,4))

def update(node, begin, end):
	if node['begin'] > end or node['end'] < begin: return 
	if node['begin'] == node['end']:
		node['val'] += 1
		node['sum'] += 1
		return
	update(node['left'], begin, end)
	update(node['right'], begin, end)
	node['sum'] = node['left']['sum'] + node['right']['sum']
	return

def read_interval(node,begin,end):
    if begin <= node['begin'] and end >= node['end']:
    	return node['sum']
    if begin > node['end'] or end < node['begin']:
    	return 0
    return read_interval(node['left'], begin, end) + read_interval(node['right'], begin, end)



node = build_segtree([9,2,6,3],1,4)
update(node,1,3)
# pprint(node)
print read_interval(node,2,4) #13
print read_interval(node,2,3) #10
print read_interval(node,4,4) #3
print read_interval(node,3,3) #7
