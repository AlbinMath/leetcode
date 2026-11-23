# LeetCode 2516: Take K of Each Character From Left and Right

**LeetCode Problem #2516 — Take K of Each Character From Left and Right**
Solve LeetCode Take K of Each Character From Left and Right using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Take K of Each Character From Left and Right |
| LeetCode | #2516 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of the characters `'a'`, `'b'`, and `'c'` and a non-negative integer `k`. Each minute, you may take either the **leftmost** character of `s`, or the **rightmost** character of `s`.

Return* the **minimum** number of minutes needed for you to take **at least** *`k`* of each character, or return *`-1`* if it is not possible to take *`k`* of each character.*

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only the letters `'a'`, `'b'`, and `'c'`.
- `0 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "aabaaaacaabc", k = 2`
- **Output:** `8`
- **Explanation:** Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

### Example 2
- **Input:** `s = "a", k = 1`
- **Output:** `-1`
- **Explanation:** It is not possible to take one 'b' or 'c' so return -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Take K of Each Character From Left and Right**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabaaaacaabc", k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

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
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
            
        total = [s.count('a'), s.count('b'), s.count('c')]
        if min(total) < k:
            return -1
            
        win = [0, 0, 0]
        max_middle = 0
        left = 0
        base = ord('a')
        
        for right, ch in enumerate(s):
            idx = ord(ch) - base
            win[idx] += 1
            
            while win[idx] > total[idx] - k:
                win[ord(s[left]) - base] -= 1
                left += 1
                
            if right - left + 1 > max_middle:
                max_middle = right - left + 1
                
        return len(s) - max_middle
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
- [3304. Find the K-th Character in String Game I](../../3501-4000/3600-find-the-k-th-character-in-string-game-i/)
- [3307. Find the K-th Character in String Game II](../../3501-4000/3601-find-the-k-th-character-in-string-game-ii/)
- [2558. Take Gifts From the Richest Pile](../../2501-3000/2692-take-gifts-from-the-richest-pile/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/)
