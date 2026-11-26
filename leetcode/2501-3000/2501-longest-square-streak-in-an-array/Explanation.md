# LeetCode 2501: Longest Square Streak in an Array

**LeetCode Problem #2501 — Longest Square Streak in an Array**
Solve LeetCode Longest Square Streak in an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Square Streak in an Array |
| LeetCode | #2501 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. A subsequence of `nums` is called a **square streak** if:

The length of the subsequence is at least `2`, and 
 **after** sorting the subsequence, each element (except the first element) is the **square** of the previous number.

Return* the length of the **longest square streak** in *`nums`*, or return *`-1`* if there is no **square streak**.*

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `2 <= nums.length <= 10^5`
- `2 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,3,6,16,8,2]`
- **Output:** `3`
- **Explanation:** Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.

### Example 2
- **Input:** `nums = [2,3,5,6,7]`
- **Output:** `-1`
- **Explanation:** There is no square streak in nums so return -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Square Streak in an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,6,16,8,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.

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
from math import isqrt

class Solution:
    def longestSquareStreak(self, nums):
        dp = {}
        best = 0
        for v in sorted(set(nums)):
            r = isqrt(v)
            if r * r == v and r in dp:
                dp[v] = dp[r] + 1
                best = max(best, dp[v])
            else:
                dp[v] = 1
        return best if best >= 2 else -1
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
- [845. Longest Mountain in Array](../../0501-1000/0845-longest-mountain-in-array/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-square-streak-in-an-array/)
