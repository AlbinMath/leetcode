# LeetCode 28: Find the Index of the First Occurrence in a String

**LeetCode Problem #28 — Find the Index of the First Occurrence in a String**
Solve LeetCode Find the Index of the First Occurrence in a String using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Index of the First Occurrence in a String |
| LeetCode | #28 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Constraints
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Examples
### Example 1
- **Input:** `haystack = "sadbutsad", needle = "sad"`
- **Output:** `0`
- **Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

### Example 2
- **Input:** `haystack = "leetcode", needle = "leeto"`
- **Output:** `-1`
- **Explanation:** "leeto" did not occur in "leetcode", so we return -1.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Find the Index of the First Occurrence in a String**, we observe the problem requirements and utilize the **Stack & Queue** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `haystack = "sadbutsad", needle = "sad"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [2108. Find First Palindromic String in the Array](../../2001-2500/2108-find-first-palindromic-string-in-the-array/)
- [3303. Find the Occurrence of First Almost Equal Substring](../../3001-3500/3303-find-the-occurrence-of-first-almost-equal-substring/)
- [724. Find Pivot Index](../../0501-1000/0724-find-pivot-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
