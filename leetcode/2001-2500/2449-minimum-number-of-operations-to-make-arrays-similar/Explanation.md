# LeetCode 2449: Minimum Number of Operations to Make Arrays Similar

**LeetCode Problem #2449 — Minimum Number of Operations to Make Arrays Similar**
Solve LeetCode Minimum Number of Operations to Make Arrays Similar using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Make Arrays Similar |
| LeetCode | #2449 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two positive integer arrays `nums` and `target`, of the same length.

In one operation, you can choose any two **distinct** indices `i` and `j` where `0 <= i, j < nums.length` and:

set `nums[i] = nums[i] + 2` and 
 set `nums[j] = nums[j] - 2`.

Two arrays are considered to be **similar** if the frequency of each element is the same.

Return *the minimum number of operations required to make *`nums`* similar to *`target`. The test cases are generated such that `nums` can always be similar to `target`.

## Constraints
- `n == nums.length == target.length`
- `1 <= n <= 10^5`
- `1 <= nums[i], target[i] <= 10^6`
- It is possible to make `nums` similar to `target`.

## Examples
### Example 1
- **Input:** `nums = [8,12,6], target = [2,14,10]`
- **Output:** `2`
- **Explanation:** It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.

### Example 2
- **Input:** `nums = [1,2,5], target = [4,1,3]`
- **Output:** `1`
- **Explanation:** We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].

### Example 3
- **Input:** `nums = [1,1,1,1,1], target = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** The array nums is already similiar to target.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Operations to Make Arrays Similar**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,12,6], target = [2,14,10]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.

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
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def key(arr):
            odd = sorted(x for x in arr if x % 2)
            even = sorted(x for x in arr if x % 2 == 0)
            return even, odd

        ne, no = key(nums)
        te, to = key(target)
        total = 0
        for a, b in zip(ne, te):
            total += abs(a - b)
        for a, b in zip(no, to):
            total += abs(a - b)
        return total // 4
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
- [1775. Equal Sum Arrays With Minimum Number of Operations](../../1501-2000/1775-equal-sum-arrays-with-minimum-number-of-operations/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2009-minimum-number-of-operations-to-make-array-continuous/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/)
