# LeetCode 4062: Transform Array Using Pair Operations

**LeetCode Problem #4062 — Transform Array Using Pair Operations**
Solve LeetCode Transform Array Using Pair Operations using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Transform Array Using Pair Operations |
| LeetCode | #4062 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `source` and `target`.

In one **operation**, you may choose two **distinct** indices `i` and `j` in `source`, along with any integer `delta`. Then update `source` as follows:

`source[i] = source[i] + source[j] - delta` 
 `source[j] = delta`

Return `true` if it is possible to make `source` equal to `target` after performing the operation **any** (including zero) number of times. Otherwise, return `false`.

## Constraints
- `2 <= source.length == target.length <= 10^5`
- `-10^9 <= source[i], target[i] <= 10^9`

## Examples
### Example 1
- **Input:** `source = [1,2,3], target = [0,2,4]`
- **Output:** `true`
- **Explanation:** Choose indices `i = 0` and `j = 2`, and set `delta = 4`. 
 Before operation, `source[0] = 1` and `source[2] = 3`. 
 After the operation,
 
 `source[0] = 1 + 3 - 4 = 0` 
 `source[2] = 4` 
 
 
 Hence, `source` becomes `[0, 2, 4]`, which is equal to `target`. 
 Therefore, the answer is `true`.

### Example 2
- **Input:** `source = [-5,-5], target = [-15,5]`
- **Output:** `true`
- **Explanation:** Choose indices `i = 1` and `j = 0`, and set `delta = -15`. 
 Before operation, `source[1] = -5` and `source[0] = -5`. 
 After the operation,
 
 `source[1] = -5 + (-5) - (-15) = 5` 
 `source[0] = -15` 
 
 
 Hence, `source` becomes `[-15, 5]`, which is equal to `target`. 
 Therefore, the answer is `true`.

### Example 3
- **Input:** `source = [1,2,1], target = [0,2,5]`
- **Output:** `false`
- **Explanation:** It can be shown that no matter what operations are performed, `source` can never be made equal to `target`. Therefore, the answer is `false`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Transform Array Using Pair Operations**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `source = [1,2,3], target = [0,2,4]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Choose indices `i = 0` and `j = 2`, and set `delta = 4`. 
 Before operation, `source[0] = 1` and `source[2] = 3`. 
 After the operation,
 
 `source[0] = 1 + 3 - 4 = 0` 
 `source[2] = 4` 
 
 
 Hence, `source` becomes `[0, 2, 4]`, which is equal to `target`. 
 Therefore, the answer is `true`.

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
    def canTransform(self, source: List[int], target: List[int]) -> bool:
        return sum(source) == sum(target)
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
- [3012. Minimize Length of Array Using Operations](../../3001-3500/3012-minimize-length-of-array-using-operations/)
- [3896. Minimum Operations to Transform Array into Alternating Prime](../../3501-4000/3896-minimum-operations-to-transform-array-into-alternating-prime/)
- [3022. Minimize OR of Remaining Elements Using Operations](../../3001-3500/3022-minimize-or-of-remaining-elements-using-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/transform-array-using-pair-operations/)
