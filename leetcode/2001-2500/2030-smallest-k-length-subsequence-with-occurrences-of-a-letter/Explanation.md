# LeetCode 2030: Smallest K-Length Subsequence With Occurrences of a Letter

**LeetCode Problem #2030 — Smallest K-Length Subsequence With Occurrences of a Letter**
Solve LeetCode Smallest K-Length Subsequence With Occurrences of a Letter using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest K-Length Subsequence With Occurrences of a Letter |
| LeetCode | #2030 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`, an integer `k`, a letter `letter`, and an integer `repetition`.

Return *the **lexicographically smallest** subsequence of* `s`* of length* `k` *that has the letter* `letter` *appear **at least*** `repetition` *times*. The test cases are generated so that the `letter` appears in `s` **at least** `repetition` times.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A string `a` is **lexicographically smaller** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.

## Constraints
- `1 <= repetition <= k <= s.length <= 5 * 10^4`
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter, and appears in `s` at least `repetition` times.

## Examples
### Example 1
- **Input:** `s = "leet", k = 3, letter = "e", repetition = 1`
- **Output:** `"eet"`
- **Explanation:** There are four subsequences of length 3 that have the letter 'e' appear at least 1 time:
- "lee" (from "

### Example 2
- **Input:** `s = "leetcode", k = 4, letter = "e", repetition = 2`
- **Output:** `"ecde"`
- **Explanation:** "ecde" is the lexicographically smallest subsequence of length 4 that has the letter "e" appear at least 2 times.

### Example 3
- **Input:** `s = "bb", k = 2, letter = "b", repetition = 2`
- **Output:** `"bb"`
- **Explanation:** "bb" is the only subsequence of length 2 that has the letter "b" appear at least 2 times.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest K-Length Subsequence With Occurrences of a Letter**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leet", k = 3, letter = "e", repetition = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"eet"`.
4. **Verification:** There are four subsequences of length 3 that have the letter 'e' appear at least 1 time:
- "lee" (from "

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
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        remaining = s.count(letter)
        need = repetition
        stack = []

        for i, c in enumerate(s):
            # remaining = copies of `letter` in s[i:], including s[i]
            while stack and stack[-1] > c and len(stack) - 1 + (n - i) >= k:
                top = stack[-1]
                if top == letter:
                    if need + 1 > remaining:
                        break
                    need += 1
                stack.pop()

            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    need -= 1
                elif k - len(stack) > max(need, 0):
                    stack.append(c)

            if c == letter:
                remaining -= 1

        return ''.join(stack)
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
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2099-find-subsequence-of-length-k-with-the-largest-sum/)
- [2813. Maximum Elegance of a K-Length Subsequence](../../2501-3000/2813-maximum-elegance-of-a-k-length-subsequence/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0744-find-smallest-letter-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/)
