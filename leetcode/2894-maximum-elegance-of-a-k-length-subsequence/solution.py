from typing import List

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: x[0], reverse=True)
        
        total_profit = 0
        seen = set()
        dup_profits = []
        
        for i in range(k):
            profit, cat = items[i]
            total_profit += profit
            if cat not in seen:
                seen.add(cat)
            else:
                dup_profits.append(profit)
                
        max_elegance = total_profit + len(seen) ** 2
        
        for i in range(k, len(items)):
            if not dup_profits:
                break
            profit, cat = items[i]
            if cat not in seen:
                seen.add(cat)
                total_profit += profit - dup_profits.pop()
                max_elegance = max(max_elegance, total_profit + len(seen) ** 2)
                
        return max_elegance
