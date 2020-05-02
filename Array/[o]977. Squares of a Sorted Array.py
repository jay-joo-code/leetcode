from typing import List
from collections import deque

# attempt 1: sort. correct
def sortedSquares(A: List[int]) -> List[int]:
	res = [x**2 for x in A]
	return sorted(res)

# solution: two pointer
def sortedSquaresTwoPointer(self, A):
	answer = deque()
	l, r = 0, len(A) - 1
	while l <= r:
		left, right = abs(A[l]), abs(A[r])
		if left > right:
			answer.appendleft(left * left)
			l += 1
		else:
			answer.appendleft(right * right)
			r -= 1
	return list(answer)

# solution: two pointer without deque
def sortedSquaresTwoPointerWihoutDeque(self, A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer