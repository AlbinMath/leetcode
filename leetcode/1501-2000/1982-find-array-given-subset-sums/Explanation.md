# LeetCode 1982: Find Array Given Subset Sums

**LeetCode Problem #1982 — Find Array Given Subset Sums**
Solve LeetCode Find Array Given Subset Sums using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Array Given Subset Sums |
| LeetCode | #1982 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` representing the length of an unknown array that you are trying to recover. You are also given an array `sums` containing the values of all `2^n` **subset sums** of the unknown array (in no particular order).

Return *the array *`ans`* of length *`n`* representing the unknown array. If **multiple** answers exist, return **any** of them*.

An array `sub` is a **subset** of an array `arr` if `sub` can be obtained from `arr` by deleting some (possibly zero or all) elements of `arr`. The sum of the elements in `sub` is one possible **subset sum** of `arr`. The sum of an empty array is considered to be `0`.

**Note:** Test cases are generated such that there will **always** be at least one correct answer.

## Constraints
- `1 <= n <= 15`
- `sums.length == 2^n`
- `-10^4 <= sums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `n = 3, sums = [-3,-2,-1,0,0,1,2,3]`
- **Output:** `[1,2,-3]`
- **Explanation:** [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.

### Example 2
- **Input:** `n = 2, sums = [0,0,0,0]`
- **Output:** `[0,0]`
- **Explanation:** The only correct answer is [0,0].

### Example 3
- **Input:** `n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]`
- **Output:** `[0,-1,4,5]`
- **Explanation:** [0,-1,4,5] is able to achieve the given subset sums.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Array Given Subset Sums**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, sums = [-3,-2,-1,0,0,1,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,-3]`.
4. **Verification:** [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.

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
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        sums.sort()
        ans = []
        
        for _ in range(n):
            d = sums[1] - sums[0]
            freq = Counter(sums)
            without_d = []
            with_d = []
            
            for x in sums:
                if freq[x] > 0:
                    freq[x] -= 1
                    freq[x + d] -= 1
                    without_d.append(x)
                    with_d.append(x + d)
            
            if 0 in without_d:
                ans.append(d)
                sums = without_d
            else:
                ans.append(-d)
                sums = with_d
                
        return ans
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
- [3006. Find Beautiful Indices in the Given Array I](../../3001-3500/3006-find-beautiful-indices-in-the-given-array-i/)
- [3008. Find Beautiful Indices in the Given Array II](../../3001-3500/3008-find-beautiful-indices-in-the-given-array-ii/)
- [1605. Find Valid Matrix Given Row and Column Sums](../../1501-2000/1605-find-valid-matrix-given-row-and-column-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-array-given-subset-sums/)
