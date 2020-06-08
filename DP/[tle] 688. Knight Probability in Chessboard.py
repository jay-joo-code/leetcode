
# attempt (TLE)
def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if r < 0 or c < 0 or r >= N or c >= N:
            return 0
        
        if K == 0:
            return 1

        direction = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        accum = 0

        for dr, dc in direction:
            accum += (1 / 8) * self.knightProbability(N, K-1, r+dr, c+dc)

        return accum

# solution (accepted)
# don't understand what it's memoizing
# really don't want to right now
# future me please follow through each step
# and figure out what it's memoizing
def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        mem = {}
        def dfs(k,x,y,P):
            p = 0
            if 0 <= x < N and 0 <= y < N:
                if k < K:
                    for dx,dy in moves:
                        x_next = x + dx
                        y_next = y + dy
                        if (x_next, y_next, k + 1) not in mem:
                            mem[(x_next, y_next, k + 1)] = dfs(k + 1, x_next, y_next, P / len(moves))
                        p += mem[(x_next, y_next, k + 1)]
                else:   # k == K
                    return P

            return p

        return dfs(0,r,c,1.0)
