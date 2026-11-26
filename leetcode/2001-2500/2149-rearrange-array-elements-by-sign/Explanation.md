# LeetCode 2149: Rearrange Array Elements by Sign

**LeetCode Problem #2149 — Rearrange Array Elements by Sign**
Solve LeetCode Rearrange Array Elements by Sign using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Array Elements by Sign |
| LeetCode | #2149 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of **even** length consisting of an **equal** number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every **consecutive pair** of integers have **opposite signs**. 
 For all integers with the same sign, the **order** in which they were present in `nums` is **preserved**. 
 The rearranged array begins with a positive integer.

Return *the modified array after rearranging the elements to satisfy the aforementioned conditions*.

## Constraints
- `2 <= nums.length <= 2 * 10^5`
- `nums.length` is **even**
- `1 <= |nums[i]| <= 10^5`
- `nums` consists of **equal** number of positive and negative integers.

## Examples
### Example 1
- **Input:** `nums = [3,1,-2,-5,2,-4]`
- **Output:** `[3,-2,1,-5,2,-4]`
- **Explanation:** The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.

### Example 2
- **Input:** `nums = [-1,1]`
- **Output:** `[1,-1]`
- **Explanation:** 1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Array Elements by Sign**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,-2,-5,2,-4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,-2,1,-5,2,-4]`.
4. **Verification:** The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.

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
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos, neg = 0, 1
        for x in nums:
            if x > 0:
                res[pos] = x
                pos += 2
            else:
                res[neg] = x
                neg += 2
        return res
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
- [1822. Sign of the Product of an Array](../../1501-2000/1822-sign-of-the-product-of-an-array/)
- [2587. Rearrange Array to Maximize Prefix Score](../../2501-3000/2587-rearrange-array-to-maximize-prefix-score/)
- [4065. Rearrange Array by Removing Distinct Values](../../4001-4500/4065-rearrange-array-by-removing-distinct-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-array-elements-by-sign/)
