# LeetCode 1980: Find Unique Binary String

**LeetCode Problem #1980 — Find Unique Binary String**
Solve LeetCode Find Unique Binary String using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Unique Binary String |
| LeetCode | #1980 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length *`n`* that **does not appear** in *`nums`*. If there are multiple answers, you may return **any** of them*.

## Constraints
- `n == nums.length`
- `1 <= n <= 16`
- `nums[i].length == n`
- `nums[i] `is either `'0'` or `'1'`.
- All the strings of `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = ["01","10"]`
- **Output:** `"11"`
- **Explanation:** "11" does not appear in nums. "00" would also be correct.

### Example 2
- **Input:** `nums = ["00","01"]`
- **Output:** `"11"`
- **Explanation:** "11" does not appear in nums. "10" would also be correct.

### Example 3
- **Input:** `nums = ["111","011","001"]`
- **Output:** `"101"`
- **Explanation:** "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Unique Binary String**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = ["01","10"]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"11"`.
4. **Verification:** "11" does not appear in nums. "00" would also be correct.

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
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))
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
- [1545. Find Kth Bit in Nth Binary String](../../1501-2000/1667-find-kth-bit-in-nth-binary-string/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [387. First Unique Character in a String](../../0001-0500/0387-first-unique-character-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-unique-binary-string/)
