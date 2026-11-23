class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
            
        ways = 0
        for spent in range(0, total + 1, cost1):
            ways += (total - spent) // cost2 + 1
            
        return ways
