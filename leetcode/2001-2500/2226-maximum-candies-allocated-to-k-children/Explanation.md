# LeetCode 2226: Maximum Candies Allocated to K Children

**LeetCode Problem #2226 — Maximum Candies Allocated to K Children**
Solve LeetCode Maximum Candies Allocated to K Children using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Candies Allocated to K Children |
| LeetCode | #2226 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `candies`. Each element in the array denotes a pile of candies of size `candies[i]`. You can divide each pile into any number of **sub piles**, but you **cannot** merge two piles together.

You are also given an integer `k`. You should allocate piles of candies to `k` children such that each child gets the **same** number of candies. Each child can be allocated candies from **only one** pile of candies and some piles of candies may go unused.

Return *the **maximum number of candies** each child can get.*

## Constraints
- `1 <= candies.length <= 10^5`
- `1 <= candies[i] <= 10^7`
- `1 <= k <= 10^12`

## Examples
### Example 1
- **Input:** `candies = [5,8,6], k = 3`
- **Output:** `5`
- **Explanation:** We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

### Example 2
- **Input:** `candies = [2,5], k = 11`
- **Output:** `0`
- **Explanation:** There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Candies Allocated to K Children**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candies = [5,8,6], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

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
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        lo, hi = 1, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if sum(p // mid for p in candies) >= k:
                lo = mid
            else:
                hi = mid - 1

        return lo
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
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1191-k-concatenation-maximum-sum/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2106-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/)
