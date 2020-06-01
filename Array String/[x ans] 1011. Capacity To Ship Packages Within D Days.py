
# attempt (wrong)
def shipWithinDays(self, weights: List[int], D: int) -> int:
	# even if mid's count == D
	# need to set high = mid and iterate
	# to find potentially lower capacity
	# with the same number of count (number of ships)
	low, high = max(weights), sum(weights)
	
	while low < high:
			mid = low + (high - low) // 2
			
			count = 1
			weight = 0
			
			for x in weights:
					weight += x
					
					if weight > mid:
							weight = x
							count += 1
			
			if count == D:	# wrong part
					return mid
			elif count > D:
					low = mid
			elif count < D:
					high = mid
	
	return low

# retrospective attempt
def shipWithinDays(weights, D):
	low, high = max(weights), sum(weights)

	while low < high:
		mid = (low + high) // 2
	

# solution (accepted)
def shipWithinDaysSolution(weights, D):
	#  binary search
	low, high = max(weights), sum(weights)

	while low < high:
		# guess the capacity of ship
		# as value between low and high
		# hence binary search
		mid = (low+high)//2

		#----simulating loading the weight to ship one by one----#
		cur_cap = 0 # loaded capacity of current ship
		num_ship = 1 # number of ship needed

		for w in weights:
			cur_cap += w
			if cur_cap > mid: # current ship meets its capacity
				cur_cap = w
				num_ship += 1
		#---------------simulation ends--------------------------#

		# we need too many ships, so we need to increase capacity to reduce num of ships needed
		if num_ship > D:
			low = mid+1
		# we are able to ship with good num of ships, 
		# but we still need to find the optimal max capacity
		else:
			high = mid

	return low
