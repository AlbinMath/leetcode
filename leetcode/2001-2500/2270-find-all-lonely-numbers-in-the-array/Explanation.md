# LeetCode 2150: Find All Lonely Numbers in the Array

**LeetCode Problem #2150 — Find All Lonely Numbers in the Array**
Solve LeetCode Find All Lonely Numbers in the Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Lonely Numbers in the Array |
| LeetCode | #2150 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. A number `x` is **lonely** when it appears only **once**, and no **adjacent** numbers (i.e. `x + 1` and `x - 1)` appear in the array.

Return ***all** lonely numbers in *`nums`. You may return the answer in **any order**.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [10,6,5,8]`
- **Output:** `[10,8]`
- **Explanation:** - 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.

### Example 2
- **Input:** `nums = [1,3,5,3]`
- **Output:** `[1,5]`
- **Explanation:** - 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find All Lonely Numbers in the Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,6,5,8]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[10,8]`.
4. **Verification:** - 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.

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
from collections import Counter

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        
        return [
            num for num, count in freq.items()
            if count == 1 and (num - 1) not in freq and (num + 1) not in freq
        ]
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
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/)
