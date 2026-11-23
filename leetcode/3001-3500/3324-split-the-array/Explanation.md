# LeetCode 3046: Split the Array

**LeetCode Problem #3046 — Split the Array**
Solve LeetCode Split the Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split the Array |
| LeetCode | #3046 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of **even** length. You have to split the array into two parts `nums1` and `nums2` such that:

`nums1.length == nums2.length == nums.length / 2`. 
 `nums1` should contain **distinct **elements. 
 `nums2` should also contain **distinct** elements.

Return `true`* if it is possible to split the array, and *`false` *otherwise**.*

## Constraints
- `1 <= nums.length <= 100`
- `nums.length % 2 == 0 `
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,2,3,4]`
- **Output:** `true`
- **Explanation:** One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

### Example 2
- **Input:** `nums = [1,1,1,1]`
- **Output:** `false`
- **Explanation:** The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split the Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

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
class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        freq = [0] * 101
        
        for num in nums:
            freq[num] += 1
            if freq[num] > 2:
                return False
                
        return True
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
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [805. Split Array With Same Average](../../0501-1000/0823-split-array-with-same-average/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0872-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-the-array/)
