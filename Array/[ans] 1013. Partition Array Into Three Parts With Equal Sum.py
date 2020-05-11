from typing import List

# attempt 1 (after looking at ans): wrong
def canThreePartsEqualSum(A: List[int]) -> bool:
	avg = sum(A) // 3
	part = 0
	count = 0
	
	for n in A:
		part += n
		
		if part == avg:
			count += 1
			part = 0
	
	if count == 3: return True	# does not consider count may be higher than 3 and still be valid if avg is 0
	else: return False

# example that proves the part above is flawed
[10,-10,10,-10,10,-10,10,-10]