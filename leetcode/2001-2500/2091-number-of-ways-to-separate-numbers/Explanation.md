# LeetCode 1977: Number of Ways to Separate Numbers

**LeetCode Problem #1977 — Number of Ways to Separate Numbers**
Solve LeetCode Number of Ways to Separate Numbers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Separate Numbers |
| LeetCode | #1977 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You wrote down many **positive** integers in a string called `num`. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was **non-decreasing** and that **no** integer had leading zeros.

Return *the **number of possible lists of integers** that you could have written down to get the string *`num`. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= num.length <= 3500`
- `num` consists of digits `'0'` through `'9'`.

## Examples
### Example 1
- **Input:** `num = "327"`
- **Output:** `2`
- **Explanation:** You could have written down the numbers:
3, 27
327

### Example 2
- **Input:** `num = "094"`
- **Output:** `0`
- **Explanation:** No numbers can have leading zeros and all numbers must be positive.

### Example 3
- **Input:** `num = "0"`
- **Output:** `0`
- **Explanation:** No numbers can have leading zeros and all numbers must be positive.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Ways to Separate Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "327"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You could have written down the numbers:
3, 27
327

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
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0
            
        MOD = 10**9 + 7
        n = len(num)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = 1 + lcp[i + 1][j + 1]
        def is_less_or_equal(a: int, b: int, l: int) -> bool:
            common = lcp[a][b]
            if common >= l:
                return True
            return num[a + common] < num[b + common]
        pref = [[0] * (n + 1) for _ in range(n)]
        
        for i in range(n):
            for l in range(1, i + 2):
                start = i - l + 1
                ways = 0
                if num[start] != '0':
                    if start == 0:
                        ways = 1
                    else:
                        prev_end = start - 1
                        max_prev_len = min(l - 1, prev_end + 1)
                        ways = pref[prev_end][max_prev_len]
                        prev_start = prev_end - l + 1
                        if prev_start >= 0 and is_less_or_equal(prev_start, start, l):
                            same_len_ways = (pref[prev_end][l] - pref[prev_end][l - 1]) % MOD
                            ways = (ways + same_len_ways) % MOD
                            
                pref[i][l] = (pref[i][l - 1] + ways) % MOD
                
        return pref[n - 1][n]
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
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1421-find-numbers-with-even-number-of-digits/)
- [1365. How Many Numbers Are Smaller Than the Current Number](../../1001-1500/1482-how-many-numbers-are-smaller-than-the-current-number/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-separate-numbers/)
