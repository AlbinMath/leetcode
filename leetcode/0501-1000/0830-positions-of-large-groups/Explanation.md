# LeetCode 830: Positions of Large Groups

**LeetCode Problem #830 — Positions of Large Groups**
Solve LeetCode Positions of Large Groups using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Positions of Large Groups |
| LeetCode | #830 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In a string ` s ` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `s = "abbxxxxzyy"` has the groups `"a"`, `"bb"`, `"xxxx"`, `"z"`, and `"yy"`.

A group is identified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group. In the above example, `"xxxx"` has the interval `[3,6]`.

A group is considered **large** if it has 3 or more characters.

Return *the intervals of every **large** group sorted in **increasing order by start index***.

## Constraints
- `1 <= s.length <= 1000`
- `s` contains lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "abbxxxxzzy"`
- **Output:** `[[3,6]]`
- **Explanation:** `"xxxx" is the only `large group with start index 3 and end index 6.

### Example 2
- **Input:** `s = "abc"`
- **Output:** `[]`
- **Explanation:** We have groups "a", "b", and "c", none of which are large groups.

### Example 3
- **Input:** `s = "abcdddeeeeaabbbcd"`
- **Output:** `[[3,5],[6,9],[12,14]]`
- **Explanation:** The large groups are "ddd", "eeee", and "bbb".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Positions of Large Groups**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abbxxxxzzy"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,6]]`.
4. **Verification:** `"xxxx" is the only `large group with start index 3 and end index 6.

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
class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        n = len(s)
        i = 0

        while i < n:
            j = i

            # Find the end of the consecutive group
            while j < n and s[j] == s[i]:
                j += 1

            # A group is large if it contains at least 3 characters
            if j - i >= 3:
                result.append([i, j - 1])

            i = j

        return result
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
- [1582. Special Positions in a Binary Matrix](../../1501-2000/1582-special-positions-in-a-binary-matrix/)
- [4035. Maximum Valid Split Positions I](../../4001-4500/4035-maximum-valid-split-positions-i/)
- [4037. Maximum Valid Split Positions II](../../4001-4500/4037-maximum-valid-split-positions-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/positions-of-large-groups/)
