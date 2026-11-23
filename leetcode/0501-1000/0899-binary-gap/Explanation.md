# LeetCode 868: Binary Gap

**LeetCode Problem #868 — Binary Gap**
Solve LeetCode Binary Gap using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Gap |
| LeetCode | #868 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, find and return *the **longest distance** between any two **adjacent** *`1`*'s in the binary representation of *`n`*. If there are no two adjacent *`1`*'s, return *`0`*.*

Two `1`'s are **adjacent** if there are only `0`'s separating them (possibly no `0`'s). The distance between two `1`'s is the absolute difference between their bit positions. For example, the two `1`'s in `"1001"` have a distance of 3.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 22`
- **Output:** `2`
- **Explanation:** 22 in binary is "10110".
The first adjacent pair of 1's is " 1 0 1 10" with a distance of 2.
The second adjacent pair of 1's is "10 11 0" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that " 1 01 1 0" is not a valid pair since there is a 1 separating the two 1's underlined.

### Example 2
- **Input:** `n = 8`
- **Output:** `0`
- **Explanation:** 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

### Example 3
- **Input:** `n = 5`
- **Output:** `2`
- **Explanation:** 5 in binary is "101".

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Binary Gap**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 22`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 22 in binary is "10110".
The first adjacent pair of 1's is " 1 0 1 10" with a distance of 2.
The second adjacent pair of 1's is "10 11 0" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that " 1 01 1 0" is not a valid pair since there is a 1 separating the two 1's underlined.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        last_position = -1
        max_gap = 0

        for i, bit in enumerate(binary):
            if bit == '1':
                if last_position != -1:
                    max_gap = max(max_gap, i - last_position)
                last_position = i

        return max_gap
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [164. Maximum Gap](../../0001-0500/0164-maximum-gap/)
- [3589. Count Prime-Gap Balanced Subarrays](../../3501-4000/3907-count-prime-gap-balanced-subarrays/)
- [67. Add Binary](../../0001-0500/0067-add-binary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-gap/)
