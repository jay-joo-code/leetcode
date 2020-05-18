

# solution
def isValidBST(self, root: TreeNode, floor: bool = float('-inf'), ceiling: bool = float('inf')) -> bool:
	if not root: return True
	
	if root.val <= floor or root.val >= ceiling:
		return False
	
	return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)