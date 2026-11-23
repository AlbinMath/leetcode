import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []  # buy: [-price, amt] (max-heap), sell: [price, amt] (min-heap)

        for p, a, t in orders:
            if t == 0:  # buy order
                while a > 0 and sell and sell[0][0] <= p:
                    take = min(a, sell[0][1])
                    a -= take
                    sell[0][1] -= take
                    if sell[0][1] == 0:
                        heapq.heappop(sell)
                if a > 0:
                    heapq.heappush(buy, [-p, a])
            else:  # sell order
                while a > 0 and buy and -buy[0][0] >= p:
                    take = min(a, buy[0][1])
                    a -= take
                    buy[0][1] -= take
                    if buy[0][1] == 0:
                        heapq.heappop(buy)
                if a > 0:
                    heapq.heappush(sell, [p, a])

        MOD = 10**9 + 7
        return (sum(x[1] for x in buy) + sum(x[1] for x in sell)) % MOD
