
# solution 
def serialize(self, root):
    ret = []
	queue = [root]

	while queue:
		if queue.count(None) == len(queue):
			break
		node = queue.pop(0)
		if node == None:
			ret.append('#')
		else:
			nxtLeft = node.left if node.left else None
			nxtRight = node.right if node.right else None
			queue += [nxtLeft, nxtRight]
			ret.append('%d' % node.val)

	return ','.join(ret)
    

def deserialize(self, data):
    if not data:
		return None
	data = data.split(',')

	queue = [TreeNode( int(data.pop(0)) )]
	root = queue[-1]
	left = True
	while data:
		nxt = data.pop(0)
		node = None if nxt == '#' else TreeNode( int(nxt) )
		if node:
			queue.append(node)
		if left:
			queue[0].left = node
		else:
			queue[0].right = node
			queue.pop(0)
		left = not left

	return root
