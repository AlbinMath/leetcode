# LeetCode 859: Buddy Strings

**LeetCode Problem #859 — Buddy Strings**
Solve LeetCode Buddy Strings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Buddy Strings |
| LeetCode | #859 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `goal`, return `true`* if you can swap two letters in *`s`* so the result is equal to *`goal`*, otherwise, return *`false`*.*

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

For example, swapping at indices `0` and `2` in `"abcd"` results in `"cbad"`.

## Constraints
- `1 <= s.length, goal.length <= 2 * 10^4`
- `s` and `goal` consist of lowercase letters.

## Examples
### Example 1
- **Input:** `s = "ab", goal = "ba"`
- **Output:** `true`
- **Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

### Example 2
- **Input:** `s = "ab", goal = "ab"`
- **Output:** `false`
- **Explanation:** The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

### Example 3
- **Input:** `s = "aa", goal = "aa"`
- **Output:** `true`
- **Explanation:** You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Buddy Strings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ab", goal = "ba"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

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
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # Swapping identical characters keeps the string unchanged
            return len(set(s)) < len(s)

        differences = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append(i)

        # Exactly two positions must differ
        if len(differences) != 2:
            return False

        i, j = differences

        # Swapping these two characters must produce goal
        return s[i] == goal[j] and s[j] == goal[i]
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
- [43. Multiply Strings](../../0001-0500/0043-multiply-strings/)
- [205. Isomorphic Strings](../../0001-0500/0205-isomorphic-strings/)
- [415. Add Strings](../../0001-0500/0415-add-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/buddy-strings/)
