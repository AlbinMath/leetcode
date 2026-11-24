# LeetCode 3828: Final Element After Subarray Deletions

**LeetCode Problem #3828 — Final Element After Subarray Deletions**
Solve LeetCode Final Element After Subarray Deletions using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Final Element After Subarray Deletions |
| LeetCode | #3828 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Two players, Alice and Bob, play a game in turns, with Alice playing first.

In each turn, the current player chooses any ** subarray ** `nums[l..r]` such that `r - l + 1 < m`, where `m` is the **current length** of the array. 
 The selected **subarray is removed**, and the remaining elements are **concatenated** to form the new array. 
 The game continues until **only one** element remains.

Alice aims to **maximize** the final element, while Bob aims to **minimize** it. Assuming both play optimally, return the value of the final remaining element.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,5,2]`
- **Output:** `2`
- **Explanation:** One valid optimal strategy: 

 
 Alice removes `[1]`, array becomes `[5, 2]`. 
 Bob removes `[5]`, array becomes `[2]`​​​​​​​. Thus, the answer is 2.

### Example 2
- **Input:** `nums = [3,7]`
- **Output:** `7`
- **Explanation:** Alice removes `[3]`, leaving the array `[7]`. Since Bob cannot play a turn now, the answer is 7.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Final Element After Subarray Deletions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One valid optimal strategy: 

 
 Alice removes `[1]`, array becomes `[5, 2]`. 
 Bob removes `[5]`, array becomes `[2]`​​​​​​​. Thus, the answer is 2.

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
from typing import List

class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])
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
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../3501-4000/3830-longest-alternating-subarray-after-removing-at-most-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-element-after-subarray-deletions/)
