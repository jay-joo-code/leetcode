
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
	m = len(nums1)
	n = len(nums2)
	nums1 += [float('inf')]
	nums2 += [float('inf')]
	t = m + n
	
	finding = []
	if t % 2 == 0:
		finding += [t // 2] + [t // 2 + 1]
	else:
		finding.append((t+1)//2)
	
	i, j, count = 0, 0, 0
	res = []
	while len(finding) != 0:
		count += 1
		
		if nums1[i] < nums2[j]:
			if count in finding:
				res.append(nums1[i])
				finding.pop(0)
			i += 1
				
		else:
			if count in finding:
				res.append(nums2[j])
				finding.pop(0)
			j += 1

	if len(res) == 1: return res[0]
	else: 
		return (res[0]+res[1]) / 2