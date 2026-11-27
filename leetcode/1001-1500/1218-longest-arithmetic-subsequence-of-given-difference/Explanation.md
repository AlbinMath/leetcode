# LeetCode 1218: Longest Arithmetic Subsequence of Given Difference

**LeetCode Problem #1218 — Longest Arithmetic Subsequence of Given Difference**
Solve LeetCode Longest Arithmetic Subsequence of Given Difference using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Arithmetic Subsequence of Given Difference |
| LeetCode | #1218 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence in `arr` which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals `difference`.

A **subsequence** is a sequence that can be derived from `arr` by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i], difference <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4], difference = 1`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is [1,2,3,4].

### Example 2
- **Input:** `arr = [1,3,5,7], difference = 1`
- **Output:** `1`
- **Explanation:** The longest arithmetic subsequence is any single element.

### Example 3
- **Input:** `arr = [1,5,7,8,5,3,4,2,1], difference = -2`
- **Output:** `4`
- **Explanation:** The longest arithmetic subsequence is [7,5,3,1].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Arithmetic Subsequence of Given Difference**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4], difference = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest arithmetic subsequence is [1,2,3,4].

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
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        max_len = 0
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
            if dp[num] > max_len:
                max_len = dp[num]
                
        return max_len
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
- [1027. Longest Arithmetic Subsequence](../../1001-1500/1027-longest-arithmetic-subsequence/)
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [446. Arithmetic Slices II - Subsequence](../../0001-0500/0446-arithmetic-slices-ii-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)
