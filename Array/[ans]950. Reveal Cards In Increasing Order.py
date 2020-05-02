from typing import List
from collections import deque

# solution: simulation
def deckRevealedIncreasing(deck):
	N = len(deck)
	index = deque(range(N))
	ans = [None] * N

	for card in sorted(deck):
		ans[index.popleft()] = card
		if index:
			index.append(index.popleft())

	return ans

deckRevealedIncreasing([2, 5, 3, 6])