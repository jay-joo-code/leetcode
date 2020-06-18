
# attempt (AC) after referring to solution
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
  if not people: return []
  
  people.sort(key=lambda arr: arr[0]*1000-arr[1], reverse=True)
  res = []
  
  for person in people:
      res.insert(person[1], person)
  
  return res
