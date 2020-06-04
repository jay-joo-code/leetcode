
# solution (accepted)
def minRefuelStops(self, target, startFuel, s):
	"""
	dp[t] means the furthest distance that we can get with t times of refueling.

	So for every station s[i],
	if the current distance dp[t] >= s[i][0], we can refuel:
	dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])

	In the end, we'll return the first t with dp[i] >= target,
	otherwise we'll return -1.
	"""
	dp = [startFuel] + [0] * len(s)

	# iterate available stations
	for i in range(len(s)):
		
		for t in range(i + 1)[::-1]:
				# if the current distance dp[t] >= s[i][0], we can refuel:
				if dp[t] >= s[i][0]:
						dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
	
	# return the first t with dp[i] >= target
	for t, d in enumerate(dp):
			if d >= target: return t
	return -1
