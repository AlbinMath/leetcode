# LeetCode 2341: Maximum Number of Pairs in Array

**LeetCode Problem #2341 — Maximum Number of Pairs in Array**
Solve LeetCode Maximum Number of Pairs in Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Pairs in Array |
| LeetCode | #2341 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. In one operation, you may do the following:

Choose **two** integers in `nums` that are **equal**. 
 Remove both integers from `nums`, forming a **pair**.

The operation is done on `nums` as many times as possible.

Return *a **0-indexed** integer array *`answer`* of size *`2`* where *`answer[0]`* is the number of pairs that are formed and *`answer[1]`* is the number of leftover integers in *`nums`* after doing the operation as many times as possible*.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,1,3,2,2]`
- **Output:** `[3,1]`
- **Explanation:** Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

### Example 2
- **Input:** `nums = [1,1]`
- **Output:** `[1,0]`
- **Explanation:** Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.

### Example 3
- **Input:** `nums = [0]`
- **Output:** `[0,1]`
- **Explanation:** No pairs can be formed, and there is 1 number leftover in nums.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Number of Pairs in Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,1,3,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1]`.
4. **Verification:** Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

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
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        pairs = 0
        leftovers = 0
        
        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2
            
        return [pairs, leftovers]
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
- [2025. Maximum Number of Ways to Partition an Array](../../2001-2500/2025-maximum-number-of-ways-to-partition-an-array/)
- [2744. Find Maximum Number of String Pairs](../../2501-3000/2744-find-maximum-number-of-string-pairs/)
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-pairs-in-array/)
