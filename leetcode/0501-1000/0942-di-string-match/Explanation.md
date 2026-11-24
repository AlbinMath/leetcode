# LeetCode 942: DI String Match

**LeetCode Problem #942 — DI String Match**
Solve LeetCode DI String Match using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | DI String Match |
| LeetCode | #942 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

`s[i] == 'I'` if `perm[i] < perm[i + 1]`, and 
 `s[i] == 'D'` if `perm[i] > perm[i + 1]`.

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'I'` or `'D'`.

## Examples
### Example 1
- **Input:** `s = "IDID"`
- **Output:** `[0,4,1,3,2]`

### Example 2
- **Input:** `s = "III"`
- **Output:** `[0,1,2,3]`

### Example 3
- **Input:** `s = "DDI"`
- **Output:** `[3,2,0,1]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **DI String Match**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "IDID"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,4,1,3,2]`.

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
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        perm = []

        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1

        perm.append(low)

        return perm
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
- [686. Repeated String Match](../../0501-1000/0686-repeated-string-match/)
- [2375. Construct Smallest Number From DI String](../../2001-2500/2375-construct-smallest-number-from-di-string/)
- [4105. Repeated String Match II](../../4001-4500/4105-repeated-string-match-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/di-string-match/)
