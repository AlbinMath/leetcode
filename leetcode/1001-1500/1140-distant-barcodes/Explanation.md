# LeetCode 1054: Distant Barcodes

**LeetCode Problem #1054 — Distant Barcodes**
Solve LeetCode Distant Barcodes using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distant Barcodes |
| LeetCode | #1054 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In a warehouse, there is a row of barcodes, where the `i^th` barcode is `barcodes[i]`.

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

## Constraints
- `1 <= barcodes.length <= 10000`
- `1 <= barcodes[i] <= 10000`

## Examples
### Example 1
- **Input:** `barcodes = [1,1,1,2,2,2]`
- **Output:** `[2,1,2,1,2,1]`

### Example 2
- **Input:** `barcodes = [1,1,1,1,2,2,3,3]`
- **Output:** `[1,3,1,3,1,2,1,2]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Distant Barcodes**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `barcodes = [1,1,1,2,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,2,1,2,1]`.

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
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        cnt = Counter(barcodes)
        ordered = []
        for v, c in cnt.most_common():
            ordered.extend([v] * c)

        n = len(barcodes)
        res = [0] * n
        res[0::2] = ordered[:(n + 1) // 2]
        res[1::2] = ordered[(n + 1) // 2:]
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
- [4051. Count Subarrays with Distant Sums](../../4001-4500/4317-count-subarrays-with-distant-sums/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distant-barcodes/)
