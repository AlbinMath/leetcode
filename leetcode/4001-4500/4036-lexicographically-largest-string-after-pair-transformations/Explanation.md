# LeetCode 4036: Lexicographically Largest String After Pair Transformations

**LeetCode Problem #4036 — Lexicographically Largest String After Pair Transformations**
Solve LeetCode Lexicographically Largest String After Pair Transformations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Largest String After Pair Transformations |
| LeetCode | #4036 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

For each integer `x` in `nums`, start with a string consisting of exactly `x` lowercase `'a'` characters.

You may perform the following operation any number of times (including zero):

Choose two **adjacent equal** letters and replace them with the next letter in the alphabet.

For example, `"aa"` can be replaced with `"b"`, and `"bb"` can be replaced with `"c"`. The pair `"zz"` cannot be replaced.

For each `x`, determine the **lexicographically largest** string that can be obtained.

Return an array of strings where the `i^th` string is the answer for `nums[i]`.

A string `a` is **lexicographically larger** than a string `b` if, at the first position where they differ, `a` contains a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters are equal, the longer string is lexicographically larger.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^8`

## Examples
### Example 1
- **Input:** `nums = [2,5,7]`
- **Output:** `["b","ca","cba"]`
- **Explanation:** `nums[0] = 2`: `"aa"` &rarr; `"b"`. 
 `nums[1] = 5`: `"aaaaa"` &rarr; `"baaa"` &rarr; `"bba"` &rarr; `"ca"`. 
 `nums[2] = 7`: `"aaaaaaa"` &rarr; `"baaaaa"` &rarr; `"bbaaa"` &rarr; `"bbba"` &rarr; `"cba"`. 
 Therefore, `ans = ["b", "ca", "cba"]`.

### Example 2
- **Input:** `nums = [3,9,1]`
- **Output:** `["ba","da","a"]`
- **Explanation:** `nums[0] = 3`: `"aaa"` &rarr; `"ba"`. 
 `nums[1] = 9`: `"aaaaaaaaa"` &rarr; `"baaaaaaa"` &rarr; `"bbaaaaa"` &rarr; `"bbbaaa"` &rarr; `"bbbba"` &rarr; `"cbba"` &rarr; `"cca"` &rarr; `"da"`. 
 `nums[2] = 1`: No transformation can be applied, so the result is `"a"`. 
 Therefore, `ans = ["ba", "da", "a"]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lexicographically Largest String After Pair Transformations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["b","ca","cba"]`.
4. **Verification:** `nums[0] = 2`: `"aa"` &rarr; `"b"`. 
 `nums[1] = 5`: `"aaaaa"` &rarr; `"baaa"` &rarr; `"bba"` &rarr; `"ca"`. 
 `nums[2] = 7`: `"aaaaaaa"` &rarr; `"baaaaa"` &rarr; `"bbaaa"` &rarr; `"bbba"` &rarr; `"cba"`. 
 Therefore, `ans = ["b", "ca", "cba"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def largestString(self, nums):
        res = []
        for x in nums:
            q = x >> 25
            r = x & ((1 << 25) - 1)
            s = 'z' * q
            s += ''.join(chr(97 + b) for b in range(24, -1, -1) if (r >> b) & 1)
            res.append(s)
        return res
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [3170. Lexicographically Minimum String After Removing Stars](../../3001-3500/3170-lexicographically-minimum-string-after-removing-stars/)
- [3335. Total Characters in String After Transformations I](../../3001-3500/3335-total-characters-in-string-after-transformations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-largest-string-after-pair-transformations/)
