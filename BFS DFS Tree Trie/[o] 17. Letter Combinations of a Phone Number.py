
# attempt (AC)
def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        combs = []
        num_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def dfs(comb, nums):
            if nums == '':
                combs.append(comb)
            
            else:
                remaining = nums[1:]
                current = nums[0]
                chars = num_to_chars[current]
                for char in chars:
                    dfs(comb + char, remaining)
                
        dfs('', digits)
        return combs
