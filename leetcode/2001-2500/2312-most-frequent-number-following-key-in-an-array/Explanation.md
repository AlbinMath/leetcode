# LeetCode 2190: Most Frequent Number Following Key In an Array

**LeetCode Problem #2190 — Most Frequent Number Following Key In an Array**
Solve LeetCode Most Frequent Number Following Key In an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Frequent Number Following Key In an Array |
| LeetCode | #2190 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.** **You are also given an integer `key`, which is present in `nums`.

For every unique integer `target` in `nums`, **count** the number of times `target` immediately follows an occurrence of `key` in `nums`. In other words, count the number of indices `i` such that:

`0 <= i <= nums.length - 2`, 
 `nums[i] == key` and, 
 `nums[i + 1] == target`.

Return *the *`target`* with the **maximum** count*. The test cases will be generated such that the `target` with maximum count is unique.

## Constraints
- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- The test cases will be generated such that the answer is unique.

## Examples
### Example 1
- **Input:** `nums = [1,100,200,1,100], key = 1`
- **Output:** `100`
- **Explanation:** For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
No other integers follow an occurrence of key, so we return 100.

### Example 2
- **Input:** `nums = [2,2,2,2,3], key = 2`
- **Output:** `2`
- **Explanation:** For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Most Frequent Number Following Key In an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,100,200,1,100], key = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `100`.
4. **Verification:** For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
No other integers follow an occurrence of key, so we return 100.

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

class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counts = defaultdict(int)
        max_count = 0
        best_target = -1
        
        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                counts[target] += 1
                if counts[target] > max_count:
                    max_count = counts[target]
                    best_target = target
                    
        return best_target
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
- [508. Most Frequent Subtree Sum](../../0501-1000/0508-most-frequent-subtree-sum/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1710-find-servers-that-handled-most-number-of-requests/)
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1966-frequency-of-the-most-frequent-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/)
