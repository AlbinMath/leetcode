# LeetCode 2034: Stock Price Fluctuation 

**LeetCode Problem #2034 — Stock Price Fluctuation **
Solve LeetCode Stock Price Fluctuation  using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stock Price Fluctuation  |
| LeetCode | #2034 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a stream of **records** about a particular stock. Each record contains a **timestamp** and the corresponding **price** of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream **correcting** the price of the previous wrong record.

Design an algorithm that:

**Updates** the price of the stock at a particular timestamp, **correcting** the price from any previous records at the timestamp. 
 Finds the **latest price** of the stock based on the current records. The **latest price** is the price at the latest timestamp recorded. 
 Finds the **maximum price** the stock has been based on the current records. 
 Finds the **minimum price** the stock has been based on the current records.

Implement the `StockPrice` class:

`StockPrice()` Initializes the object with no price records. 
 `void update(int timestamp, int price)` Updates the `price` of the stock at the given `timestamp`. 
 `int current()` Returns the **latest price** of the stock. 
 `int maximum()` Returns the **maximum price** of the stock. 
 `int minimum()` Returns the **minimum price** of the stock.

## Constraints
- `1 <= timestamp, price <= 10^9`
- At most `10^5` calls will be made **in total** to `update`, `current`, `maximum`, and `minimum`.
- `current`, `maximum`, and `minimum` will be called **only after** `update` has been called **at least once**.

## Examples
### Example 1
- **Input:** `["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]`
- **Output:** `[null, null, null, 5, 10, null, 5, null, 2]`
- **Explanation:** StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5); // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current(); // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum(); // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3); // The previous timestamp 1 had the wrong price, so it is updated to 3.
 // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum(); // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2); // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum(); // return 2, the minimum price is 2 at timestamp 4.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Stock Price Fluctuation **, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 5, 10, null, 5, null, 2]`.
4. **Verification:** StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5); // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current(); // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum(); // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3); // The previous timestamp 1 had the wrong price, so it is updated to 3.
 // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum(); // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2); // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum(); // return 2, the minimum price is 2 at timestamp 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1164. Product Price at a Given Date](../../1001-1500/1164-product-price-at-a-given-date/)
- [1251. Average Selling Price](../../1001-1500/1251-average-selling-price/)
- [1333. Filter Restaurants by Vegan-Friendly, Price and Distance](../../1001-1500/1333-filter-restaurants-by-vegan-friendly-price-and-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stock-price-fluctuation/)
