# LeetCode 1888: Minimum Number of Flips to Make the Binary String Alternating

**LeetCode Problem #1888 — Minimum Number of Flips to Make the Binary String Alternating**
Solve LeetCode Minimum Number of Flips to Make the Binary String Alternating using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Flips to Make the Binary String Alternating |
| LeetCode | #1888 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s`. You are allowed to perform two types of operations on the string in any sequence:

**Type-1: Remove** the character at the start of the string `s` and **append** it to the end of the string. 
 **Type-2: Pick** any character in `s` and **flip** its value, i.e., if its value is `'0'` it becomes `'1'` and vice-versa.

Return *the **minimum** number of **type-2** operations you need to perform* *such that *`s` *becomes **alternating**.*

The string is called **alternating** if no two adjacent characters are equal.

For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "111000"`
- **Output:** `2`
- **Explanation:** : Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "10 1 01 0 ".

### Example 2
- **Input:** `s = "010"`
- **Output:** `0`
- **Explanation:** : The string is already alternating.

### Example 3
- **Input:** `s = "1110"`
- **Output:** `1`
- **Explanation:** : Use the second operation on the second element to make s = "1 0 10".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of Flips to Make the Binary String Alternating**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "111000"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** : Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "10 1 01 0 ".

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
    def minFlips(self, s: str) -> int:
        n = len(s)
        diff = 0
        min_flips = n
        
        for i in range(2 * n):
            curr = s[i if i < n else i - n]
            if int(curr) != (i & 1):
                diff += 1
                
            if i >= n:
                left = i - n
                if int(s[left]) != (left & 1):
                    diff -= 1
                    
            if i >= n - 1:
                min_flips = min(min_flips, diff, n - diff)
                
        return min_flips
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
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../2501-3000/2914-minimum-number-of-changes-to-make-binary-string-beautiful/)
- [3239. Minimum Number of Flips to Make Binary Grid Palindromic I](../../3001-3500/3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)
