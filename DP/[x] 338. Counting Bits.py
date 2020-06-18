
# attempt (AC) after mistakes
def countBits(self, num: int) -> List[int]:
  # slow
  counter = [0]
  accum = [0]
  
  # 1 -> num
  for i in range(1, num+1):
      accum[-1] += 1
      count = 0

      # iterate accum, carry over 2s
      for j in range(len(accum)-1, -1, -1):
          if accum[j] == 2:
              accum[j] = 0
              
              if j == 0:
                  accum.insert(0, 1)
              else:
                  accum[j-1] += 1
                  
          if accum[j] == 1:
              count += 1

      counter.append(count)
  
  return counter
