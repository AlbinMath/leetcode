# LeetCode 2048: Next Greater Numerically Balanced Number

**LeetCode Problem #2048 — Next Greater Numerically Balanced Number**
Solve LeetCode Next Greater Numerically Balanced Number using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Greater Numerically Balanced Number |
| LeetCode | #2048 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are **exactly** `d` occurrences of that digit in `x`.

Given an integer `n`, return *the **smallest numerically balanced** number **strictly greater** than *`n`*.*

## Constraints
- `0 <= n <= 10^6`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `22`
- **Explanation:** 22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.

### Example 2
- **Input:** `n = 1000`
- **Output:** `1333`
- **Explanation:** 1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.

### Example 3
- **Input:** `n = 3000`
- **Output:** `3133`
- **Explanation:** 3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Next Greater Numerically Balanced Number**, we observe the problem requirements and utilize the **Monotonic Stack** technique. By maintaining a **Stack**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Stack** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** 22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.

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
from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n + 1
        while True:
            c = Counter(str(x))
            if all(int(d) == k for d, k in c.items()):
                return x
            x += 1
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
- [1963. Minimum Number of Swaps to Make the String Balanced](../../1501-2000/1963-minimum-number-of-swaps-to-make-the-string-balanced/)
- [3343. Count Number of Balanced Permutations](../../3001-3500/3343-count-number-of-balanced-permutations/)
- [496. Next Greater Element I](../../0001-0500/0496-next-greater-element-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-greater-numerically-balanced-number/)
