# LeetCode 2866: Beautiful Towers II

**LeetCode Problem #2866 — Beautiful Towers II**
Solve LeetCode Beautiful Towers II using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Beautiful Towers II |
| LeetCode | #2866 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `maxHeights` of `n` integers.

You are tasked with building `n` towers in the coordinate line. The `i^th` tower is built at coordinate `i` and has a height of `heights[i]`.

A configuration of towers is **beautiful** if the following conditions hold:

`1 <= heights[i] <= maxHeights[i]` 
 `heights` is a **mountain** array.

Array `heights` is a **mountain** if there exists an index `i` such that:

For all `0 < j <= i`, `heights[j - 1] <= heights[j]` 
 For all `i <= k < n - 1`, `heights[k + 1] <= heights[k]`

Return *the **maximum possible sum of heights** of a beautiful configuration of towers*.

## Constraints
- `1 <= n == maxHeights.length <= 10^5`
- `1 <= maxHeights[i] <= 10^9`

## Examples
### Example 1
- **Input:** `maxHeights = [5,3,4,1,1]`
- **Output:** `13`
- **Explanation:** One beautiful configuration with a maximum sum is heights = [5,3,3,1,1]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i] 
- heights is a mountain of peak i = 0.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 13.

### Example 2
- **Input:** `maxHeights = [6,5,3,9,2,7]`
- **Output:** `22`
- **Explanation:** One beautiful configuration with a maximum sum is heights = [3,3,3,9,2,2]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i]
- heights is a mountain of peak i = 3.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 22.

### Example 3
- **Input:** `maxHeights = [3,2,5,5,2,3]`
- **Output:** `18`
- **Explanation:** One beautiful configuration with a maximum sum is heights = [2,2,5,5,2,2]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i]
- heights is a mountain of peak i = 2. 
Note that, for this configuration, i = 3 can also be considered a peak.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 18.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Beautiful Towers II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `maxHeights = [5,3,4,1,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** One beautiful configuration with a maximum sum is heights = [5,3,3,1,1]. This configuration is beautiful since:
- 1 <= heights[i] <= maxHeights[i] 
- heights is a mountain of peak i = 0.
It can be shown that there exists no other beautiful configuration with a sum of heights greater than 13.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        def build(arr):
            res = [0] * n
            stack = []  # indices with strictly increasing values
            for i, x in enumerate(arr):
                while stack and arr[stack[-1]] >= x:
                    stack.pop()
                if stack:
                    j = stack[-1]
                    res[i] = res[j] + x * (i - j)
                else:
                    res[i] = x * (i + 1)
                stack.append(i)
            return res

        left = build(maxHeights)
        right = build(maxHeights[::-1])[::-1]
        return max(left[i] + right[i] - maxHeights[i] for i in range(n))
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2865. Beautiful Towers I](../../2501-3000/2865-beautiful-towers-i/)
- [526. Beautiful Arrangement](../../0501-1000/0526-beautiful-arrangement/)
- [667. Beautiful Arrangement II](../../0501-1000/0667-beautiful-arrangement-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/beautiful-towers-ii/)
