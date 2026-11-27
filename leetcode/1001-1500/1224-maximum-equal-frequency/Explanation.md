# LeetCode 1224: Maximum Equal Frequency

**LeetCode Problem #1224 — Maximum Equal Frequency**
Solve LeetCode Maximum Equal Frequency using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Equal Frequency |
| LeetCode | #1224 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array `nums` of positive integers, return the longest possible length of an array prefix of `nums`, such that it is possible to remove **exactly one** element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,2,1,1,5,3,3,5]`
- **Output:** `7`
- **Explanation:** For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

### Example 2
- **Input:** `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`
- **Output:** `13`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Equal Frequency**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,1,1,5,3,3,5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

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
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = defaultdict(int)  # number -> occurrences
        freq = defaultdict(int)   # occurrences -> count of distinct numbers with this frequency
        max_freq = 0
        ans = 0
        
        for i, num in enumerate(nums):
            prev_f = count[num]
            if prev_f > 0:
                freq[prev_f] -= 1
                
            curr_f = prev_f + 1
            count[num] = curr_f
            freq[curr_f] += 1
            
            if curr_f > max_freq:
                max_freq = curr_f
                
            prefix_len = i + 1
            
            # Check the 3 valid prefix conditions
            case1 = (max_freq == 1)
            case2 = (freq[max_freq] * max_freq + 1 == prefix_len)
            case3 = (freq[max_freq] == 1 and max_freq + freq[max_freq - 1] * (max_freq - 1) == prefix_len)
            
            if case1 or case2 or case3:
                ans = prefix_len
                
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
- [895. Maximum Frequency Stack](../../0501-1000/0895-maximum-frequency-stack/)
- [3005. Count Elements With Maximum Frequency](../../3001-3500/3005-count-elements-with-maximum-frequency/)
- [3144. Minimum Substring Partition of Equal Character Frequency](../../3001-3500/3144-minimum-substring-partition-of-equal-character-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-equal-frequency/)
