# LeetCode 1785: Minimum Elements to Add to Form a Given Sum

**LeetCode Problem #1785 — Minimum Elements to Add to Form a Given Sum**
Solve LeetCode Minimum Elements to Add to Form a Given Sum using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Elements to Add to Form a Given Sum |
| LeetCode | #1785 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and two integers `limit` and `goal`. The array `nums` has an interesting property that `abs(nums[i]) <= limit`.

Return *the minimum number of elements you need to add to make the sum of the array equal to *`goal`. The array must maintain its property that `abs(nums[i]) <= limit`.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= limit <= 10^6`
- `-limit <= nums[i] <= limit`
- `-10^9 <= goal <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,-1,1], limit = 3, goal = -4`
- **Output:** `2`
- **Explanation:** You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.

### Example 2
- **Input:** `nums = [1,-10,9,1], limit = 100, goal = 0`
- **Output:** `1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Elements to Add to Form a Given Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-1,1], limit = 3, goal = -4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.

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

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(goal - sum(nums))
        return (diff + limit - 1) // limit
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
- [2835. Minimum Operations to Form Subsequence With Target Sum](../../2501-3000/2835-minimum-operations-to-form-subsequence-with-target-sum/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1001-1500/1498-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/)
