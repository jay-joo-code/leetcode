
# solution
def minCostClimbingStairs(self, cost: List[int]) -> int:
	cost_to_arrive = [0, 0] + [None] * (len(cost)-1)
	
	for i in range(2, len(cost)+1):
		cost_to_arrive[i] = min(cost[i-2] + cost_to_arrive[i-2], cost[i-1] + cost_to_arrive[i-1])
	
	return cost_to_arrive[-1]