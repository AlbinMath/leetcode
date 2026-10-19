import heapq

class StockPrice:
    def __init__(self):
        self.prices = {}          # timestamp -> current price
        self.latest = 0           # largest timestamp seen
        self.max_heap = []        # (-price, timestamp)
        self.min_heap = []        # (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest]

    def maximum(self) -> int:
        while True:
            neg_price, ts = self.max_heap[0]
            if self.prices[ts] == -neg_price:
                return -neg_price
            heapq.heappop(self.max_heap)      # stale: this timestamp was corrected

    def minimum(self) -> int:
        while True:
            price, ts = self.min_heap[0]
            if self.prices[ts] == price:
                return price
            heapq.heappop(self.min_heap)
