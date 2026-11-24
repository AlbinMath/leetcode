# LeetCode 1847: Closest Room

**LeetCode Problem #1847 — Closest Room**
Solve LeetCode Closest Room using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Room |
| LeetCode | #1847 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a hotel with `n` rooms. The rooms are represented by a 2D integer array `rooms` where `rooms[i] = [roomId_i, size_i]` denotes that there is a room with room number `roomId_i` and size equal to `size_i`. Each `roomId_i` is guaranteed to be **unique**.

You are also given `k` queries in a 2D array `queries` where `queries[j] = [preferred_j, minSize_j]`. The answer to the `j^th` query is the room number `id` of a room such that:

The room has a size of **at least** `minSize_j`, and 
 `abs(id - preferred_j)` is **minimized**, where `abs(x)` is the absolute value of `x`.

If there is a **tie** in the absolute difference, then use the room with the **smallest** such `id`. If there is **no such room**, the answer is `-1`.

Return *an array *`answer`* of length *`k`* where *`answer[j]`* contains the answer to the *`j^th`* query*.

## Constraints
- `n == rooms.length`
- `1 <= n <= 10^5`
- `k == queries.length`
- `1 <= k <= 10^4`
- `1 <= roomId_i, preferred_j <= 10^7`
- `1 <= size_i, minSize_j <= 10^7`

## Examples
### Example 1
- **Input:** `rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]`
- **Output:** `[3,-1,3]`
- **Explanation:** The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.

### Example 2
- **Input:** `rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]`
- **Output:** `[2,1,3]`
- **Explanation:** The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Closest Room**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,-1,3]`.
4. **Verification:** The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.

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
from bisect import bisect_left, insort
from typing import List

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda r: -r[1])
        order = sorted(range(len(queries)), key=lambda i: -queries[i][1])

        ids = []              # sorted room IDs with size >= current minSize
        ans = [-1] * len(queries)
        p = 0

        for qi in order:
            pref, min_size = queries[qi]

            while p < len(rooms) and rooms[p][1] >= min_size:
                insort(ids, rooms[p][0])
                p += 1

            if not ids:
                continue

            k = bisect_left(ids, pref)
            best = -1
            if k > 0:
                best = ids[k - 1]
            if k < len(ids):
                if best == -1 or ids[k] - pref < pref - best:
                    best = ids[k]
            ans[qi] = best

        return ans
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
- [16. 3Sum Closest](../../0001-0500/0016-3sum-closest/)
- [564. Find the Closest Palindrome](../../0501-1000/0564-find-the-closest-palindrome/)
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-room/)
