# LeetCode 1090: Largest Values From Labels

**LeetCode Problem #1090 — Largest Values From Labels**
Solve LeetCode Largest Values From Labels using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Values From Labels |
| LeetCode | #1090 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given `n` item's value and label as two integer arrays `values` and `labels`. You are also given two integers `numWanted` and `useLimit`.

Your task is to find a subset of items with the **maximum sum** of their values such that:

The number of items is **at most** `numWanted`. 
 The number of items with the same label is **at most** `useLimit`.

Return the maximum sum.

## Constraints
- `n == values.length == labels.length`
- `1 <= n <= 2 * 10^4`
- `0 <= values[i], labels[i] <= 2 * 10^4`
- `1 <= numWanted, useLimit <= n`

## Examples
### Example 1
- **Input:** `values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1`
- **Output:** `9`
- **Explanation:** The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.

### Example 2
- **Input:** `values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2`
- **Output:** `12`
- **Explanation:** The subset chosen is the first, second, and third items with the sum of values 5 + 4 + 3.

### Example 3
- **Input:** `values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1`
- **Output:** `16`
- **Explanation:** The subset chosen is the first and fourth items with the sum of values 9 + 7.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Largest Values From Labels**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.

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
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int],
                              numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used = defaultdict(int)
        total = taken = 0
        for v, l in items:
            if taken == numWanted:
                break
            if used[l] < useLimit:
                used[l] += 1
                total += v
                taken += 1
        return total
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
- [3403. Find the Lexicographically Largest String From the Box I](../../3001-3500/3403-find-the-lexicographically-largest-string-from-the-box-i/)
- [3770. Largest Prime from Consecutive Prime Sum](../../3501-4000/3770-largest-prime-from-consecutive-prime-sum/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-values-from-labels/)
