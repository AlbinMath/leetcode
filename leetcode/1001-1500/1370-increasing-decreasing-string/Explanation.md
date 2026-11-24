# LeetCode 1370: Increasing Decreasing String

**LeetCode Problem #1370 — Increasing Decreasing String**
Solve LeetCode Increasing Decreasing String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Increasing Decreasing String |
| LeetCode | #1370 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`. Reorder the string using the following algorithm:

Remove the **smallest** character from `s` and **append** it to the result. 
 Remove the **smallest** character from `s` that is greater than the last appended character, and **append** it to the result. 
 Repeat step 2 until no more characters can be removed. 
 Remove the **largest** character from `s` and **append** it to the result. 
 Remove the **largest** character from `s` that is smaller than the last appended character, and **append** it to the result. 
 Repeat step 5 until no more characters can be removed. 
 Repeat steps 1 through 6 until all characters from `s` have been removed.

If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

Return the resulting string after reordering `s` using this algorithm.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aaaabbbbcccc"`
- **Output:** `"abccbaabccba"`
- **Explanation:** After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

### Example 2
- **Input:** `s = "rat"`
- **Output:** `"art"`
- **Explanation:** The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Increasing Decreasing String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaaabbbbcccc"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abccbaabccba"`.
4. **Verification:** After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

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
    def sortString(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []

        while len(result) < len(s):
            for i in range(26):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

            for i in range(25, -1, -1):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

        return ''.join(result)
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
- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](../../3001-3500/3105-longest-strictly-increasing-or-strictly-decreasing-subarray/)
- [926. Flip String to Monotone Increasing](../../0501-1000/0926-flip-string-to-monotone-increasing/)
- [491. Non-decreasing Subsequences](../../0001-0500/0491-non-decreasing-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/increasing-decreasing-string/)
