
# attempt (accepted) after multiple mistakes
def numRollsToTarget(self, d: int, f: int, target: int) -> int:
	prev = [0] + [1 for _ in range(f)] + [0 for _ in range(target-f)]    # first roll
	new = [0 for _ in range(target+1)]
	
	for dice in range(2, d+1): # iter dice. 2, 3
			for t in range(dice, target+1): # 
					for f in range(1, f+1):
							if t-f >= dice-1:
									new[t] += prev[t-f]
			
			prev = new
			new = [0 for _ in range(target+1)]
	
	return prev[-1] % (10 ** 9 + 7)
