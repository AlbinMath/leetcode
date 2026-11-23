# LeetCode 1801: Number of Orders in the Backlog

**LeetCode Problem #1801 — Number of Orders in the Backlog**
Solve LeetCode Number of Orders in the Backlog using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Orders in the Backlog |
| LeetCode | #1801 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `orders`, where each `orders[i] = [price_i, amount_i, orderType_i]` denotes that `amount_i`_ orders have been placed of type `orderType_i` at the price `price_i`. The `orderType_i` is:

`0` if it is a batch of `buy` orders, or 
 `1` if it is a batch of `sell` orders.

Note that `orders[i]` represents a batch of `amount_i` independent orders with the same price and order type. All orders represented by `orders[i]` will be placed before all orders represented by `orders[i+1]` for all valid `i`.

There is a **backlog** that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

If the order is a `buy` order, you look at the `sell` order with the **smallest** price in the backlog. If that `sell` order's price is **smaller than or equal to** the current `buy` order's price, they will match and be executed, and that `sell` order will be removed from the backlog. Else, the `buy` order is added to the backlog. 
 Vice versa, if the order is a `sell` order, you look at the `buy` order with the **largest** price in the backlog. If that `buy` order's price is **larger than or equal to** the current `sell` order's price, they will match and be executed, and that `buy` order will be removed from the backlog. Else, the `sell` order is added to the backlog.

Return *the total **amount** of orders in the backlog after placing all the orders from the input*. Since this number can be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= orders.length <= 10^5`
- `orders[i].length == 3`
- `1 <= price_i, amount_i <= 10^9`
- `orderType_i` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`
- **Output:** `6`
- **Explanation:** Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders with prices larger than or equal to 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders with prices larger than or equal to 25 in the backlog, so this order is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first 2 orders are matched with the 2 sell orders of the least price, which is 15 and these 2 sell orders are removed from the backlog. The 3^rd order is matched with the sell order of the least price, which is 25 and this sell order is removed from the backlog. Then, there are no more sell orders in the backlog, so the 4^th order is added to the backlog.
Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30. So the total number of orders in the backlog is 6.

### Example 2
- **Input:** `orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]`
- **Output:** `999999984`
- **Explanation:** Here is what happens with the orders:
- 10^9 orders of type sell with price 7 are placed. There are no buy orders, so the 10^9 orders are added to the backlog.
- 3 orders of type buy with price 15 are placed. They are matched with the 3 sell orders with the least price which is 7, and those 3 sell orders are removed from the backlog.
- 999999995 orders of type buy with price 5 are placed. The least price of a sell order is 7, so the 999999995 orders are added to the backlog.
- 1 order of type sell with price 5 is placed. It is matched with the buy order of the highest price, which is 5, and that buy order is removed from the backlog.
Finally, the backlog has (1000000000-3) sell orders with price 7, and (999999995-1) buy orders with price 5. So the total number of orders = 1999999991, which is equal to 999999984 % (10^9 + 7).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Orders in the Backlog**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders with prices larger than or equal to 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders with prices larger than or equal to 25 in the backlog, so this order is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first 2 orders are matched with the 2 sell orders of the least price, which is 15 and these 2 sell orders are removed from the backlog. The 3^rd order is matched with the sell order of the least price, which is 25 and this sell order is removed from the backlog. Then, there are no more sell orders in the backlog, so the 4^th order is added to the backlog.
Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30. So the total number of orders in the backlog is 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [586. Customer Placing the Largest Number of Orders](../../0501-1000/0586-customer-placing-the-largest-number-of-orders/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-orders-in-the-backlog/)
