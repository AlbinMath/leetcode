# LeetCode 1798: Maximum Number of Consecutive Values You Can Make

**LeetCode Problem #1798 — Maximum Number of Consecutive Values You Can Make**
Solve LeetCode Maximum Number of Consecutive Values You Can Make using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Consecutive Values You Can Make |
| LeetCode | #1798 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the `i^th` coin is `coins[i]`. You can **make** some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the *maximum number of consecutive integer values that you **can** **make** with your coins **starting** from and **including** *`0`.

Note that you may have multiple coins of the same value.

## Constraints
- `coins.length == n`
- `1 <= n <= 4 * 10^4`
- `1 <= coins[i] <= 4 * 10^4`

## Examples
### Example 1
- **Input:** `coins = [1,3]`
- **Output:** `2`
- **Explanation:** You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.

### Example 2
- **Input:** `coins = [1,1,1,4]`
- **Output:** `8`
- **Explanation:** You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.

### Example 3
- **Input:** `coins = [1,4,10,3,1]`
- **Output:** `20`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Consecutive Values You Can Make**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.

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
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        reach = 0
        for c in coins:
            if c > reach + 1:
                break
            reach += c
        return reach + 1
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
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)
- [1935. Maximum Number of Words You Can Type](../../1501-2000/1935-maximum-number-of-words-you-can-type/)
- [1953. Maximum Number of Weeks for Which You Can Work](../../1501-2000/1953-maximum-number-of-weeks-for-which-you-can-work/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/)
