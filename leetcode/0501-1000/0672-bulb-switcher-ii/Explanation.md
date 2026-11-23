# LeetCode 672: Bulb Switcher II

**LeetCode Problem #672 — Bulb Switcher II**
Solve LeetCode Bulb Switcher II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bulb Switcher II |
| LeetCode | #672 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a room with `n` bulbs labeled from `1` to `n` that all are turned on initially, and **four buttons** on the wall. Each of the four buttons has a different functionality where:

**Button 1:** Flips the status of all the bulbs. 
 **Button 2:** Flips the status of all the bulbs with even labels (i.e., `2, 4, ...`). 
 **Button 3:** Flips the status of all the bulbs with odd labels (i.e., `1, 3, ...`). 
 **Button 4:** Flips the status of all the bulbs with a label `j = 3k + 1` where `k = 0, 1, 2, ...` (i.e., `1, 4, 7, 10, ...`).

You must make **exactly** `presses` button presses in total. For each press, you may pick **any** of the four buttons to press.

Given the two integers `n` and `presses`, return *the number of **different possible statuses** after performing all *`presses`* button presses*.

## Constraints
- `1 <= n <= 1000`
- `0 <= presses <= 1000`

## Examples
### Example 1
- **Input:** `n = 1, presses = 1`
- **Output:** `2`
- **Explanation:** Status can be:
- [off] by pressing button 1
- [on] by pressing button 2

### Example 2
- **Input:** `n = 2, presses = 1`
- **Output:** `3`
- **Explanation:** Status can be:
- [off, off] by pressing button 1
- [on, off] by pressing button 2
- [off, on] by pressing button 3

### Example 3
- **Input:** `n = 3, presses = 1`
- **Output:** `4`
- **Explanation:** Status can be:
- [off, off, off] by pressing button 1
- [on, off, on] by pressing button 2
- [off, on, off] by pressing button 3
- [off, on, on] by pressing button 4

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Bulb Switcher II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, presses = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Status can be:
- [off] by pressing button 1
- [on] by pressing button 2

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
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        seen = set()
        for x in range(16):
            b = bin(x).count('1')
            if b <= presses and (presses - b) % 2 == 0:
                s = tuple(
                    1 ^ ((x & 1) != 0)
                    ^ (((x >> 1) & 1) != 0 and i % 2 == 0)
                    ^ (((x >> 2) & 1) != 0 and i % 2 == 1)
                    ^ (((x >> 3) & 1) != 0 and i % 3 == 1)
                    for i in range(1, n + 1)
                )
                seen.add(s)
        return len(seen)
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
- [319. Bulb Switcher](../../0001-0500/0319-bulb-switcher/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bulb-switcher-ii/)
