
# attempt (accepted)
def generate(self, numRows: int) -> List[List[int]]:
	if numRows == 0: return []
	
	res = [[1]]
	for row in range(2, numRows+1):
		arr = [1] + [None] * (row-2) + [1]
		
		for i in range(row-2):
			arr[i+1] = res[-1][i] + res[-1][i+1]
		res.append(arr)
	return res

def generateAlt(self, numRows: int) -> List[List[int]]:
	# explanation: Any row can be constructed using the offset sum of the previous row. 
	# Example:
	# 	 1 3 3 1 0 
 	# +  0 1 3 3 1
	# =  1 4 6 4 1
	if numRows == 0: return []
	
	res = [[1]]
	for i in range(1, numRows):
		temp1 = res[-1] + [0]
		temp2 = [0] + res[-1]
		res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
	return res[:numRows]