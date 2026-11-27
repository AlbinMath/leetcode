# LeetCode 1481: Least Number of Unique Integers after K Removals

**LeetCode Problem #1481 — Least Number of Unique Integers after K Removals**
Solve LeetCode Least Number of Unique Integers after K Removals using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Least Number of Unique Integers after K Removals |
| LeetCode | #1481 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr` and an integer `k`. Find the *least number of unique integers* after removing **exactly** `k` elements .

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^9`
- `0 <= k <= arr.length`

## Examples
### Example 1
- **Input:** `arr = [5,5,4], k = 1`
- **Output:** `1`
- **Explanation:** : Remove the single 4, only 5 is left.

### Example 2
- **Input:** `arr = [4,3,1,1,3,3,2], k = 3`
- **Output:** `2`
- **Explanation:** : Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Least Number of Unique Integers after K Removals**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [5,5,4], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** : Remove the single 4, only 5 is left.

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
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freqs = sorted(Counter(arr).values())
        unique = len(freqs)
        for f in freqs:
            if k >= f:
                k -= f
                unique -= 1
            else:
                break
        return unique
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
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [3621. Number of Integers With Popcount-Depth Equal to K I](../../3501-4000/3621-number-of-integers-with-popcount-depth-equal-to-k-i/)
- [3624. Number of Integers With Popcount-Depth Equal to K II](../../3501-4000/3624-number-of-integers-with-popcount-depth-equal-to-k-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)
