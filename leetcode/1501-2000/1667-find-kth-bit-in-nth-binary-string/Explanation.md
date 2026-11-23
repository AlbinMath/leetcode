# LeetCode 1545: Find Kth Bit in Nth Binary String

**LeetCode Problem #1545 — Find Kth Bit in Nth Binary String**
Solve LeetCode Find Kth Bit in Nth Binary String using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Kth Bit in Nth Binary String |
| LeetCode | #1545 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows:

`S_1 = "0"` 
 `S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

`S_1 = "0"` 
 `S_2 = "0**1**1"` 
 `S_3 = "011**1**001"` 
 `S_4 = "0111001**1**0110001"`

Return *the* `k^th` *bit* *in* `S_n`. It is guaranteed that `k` is valid for the given `n`.

## Constraints
- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`

## Examples
### Example 1
- **Input:** `n = 3, k = 1`
- **Output:** `"0"`
- **Explanation:** S_3 is "

### Example 2
- **Input:** `n = 4, k = 11`
- **Output:** `"1"`
- **Explanation:** S_4 is "0111001101

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Kth Bit in Nth Binary String**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0"`.
4. **Verification:** S_3 is "

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
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"

        mid = 1 << (n - 1)

        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)

        bit = self.findKthBit(n - 1, (1 << n) - k)
        return "1" if bit == "0" else "0"
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
- [1980. Find Unique Binary String](../../2001-2500/2107-find-unique-binary-string/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)
