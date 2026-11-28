# LeetCode 1599: Maximum Profit of Operating a Centennial Wheel

**LeetCode Problem #1599 — Maximum Profit of Operating a Centennial Wheel**
Solve LeetCode Maximum Profit of Operating a Centennial Wheel using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Profit of Operating a Centennial Wheel |
| LeetCode | #1599 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are the operator of a Centennial Wheel that has **four gondolas**, and each gondola has room for **up** **to** **four people**. You have the ability to rotate the gondolas **counterclockwise**, which costs you `runningCost` dollars.

You are given an array `customers` of length `n` where `customers[i]` is the number of new customers arriving just before the `i^th` rotation (0-indexed). This means you **must rotate the wheel **`i`** times before the **`customers[i]`** customers arrive**. **You cannot make customers wait if there is room in the gondola**. Each customer pays `boardingCost` dollars when they board on the gondola closest to the ground and will exit once that gondola reaches the ground again.

You can stop the wheel at any time, including **before** **serving** **all** **customers**. If you decide to stop serving customers, **all subsequent rotations are free** in order to get all the customers down safely. Note that if there are currently more than four customers waiting at the wheel, only four will board the gondola, and the rest will wait **for the next rotation**.

Return* the minimum number of rotations you need to perform to maximize your profit.* If there is **no scenario** where the profit is positive, return `-1`.

## Constraints
- `n == customers.length`
- `1 <= n <= 10^5`
- `0 <= customers[i] <= 50`
- `1 <= boardingCost, runningCost <= 100`

## Examples
### Example 1
- **Input:** `customers = [8,3], boardingCost = 5, runningCost = 6`
- **Output:** `3`
- **Explanation:** The numbers written on the gondolas are the number of people currently there.
1. 8 customers arrive, 4 board and 4 wait for the next gondola, the wheel rotates. Current profit is 4 * $5 - 1 * $6 = $14.
2. 3 customers arrive, the 4 waiting board the wheel and the other 3 wait, the wheel rotates. Current profit is 8 * $5 - 2 * $6 = $28.
3. The final 3 customers board the gondola, the wheel rotates. Current profit is 11 * $5 - 3 * $6 = $37.
The highest profit was $37 after rotating the wheel 3 times.

### Example 2
- **Input:** `customers = [10,9,6], boardingCost = 6, runningCost = 4`
- **Output:** `7`
- **Explanation:** 1. 10 customers arrive, 4 board and 6 wait for the next gondola, the wheel rotates. Current profit is 4 * $6 - 1 * $4 = $20.
2. 9 customers arrive, 4 board and 11 wait (2 originally waiting, 9 newly waiting), the wheel rotates. Current profit is 8 * $6 - 2 * $4 = $40.
3. The final 6 customers arrive, 4 board and 13 wait, the wheel rotates. Current profit is 12 * $6 - 3 * $4 = $60.
4. 4 board and 9 wait, the wheel rotates. Current profit is 16 * $6 - 4 * $4 = $80.
5. 4 board and 5 wait, the wheel rotates. Current profit is 20 * $6 - 5 * $4 = $100.
6. 4 board and 1 waits, the wheel rotates. Current profit is 24 * $6 - 6 * $4 = $120.
7. 1 boards, the wheel rotates. Current profit is 25 * $6 - 7 * $4 = $122.
The highest profit was $122 after rotating the wheel 7 times.

### Example 3
- **Input:** `customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92`
- **Output:** `-1`
- **Explanation:** 1. 3 customers arrive, 3 board and 0 wait, the wheel rotates. Current profit is 3 * $1 - 1 * $92 = -$89.
2. 4 customers arrive, 4 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 2 * $92 = -$177.
3. 0 customers arrive, 0 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 3 * $92 = -$269.
4. 5 customers arrive, 4 board and 1 waits, the wheel rotates. Current profit is 11 * $1 - 4 * $92 = -$357.
5. 1 customer arrives, 2 board and 0 wait, the wheel rotates. Current profit is 13 * $1 - 5 * $92 = -$447.
The profit was never positive, so return -1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Profit of Operating a Centennial Wheel**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `customers = [8,3], boardingCost = 5, runningCost = 6`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The numbers written on the gondolas are the number of people currently there.
1. 8 customers arrive, 4 board and 4 wait for the next gondola, the wheel rotates. Current profit is 4 * $5 - 1 * $6 = $14.
2. 3 customers arrive, the 4 waiting board the wheel and the other 3 wait, the wheel rotates. Current profit is 8 * $5 - 2 * $6 = $28.
3. The final 3 customers board the gondola, the wheel rotates. Current profit is 11 * $5 - 3 * $6 = $37.
The highest profit was $37 after rotating the wheel 3 times.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = boarded = rotations = 0
        best_profit = 0
        ans = -1
        n = len(customers)
        i = 0

        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
                i += 1
            take = min(4, waiting)
            waiting -= take
            boarded += take
            rotations += 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > best_profit:
                best_profit = profit
                ans = rotations

        return ans
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1235. Maximum Profit in Job Scheduling](../../1001-1500/1235-maximum-profit-in-job-scheduling/)
- [3530. Maximum Profit from Valid Topological Order in DAG](../../3501-4000/3530-maximum-profit-from-valid-topological-order-in-dag/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/)
