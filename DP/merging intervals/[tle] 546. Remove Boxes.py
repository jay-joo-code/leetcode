
# attempt (tle)
# honestly pretty proud I got this far
def removeBoxes(self, boxes: List[int]) -> int:
	seen = {}
	
	def dfs(remaining, points):
			if len(remaining) == 1 and remaining[0] is None:
					return points
			
			seen_key = tuple(remaining)
			if seen_key in seen:
					return seen[seen_key] + points
			
			mx = 0
			start = end = 0
			while remaining[start] is not None:
					if remaining[start] == remaining[end]:
							end += 1
					else:
							mx = max(mx, dfs(remaining[:start] + remaining[end:], points+(end-start)*(end-start)))
							start = end
							end += 1
			seen[seen_key] = mx - points
			return mx
	
	return dfs(boxes + [None], 0)
							
