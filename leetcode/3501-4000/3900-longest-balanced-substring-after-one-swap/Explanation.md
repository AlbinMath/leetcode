# LeetCode 3900: Longest Balanced Substring After One Swap

**LeetCode Problem #3900 — Longest Balanced Substring After One Swap**
Solve LeetCode Longest Balanced Substring After One Swap using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Balanced Substring After One Swap |
| LeetCode | #3900 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary string `s` consisting only of characters `'0'` and `'1'`.

A string is **balanced** if it contains an **equal** number of `'0'`s and `'1'`s.

You can perform **at most one** swap between any two characters in `s`. Then, you select a **balanced** substring from `s`.

Return an integer representing the **maximum** length of the **balanced** substring you can select.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of the characters `'0'` and `'1'`.

## Examples
### Example 1
- **Input:** `s = "100001"`
- **Output:** `4`
- **Explanation:** Swap "10

### Example 2
- **Input:** `s = "111"`
- **Output:** `0`
- **Explanation:** Choose not to perform any swaps. 
 Select the empty substring, which is balanced because it has zero `'0'`s and zero `'1'`s.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Balanced Substring After One Swap**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "100001"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Swap "10

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        T1 = s.count('1')
        T0 = n - T1

        P = [0] * (n + 1)
        pos = defaultdict(list)
        pos[0].append(0)
        for i, ch in enumerate(s):
            P[i + 1] = P[i] + (1 if ch == '1' else -1)
            pos[P[i + 1]].append(i + 1)

        res = 0
        for d, cap in ((0, n), (2, 2 * T0), (-2, 2 * T1)):
            for j in range(1, n + 1):
                lst = pos.get(P[j] - d)
                if not lst:
                    continue
                lo = max(0, j - cap)
                k = bisect_left(lst, lo)
                if k < len(lst) and lst[k] < j:
                    res = max(res, j - lst[k])
        return res
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1156. Swap For Longest Repeated Character Substring](../../1001-1500/1156-swap-for-longest-repeated-character-substring/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [2213. Longest Substring of One Repeating Character](../../2001-2500/2213-longest-substring-of-one-repeating-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-balanced-substring-after-one-swap/)
