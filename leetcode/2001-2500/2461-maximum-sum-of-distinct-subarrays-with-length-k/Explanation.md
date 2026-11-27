# LeetCode 2461: Maximum Sum of Distinct Subarrays With Length K

**LeetCode Problem #2461 — Maximum Sum of Distinct Subarrays With Length K**
Solve LeetCode Maximum Sum of Distinct Subarrays With Length K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Distinct Subarrays With Length K |
| LeetCode | #2461 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`. Find the maximum subarray sum of all the subarrays of `nums` that meet the following conditions:

The length of the subarray is `k`, and 
 All the elements of the subarray are **distinct**.

Return *the maximum subarray sum of all the subarrays that meet the conditions**.* If no subarray meets the conditions, return `0`.

*A **subarray** is a contiguous non-empty sequence of elements within an array.*

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,5,4,2,9,9,9], k = 3`
- **Output:** `15`
- **Explanation:** The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

### Example 2
- **Input:** `nums = [4,4,4], k = 3`
- **Output:** `0`
- **Explanation:** The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Sum of Distinct Subarrays With Length K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,4,2,9,9,9], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

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
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        curr_sum = 0
        max_sum = 0
        
        for i, val in enumerate(nums):
            curr_sum += val
            freq[val] += 1
            
            if i >= k:
                out_val = nums[i - k]
                curr_sum -= out_val
                freq[out_val] -= 1
                if freq[out_val] == 0:
                    del freq[out_val]
                    
            if i >= k - 1 and len(freq) == k and curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum
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
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../3501-4000/3795-minimum-subarray-length-with-distinct-sum-at-least-k/)
- [3473. Sum of K Subarrays With Length at Least M](../../3001-3500/3473-sum-of-k-subarrays-with-length-at-least-m/)
- [3381. Maximum Subarray Sum With Length Divisible by K](../../3001-3500/3381-maximum-subarray-sum-with-length-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)
