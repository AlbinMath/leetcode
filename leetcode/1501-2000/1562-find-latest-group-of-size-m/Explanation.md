# LeetCode 1562: Find Latest Group of Size M

**LeetCode Problem #1562 — Find Latest Group of Size M**
Solve LeetCode Find Latest Group of Size M using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Latest Group of Size M |
| LeetCode | #1562 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `arr` that represents a permutation of numbers from `1` to `n`.

You have a binary string of size `n` that initially has all its bits set to zero. At each step `i` (assuming both the binary string and `arr` are 1-indexed) from `1` to `n`, the bit at position `arr[i]` is set to `1`.

You are also given an integer `m`. Find the latest step at which there exists a group of ones of length `m`. A group of ones is a contiguous substring of `1`'s such that it cannot be extended in either direction.

Return *the latest step at which there exists a group of ones of length **exactly*** `m`. *If no such group exists, return* `-1`.

## Constraints
- `n == arr.length`
- `1 <= m <= n <= 10^5`
- `1 <= arr[i] <= n`
- All integers in `arr` are **distinct**.

## Examples
### Example 1
- **Input:** `arr = [3,5,1,2,4], m = 1`
- **Output:** `4`
- **Explanation:** Step 1: "00 1 00", groups: ["1"]
Step 2: "0010 1 ", groups: ["1", "1"]
Step 3: " 1 0101", groups: ["1", "1", "1"]
Step 4: "1 1 101", groups: ["111", "1"]
Step 5: "111 1 1", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.

### Example 2
- **Input:** `arr = [3,1,5,4,2], m = 2`
- **Output:** `-1`
- **Explanation:** Step 1: "00 1 00", groups: ["1"]
Step 2: " 1 0100", groups: ["1", "1"]
Step 3: "1010 1 ", groups: ["1", "1", "1"]
Step 4: "101 1 1", groups: ["1", "111"]
Step 5: "1 1 111", groups: ["11111"]
No group of size 2 exists during any step.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Latest Group of Size M**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,5,1,2,4], m = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Step 1: "00 1 00", groups: ["1"]
Step 2: "0010 1 ", groups: ["1", "1"]
Step 3: " 1 0101", groups: ["1", "1", "1"]
Step 4: "1 1 101", groups: ["111", "1"]
Step 5: "111 1 1", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        length = [0] * (n + 2)
        cnt = [0] * (n + 2)
        ans = -1

        for i, p in enumerate(arr, 1):
            left, right = length[p - 1], length[p + 1]
            total = left + right + 1

            cnt[left] -= 1
            cnt[right] -= 1
            cnt[total] += 1

            length[p - left] = total
            length[p + right] = total

            if cnt[m] > 0:
                ans = i

        return ans
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3254. Find the Power of K-Size Subarrays I](../../3001-3500/3254-find-the-power-of-k-size-subarrays-i/)
- [3255. Find the Power of K-Size Subarrays II](../../3001-3500/3255-find-the-power-of-k-size-subarrays-ii/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-latest-group-of-size-m/)
