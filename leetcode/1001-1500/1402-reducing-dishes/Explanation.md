# LeetCode 1402: Reducing Dishes

**LeetCode Problem #1402 — Reducing Dishes**
Solve LeetCode Reducing Dishes using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reducing Dishes |
| LeetCode | #1402 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A chef has collected data on the `satisfaction` level of his `n` dishes. Chef can cook any dish in 1 unit of time.

**Like-time coefficient** of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. `time[i] * satisfaction[i]`.

Return the maximum sum of **like-time coefficient **that the chef can obtain after preparing some amount of dishes.

Dishes can be prepared in **any **order and the chef can discard some dishes to get this maximum value.

## Constraints
- `n == satisfaction.length`
- `1 <= n <= 500`
- `-1000 <= satisfaction[i] <= 1000`

## Examples
### Example 1
- **Input:** `satisfaction = [-1,-8,0,5,-9]`
- **Output:** `14`
- **Explanation:** After Removing the second and last dish, the maximum total

### Example 2
- **Input:** `satisfaction = [4,3,2]`
- **Output:** `20`
- **Explanation:** Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

### Example 3
- **Input:** `satisfaction = [-1,-4,-5]`
- **Output:** `0`
- **Explanation:** People do not like the dishes. No dish is prepared.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reducing Dishes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `satisfaction = [-1,-8,0,5,-9]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** After Removing the second and last dish, the maximum total

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
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        suffix = 0
        total = 0
        for s in satisfaction:
            suffix += s
            if suffix <= 0:
                break
            total += suffix
        return total
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reducing-dishes/)
