# LeetCode 3964: Minimum Lights to Illuminate a Road

**LeetCode Problem #3964 — Minimum Lights to Illuminate a Road**
Solve LeetCode Minimum Lights to Illuminate a Road using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Lights to Illuminate a Road |
| LeetCode | #3964 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `lights` of length `n`, representing positions 0 through `n - 1` on a road.

For each position `i`:

If `lights[i] = v`, where `v > 0`, there is a working bulb at position `i` that **illuminates** every position from `max(0, i - v)` to `min(n - 1, i + v)`, inclusive. 
 If `lights[i] = 0`, there is no working bulb at position `i`.

A position is **visible** if it is illuminated by **at least** one working bulb.

You may install **additional** bulbs at **any** positions. Each additional bulb installed at position `j` **illuminates** positions from `max(0, j - 1)` to `min(n - 1, j + 1)`, inclusive.

Return the minimum number of additional bulbs required to make **every** position on the road visible.

## Constraints
- `1 <= n == lights.length <= 10^5`
- `0 <= lights[i] <= n`

## Examples
### Example 1
- **Input:** `lights = [0,0,0,0]`
- **Output:** `2`
- **Explanation:** One optimal placement is: 

 
 Install an additional bulb at position 1, illuminating positions `[0, 1, 2]`. 
 Install an additional bulb at position 3, illuminating positions `[2, 3]`. 
 

 Therefore, the minimum number of additional bulbs required is 2.

### Example 2
- **Input:** `lights = [0,0,0,2,0]`
- **Output:** `1`
- **Explanation:** Since `lights[3] = 2`, the working bulb at position 3 illuminates positions `[1, 2, 3, 4]`. 
 Installing an additional bulb at position 1 illuminates positions `[0, 1, 2]`, making every position visible. 
 Therefore, the minimum number of additional bulbs required is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Lights to Illuminate a Road**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `lights = [0,0,0,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal placement is: 

 
 Install an additional bulb at position 1, illuminating positions `[0, 1, 2]`. 
 Install an additional bulb at position 3, illuminating positions `[2, 3]`. 
 

 Therefore, the minimum number of additional bulbs required is 2.

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
    def minLights(self, lights: List[int]) -> int:
        n = len(lights)
        diff = [0] * (n + 1)
        for i, v in enumerate(lights):
            if v > 0:
                diff[max(0, i - v)] += 1
                diff[min(n - 1, i + v) + 1] -= 1

        covered = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            covered[i] = cur > 0

        res = 0
        i = 0
        while i < n:
            if covered[i]:
                i += 1
            else:
                res += 1
                i += 3
        return res
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
- [4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights](../../4001-4500/4025-minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/)
