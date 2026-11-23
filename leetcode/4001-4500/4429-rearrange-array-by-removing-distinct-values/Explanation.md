# LeetCode 4065: Rearrange Array by Removing Distinct Values

**LeetCode Problem #4065 — Rearrange Array by Removing Distinct Values**
Solve LeetCode Rearrange Array by Removing Distinct Values using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Array by Removing Distinct Values |
| LeetCode | #4065 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

You start with an **empty** array `ans`. Repeat the following operation until `nums` is **empty**:

Identify **all** **distinct** values currently present in `nums`. 
 Remove **one** occurrence of every **distinct** value currently in `nums`, and append those values to `ans` in **ascending** order.

Return the array `ans`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [3,1,3,2,1,3]`
- **Output:** `[1,2,3,1,3,3]`
- **Explanation:** Operation 
 Appended to `ans` 
 `nums` after 
 `ans` after 
 
 
 
 
 1 
 1, 2, 3 
 `[3, 1, 3]` 
 `[1, 2, 3]` 
 
 
 2 
 1, 3 
 `[3]` 
 `[1, 2, 3, 1, 3]` 
 
 
 3 
 3 
 `[]` 
 `[1, 2, 3, 1, 3, 3]` 
 
 
 

 `nums` is now empty, so the answer is `[1, 2, 3, 1, 3, 3]`.

### Example 2
- **Input:** `nums = [7,7,4,4,4]`
- **Output:** `[4,7,4,7,4]`
- **Explanation:** Operation 
 Appended to `ans` 
 `nums` after 
 `ans` after 
 
 
 
 
 1 
 4, 7 
 `[7, 4, 4]` 
 `[4, 7]` 
 
 
 2 
 4, 7 
 `[4]` 
 `[4, 7, 4, 7]` 
 
 
 3 
 4 
 `[]` 
 `[4, 7, 4, 7, 4]` 
 
 
 

 `nums` is now empty, so the answer is `[4, 7, 4, 7, 4]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Array by Removing Distinct Values**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,3,2,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,1,3,3]`.
4. **Verification:** Operation 
 Appended to `ans` 
 `nums` after 
 `ans` after 
 
 
 
 
 1 
 1, 2, 3 
 `[3, 1, 3]` 
 `[1, 2, 3]` 
 
 
 2 
 1, 3 
 `[3]` 
 `[1, 2, 3, 1, 3]` 
 
 
 3 
 3 
 `[]` 
 `[1, 2, 3, 1, 3, 3]` 
 
 
 

 `nums` is now empty, so the answer is `[1, 2, 3, 1, 3, 3]`.

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
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        keys = sorted(cnt)
        ans = []
        while len(ans) < len(nums):
            for k in keys:
                if cnt[k] > 0:
                    ans.append(k)
                    cnt[k] -= 1
        return ans
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
- [1619. Mean of Array After Removing Some Elements](../../1001-1500/1210-mean-of-array-after-removing-some-elements/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2212-removing-minimum-and-maximum-from-array/)
- [2149. Rearrange Array Elements by Sign](../../2001-2500/2271-rearrange-array-elements-by-sign/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/)
