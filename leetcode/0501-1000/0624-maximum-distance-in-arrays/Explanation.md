# LeetCode 624: Maximum Distance in Arrays

**LeetCode Problem #624 — Maximum Distance in Arrays**
Solve LeetCode Maximum Distance in Arrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Distance in Arrays |
| LeetCode | #624 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given `m` `arrays`, where each array is sorted in **ascending order**.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.

Return *the maximum distance*.

## Constraints
- `m == arrays.length`
- `2 <= m <= 10^5`
- `1 <= arrays[i].length <= 500`
- `-10^4 <= arrays[i][j] <= 10^4`
- `arrays[i]` is sorted in **ascending order**.
- There will be at most `10^5` integers in all the arrays.

## Examples
### Example 1
- **Input:** `arrays = [[1,2,3],[4,5],[1,2,3]]`
- **Output:** `4`
- **Explanation:** One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

### Example 2
- **Input:** `arrays = [[1],[1]]`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Distance in Arrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arrays = [[1,2,3],[4,5],[1,2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

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
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        ans = 0
        for arr in arrays[1:]:
            ans = max(ans, arr[-1] - cur_min, cur_max - arr[0])
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])
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
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [2513. Minimize the Maximum of Two Arrays](../../2501-3000/2513-minimize-the-maximum-of-two-arrays/)
- [1855. Maximum Distance Between a Pair of Values](../../1501-2000/1855-maximum-distance-between-a-pair-of-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/)
