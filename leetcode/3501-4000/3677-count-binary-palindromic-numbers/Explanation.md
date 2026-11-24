# LeetCode 3677: Count Binary Palindromic Numbers

**LeetCode Problem #3677 — Count Binary Palindromic Numbers**
Solve LeetCode Count Binary Palindromic Numbers using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Binary Palindromic Numbers |
| LeetCode | #3677 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **non-negative** integer `n`.

A **non-negative** integer is called **binary-palindromic** if its binary representation (written without leading zeros) reads the same forward and backward.

Return the number of integers ` k ` such that `0 <= k <= n` and the binary representation of ` k ` is a palindrome.

**Note:** The number 0 is considered binary-palindromic, and its representation is `"0"`.

## Constraints
- `0 <= n <= 10^15`

## Examples
### Example 1
- **Input:** `n = 9`
- **Output:** `6`
- **Explanation:** The integers `k` in the range `[0, 9]` whose binary representations are palindromes are: 

 
 `0 &rarr; "0"` 
 `1 &rarr; "1"` 
 `3 &rarr; "11"` 
 `5 &rarr; "101"` 
 `7 &rarr; "111"` 
 `9 &rarr; "1001"` 
 

 All other values in `[0, 9]` have non-palindromic binary forms. Therefore, the count is 6.

### Example 2
- **Input:** `n = 0`
- **Output:** `1`
- **Explanation:** Since `"0"` is a palindrome, the count is 1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Binary Palindromic Numbers**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 9`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The integers `k` in the range `[0, 9]` whose binary representations are palindromes are: 

 
 `0 &rarr; "0"` 
 `1 &rarr; "1"` 
 `3 &rarr; "11"` 
 `5 &rarr; "101"` 
 `7 &rarr; "111"` 
 `9 &rarr; "1001"` 
 

 All other values in `[0, 9]` have non-palindromic binary forms. Therefore, the count is 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def countBinaryPalindromes(self, n):
        if n == 0:
            return 1
        B = n.bit_length()
        total = 1  # the number 0

        # all palindromes with fewer bits than n
        for L in range(1, B):
            total += 1 << ((L + 1) // 2 - 1)

        half = (B + 1) // 2

        def build(h):
            s = bin(h)[2:]
            tail = s[::-1] if B % 2 == 0 else s[:-1][::-1]
            return int(s + tail, 2)

        lo, hi = 1 << (half - 1), (1 << half) - 1
        # find the largest h with build(h) <= n
        ans = lo - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if build(mid) <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        total += ans - (1 << (half - 1)) + 1
        return total
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [1022. Sum of Root To Leaf Binary Numbers](../../1001-1500/1022-sum-of-root-to-leaf-binary-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-binary-palindromic-numbers/)
