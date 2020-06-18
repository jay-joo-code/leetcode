
# attempt (TLE)
def dailyTemperatures(self, T: List[int]) -> List[int]:
  res = []
  for i in range(len(T)):
      for j in range(i+1, len(T)):
          if T[i] < T[j]:
              res.append(j-i)
              break
          if j == len(T)-1:
              res.append(0)
  res.append(0)
  return res

# solution (AC)
def dailyTemperatures(self, T: List[int]) -> List[int]:
  # remember previous temperatures that haven't been calculated in stack
  # calculate if find a higher temperature
  stack = []
  res =[0] * len(T)
  
  for idx in range(len(T)):
      # stack has elts and T[last idx in stack] is less than current T[idx]
      while stack and T[stack[-1]] < T[idx]:
          res[stack[-1]] = idx - stack[-1]
          stack.pop()
          
      stack.append(idx)
      
  return res

