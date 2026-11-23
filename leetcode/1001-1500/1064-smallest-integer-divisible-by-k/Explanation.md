# LeetCode 1015: Smallest Integer Divisible by K

**LeetCode Problem #1015 — Smallest Integer Divisible by K**
Solve LeetCode Smallest Integer Divisible by K using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Integer Divisible by K |
| LeetCode | #1015 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a positive integer `k`, you need to find the **length** of the **smallest** positive integer `n` such that `n` is divisible by `k`, and `n` only contains the digit `1`.

Return *the **length** of *`n`. If there is no such `n`, return -1.

**Note:** `n` may not fit in a 64-bit signed integer.

## Constraints
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `k = 1`
- **Output:** `1`
- **Explanation:** The smallest answer is n = 1, which has length 1.

### Example 2
- **Input:** `k = 2`
- **Output:** `-1`
- **Explanation:** There is no such positive integer n divisible by 2.

### Example 3
- **Input:** `k = 3`
- **Output:** `3`
- **Explanation:** The smallest answer is n = 111, which has length 3.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Integer Divisible by K**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 1`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The smallest answer is n = 1, which has length 1.

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
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        r = 0
        for i in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0:
                return i
        return -1
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
- [3821. Find Nth Smallest Integer With K One Bits](../../4001-4500/4189-find-nth-smallest-integer-with-k-one-bits/)
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2301-count-array-pairs-divisible-by-k/)
- [2261. K Divisible Elements Subarrays](../../2001-2500/2339-k-divisible-elements-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-integer-divisible-by-k/)
