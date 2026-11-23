# LeetCode 564: Find the Closest Palindrome

**LeetCode Problem #564 — Find the Closest Palindrome**
Solve LeetCode Find the Closest Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Closest Palindrome |
| LeetCode | #564 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `n` representing an integer, return *the closest integer (not including itself), which is a palindrome*. If there is a tie, return ***the smaller one***.

The closest is defined as the absolute difference minimized between two integers.

## Constraints
- `1 <= n.length <= 18`
- `n` consists of only digits.
- `n` does not have leading zeros.
- `n` is representing an integer in the range `[1, 10^18 - 1]`.

## Examples
### Example 1
- **Input:** `n = "123"`
- **Output:** `"121"`

### Example 2
- **Input:** `n = "1"`
- **Output:** `"0"`
- **Explanation:** 0 and 2 are the closest palindromes but we return the smallest which is 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Closest Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = "123"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"121"`.

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
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        num = int(n)

        # candidates where the digit count changes
        candidates = {10 ** (L - 1) - 1, 10 ** L + 1}

        prefix = int(n[:(L + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)
            if L % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]  # skip the middle digit when mirroring
            candidates.add(int(pal))

        candidates.discard(num)  # must not return n itself
        return str(min(candidates, key=lambda x: (abs(x - num), x)))
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
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [1521. Find a Value of a Mysterious Function Closest to Target](../../1501-2000/1645-find-a-value-of-a-mysterious-function-closest-to-target/)
- [2359. Find Closest Node to Given Two Nodes](../../2001-2500/2438-find-closest-node-to-given-two-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-closest-palindrome/)
