# LeetCode 2404: Most Frequent Even Element

**LeetCode Problem #2404 — Most Frequent Even Element**
Solve LeetCode Most Frequent Even Element using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Frequent Even Element |
| LeetCode | #2404 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the most frequent even element*.

If there is a tie, return the **smallest** one. If there is no such element, return `-1`.

## Constraints
- `1 <= nums.length <= 2000`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [0,1,2,2,4,4,1]`
- **Output:** `2`
- **Explanation:** The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

### Example 2
- **Input:** `nums = [4,4,4,9,2,4]`
- **Output:** `4`
- **Explanation:** 4 is the even element appears the most.

### Example 3
- **Input:** `nums = [29,47,21,41,13,37,25,7]`
- **Output:** `-1`
- **Explanation:** There is no even element.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Most Frequent Even Element**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,2,4,4,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        max_freq = 0
        best_num = -1
        
        for num in nums:
            if num % 2 == 0:
                freq[num] += 1
                if freq[num] > max_freq or (freq[num] == max_freq and num < best_num):
                    max_freq = freq[num]
                    best_num = num
                    
        return best_num
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1966-frequency-of-the-most-frequent-element/)
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../4001-4500/4198-longest-alternating-subarray-after-removing-at-most-one-element/)
- [3866. First Unique Even Element](../../4001-4500/4252-first-unique-even-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-frequent-even-element/)
