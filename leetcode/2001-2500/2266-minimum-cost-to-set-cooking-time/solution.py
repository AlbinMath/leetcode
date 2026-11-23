class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        def get_cost(m, s):
            if not (0 <= m <= 99 and 0 <= s <= 99):
                return float('inf')
            
            digits = str(m * 100 + s)
            curr = str(startAt)
            cost = 0
            
            for d in digits:
                if d != curr:
                    cost += moveCost
                    curr = d
                cost += pushCost
                
            return cost

        m = targetSeconds // 60
        s = targetSeconds % 60
        return min(get_cost(m, s), get_cost(m - 1, s + 60))
