from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        loss = 0
        extra = 0
        for cost, cashback in transactions:
            if cost > cashback:
                loss += cost - cashback
                extra = max(extra, cashback)
            else:
                extra = max(extra, cost)
        return loss + extra
