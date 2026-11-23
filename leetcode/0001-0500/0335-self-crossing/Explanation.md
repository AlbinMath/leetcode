# LeetCode 335: Self Crossing

**LeetCode Problem #335 — Self Crossing**
Solve LeetCode Self Crossing using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Self Crossing |
| LeetCode | #335 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `distance`.

You start at the point `(0, 0)` on an **X-Y plane,** and you move `distance[0]` meters to the north, then `distance[1]` meters to the west, `distance[2]` meters to the south, `distance[3]` meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return `true` *if your path crosses itself or *`false`* if it does not*.

## Constraints
- `1 <= distance.length <= 10^5`
- `1 <= distance[i] <= 10^5`

## Examples
### Example 1
- **Input:** `distance = [2,1,1,2]`
- **Output:** `true`
- **Explanation:** The path crosses itself at the point (0, 1).

### Example 2
- **Input:** `distance = [1,2,3,4]`
- **Output:** `false`
- **Explanation:** The path does not cross itself at any point.

### Example 3
- **Input:** `distance = [1,1,1,2,1]`
- **Output:** `true`
- **Explanation:** The path crosses itself at the point (0, 0).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Self Crossing**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `distance = [2,1,1,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The path crosses itself at the point (0, 1).

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
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        for i in range(3, len(d)):
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True
            if (i >= 5 and d[i-2] >= d[i-4] and d[i] + d[i-4] >= d[i-2]
                    and d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3]):
                return True
        return False
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
- [238. Product of Array Except Self](../../0001-0500/0238-product-of-array-except-self/)
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [728. Self Dividing Numbers](../../0501-1000/0728-self-dividing-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/self-crossing/)
