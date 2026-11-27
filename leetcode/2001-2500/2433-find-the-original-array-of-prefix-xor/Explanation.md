# LeetCode 2433: Find The Original Array of Prefix Xor

**LeetCode Problem #2433 — Find The Original Array of Prefix Xor**
Solve LeetCode Find The Original Array of Prefix Xor using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find The Original Array of Prefix Xor |
| LeetCode | #2433 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an **integer** array `pref` of size `n`. Find and return *the array *`arr`* of size *`n`* that satisfies*:

`pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

Note that `^` denotes the **bitwise-xor** operation.

It can be proven that the answer is **unique**.

## Constraints
- `1 <= pref.length <= 10^5`
- `0 <= pref[i] <= 10^6`

## Examples
### Example 1
- **Input:** `pref = [5,2,0,3,1]`
- **Output:** `[5,7,2,3,2]`
- **Explanation:** From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

### Example 2
- **Input:** `pref = [13]`
- **Output:** `[13]`
- **Explanation:** We have pref[0] = arr[0] = 13.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find The Original Array of Prefix Xor**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pref = [5,2,0,3,1]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,7,2,3,2]`.
4. **Verification:** From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def findArray(self, pref):
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i] ^ pref[i - 1])
        return res
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2527. Find Xor-Beauty of Array](../../2501-3000/2527-find-xor-beauty-of-array/)
- [2657. Find the Prefix Common Array of Two Arrays](../../2501-3000/2657-find-the-prefix-common-array-of-two-arrays/)
- [2007. Find Original Array From Doubled Array](../../2001-2500/2007-find-original-array-from-doubled-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)
