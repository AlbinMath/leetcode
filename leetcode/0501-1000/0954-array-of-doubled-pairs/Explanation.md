# LeetCode 954: Array of Doubled Pairs

**LeetCode Problem #954 — Array of Doubled Pairs**
Solve LeetCode Array of Doubled Pairs using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Array of Doubled Pairs |
| LeetCode | #954 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array of even length `arr`, return `true`* if it is possible to reorder *`arr`* such that *`arr[2 * i + 1] = 2 * arr[2 * i]`* for every *`0 <= i < len(arr) / 2`*, or *`false`* otherwise*.

## Constraints
- `2 <= arr.length <= 3 * 10^4`
- `arr.length` is even.
- `-10^5 <= arr[i] <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [3,1,3,6]`
- **Output:** `false`

### Example 2
- **Input:** `arr = [2,1,2,6]`
- **Output:** `false`

### Example 3
- **Input:** `arr = [4,-2,2,-4]`
- **Output:** `true`
- **Explanation:** We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Array of Doubled Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,1,3,6]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.

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
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for x in sorted(counts, key=abs):
            if counts[x] > counts[2 * x]:
                return False
            counts[2 * x] -= counts[x]
            
        return True
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
- [532. K-diff Pairs in an Array](../../0501-1000/0532-k-diff-pairs-in-an-array/)
- [629. K Inverse Pairs Array](../../0501-1000/0629-k-inverse-pairs-array/)
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/array-of-doubled-pairs/)
