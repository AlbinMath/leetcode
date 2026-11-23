# LeetCode 3890: Integers With Multiple Sum of Two Cubes

**LeetCode Problem #3890 — Integers With Multiple Sum of Two Cubes**
Solve LeetCode Integers With Multiple Sum of Two Cubes using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Integers With Multiple Sum of Two Cubes |
| LeetCode | #3890 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`.

An integer `x` is considered **good** if there exist **at least** two **distinct** pairs `(a, b)` such that:

`a` and `b` are positive integers. 
 `a <= b` 
 `x = a^3 + b^3`

Return an array containing all good integers **less than or equal to** `n`, sorted in ascending order.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 4104`
- **Output:** `[1729,4104]`
- **Explanation:** Among integers less than or equal to 4104, the good integers are: 

 
 1729: `1^3 + 12^3 = 1729` and `9^3 + 10^3 = 1729`. 
 4104: `2^3 + 16^3 = 4104` and `9^3 + 15^3 = 4104`. 
 

 Thus, the answer is `[1729, 4104]`.

### Example 2
- **Input:** `n = 578`
- **Output:** `[]`
- **Explanation:** There are no good integers less than or equal to 578, so the answer is an empty array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Integers With Multiple Sum of Two Cubes**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4104`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1729,4104]`.
4. **Verification:** Among integers less than or equal to 4104, the good integers are: 

 
 1729: `1^3 + 12^3 = 1729` and `9^3 + 10^3 = 1729`. 
 4104: `2^3 + 16^3 = 4104` and `9^3 + 15^3 = 4104`. 
 

 Thus, the answer is `[1729, 4104]`.

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
from typing import List
from collections import Counter

class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        cnt = Counter()
        a = 1
        while 2 * a ** 3 <= n:          # smallest sum with this a is a^3 + a^3
            b = a
            while True:
                s = a ** 3 + b ** 3
                if s > n:
                    break
                cnt[s] += 1
                b += 1
            a += 1
        return sorted(s for s, c in cnt.items() if c >= 2)
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
- [371. Sum of Two Integers](../../0001-0500/0371-sum-of-two-integers/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1440-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/)
