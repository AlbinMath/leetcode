# LeetCode 1962: Remove Stones to Minimize the Total

**LeetCode Problem #1962 — Remove Stones to Minimize the Total**
Solve LeetCode Remove Stones to Minimize the Total using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Stones to Minimize the Total |
| LeetCode | #1962 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `piles`, where `piles[i]` represents the number of stones in the `i^th` pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

Choose any `piles[i]` and **remove** `floor(piles[i] / 2)` stones from it.

**Notice** that you can apply the operation on the **same** pile more than once.

Return *the **minimum** possible total number of stones remaining after applying the *`k`* operations*.

`floor(x)` is the **largest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).

## Constraints
- `1 <= piles.length <= 10^5`
- `1 <= piles[i] <= 10^4`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `piles = [5,4,9], k = 2`
- **Output:** `12`
- **Explanation:** Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4, 5 ].
- Apply the operation on pile 0. The resulting piles are [ 3 ,4,5].
The total number of stones in [3,4,5] is 12.

### Example 2
- **Input:** `piles = [4,3,6,7], k = 3`
- **Output:** `12`
- **Explanation:** Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3, 3 ,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3, 4 ].
- Apply the operation on pile 0. The resulting piles are [ 2 ,3,3,4].
The total number of stones in [2,3,3,4] is 12.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Stones to Minimize the Total**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `piles = [5,4,9], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4, 5 ].
- Apply the operation on pile 0. The resulting piles are [ 3 ,4,5].
The total number of stones in [3,4,5] is 12.

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
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]  # max-heap via negation
        heapq.heapify(heap)
        for _ in range(k):
            p = -heap[0]
            heapq.heapreplace(heap, -(p - p // 2))
        return -sum(heap)
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
- [2646. Minimize the Total Price of the Trips](../../2501-3000/2646-minimize-the-total-price-of-the-trips/)
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1010. Pairs of Songs With Total Durations Divisible by 60](../../1001-1500/1010-pairs-of-songs-with-total-durations-divisible-by-60/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)
