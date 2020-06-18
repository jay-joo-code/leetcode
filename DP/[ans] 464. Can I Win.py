
# solution (AC)
def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
	seen = {}

	def can_win(choices, remainder):
			# if the largest choice exceeds the remainder, then we can win!
			if choices[-1] >= remainder:
					return True

			# if we have seen this exact scenario play out, then we know the outcome
			# tuple look up is faster than str lookup. 200 ms difference
			seen_key = tuple(choices)
			if seen_key in seen:
					return seen[seen_key]

			# we haven't won yet.. it's the next player's turn.
			# importantly, if we win just one permutation then
			# we're still on our way to being able to 'force their hand'
			for index in range(len(choices)):
					if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
							seen[seen_key] = True
							return True

			# uh-oh if we got here then next player won all permutations, we can't force their hand
			# actually, they were able to force our hand :(
			seen[seen_key] = False
			return False


	# note: usefully, choices is already sorted
	choices = list(range(1, maxChoosableInteger + 1))

	# let's do some quick checks before we journey through the tree of permutations
	summed_choices = sum(choices)

	# if all the choices added up are less then the total, no-one can win
	if summed_choices < desiredTotal:
			return False

	# if the sum matches desiredTotal exactly, then as
	# long as there is an odd number of choices then first player wins
	if summed_choices == desiredTotal and len(choices) % 2:
			return True

	# slow: time to go through the tree of permutations
	return can_win(choices, desiredTotal)
