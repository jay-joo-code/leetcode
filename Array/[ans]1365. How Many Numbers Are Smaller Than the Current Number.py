
# accepted solution
class Solution:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        indices = {}
        
		# reversing required for duplicate elts
		# for duplicate elts of arry, reversing the sorted list
		# allows the lower count value overwrites the higher value
        for i in reversed(range(len(s))):
            indices[s[i]] = i

        return [indices[x] for x in arr]
        