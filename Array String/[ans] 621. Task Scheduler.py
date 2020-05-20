
# solution
def leastInterval(self, tasks: List[str], n: int) -> int:
	counter = {}
	
	for task in tasks:
		if task in counter:
			counter[task] += 1
		else:
			counter[task] = 1
	
	chars_by_freq = sorted(counter, key=lambda k:counter[k], reverse=True)
	highest = counter[chars_by_freq[0]]
	idle = (highest - 1) * n
	
	for i in range(1, len(chars_by_freq)):
		idle -= min(counter[chars_by_freq[i]], highest-1)

	if idle > 0:
		return len(tasks) + idle
	else:
		return len(tasks)