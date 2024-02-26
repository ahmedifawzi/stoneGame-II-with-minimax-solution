class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def help(i, m, is_alex):
            if i >= len(piles):
                return 0
            
            if (i, m, is_alex) in memo:
                return memo[(i, m, is_alex)]
            
            max_score = float('-inf') if is_alex == 0 else float('inf')
            curr_sum = 0
            
            for x in range(i, min(len(piles), i + 2 * m)):
                curr_sum += piles[x]
                next_score = help(x + 1, max(x - i + 1, m), 1 - is_alex)
                
                if is_alex == 0:
                    max_score = max(max_score, curr_sum + next_score)
                else:
                    max_score = min(max_score, next_score)
            
            memo[(i, m, is_alex)] = max_score
            return max_score

        return help(0, 1, 0)
