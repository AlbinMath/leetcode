# LeetCode 2248: Intersection of Multiple Arrays

**LeetCode Problem #2248 — Intersection of Multiple Arrays**
Solve LeetCode Intersection of Multiple Arrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Intersection of Multiple Arrays |
| LeetCode | #2248 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D integer array `nums` where `nums[i]` is a non-empty array of **distinct** positive integers, return *the list of integers that are present in **each array** of* `nums`* sorted in **ascending order***.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= sum(nums[i].length) <= 1000`
- `1 <= nums[i][j] <= 1000`
- All the values of `nums[i]` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [[`
- **Output:** `[3,4]`
- **Explanation:** The only integers present in each of nums[0] = [

### Example 2
- **Input:** `nums = [[1,2,3],[4,5,6]]`
- **Output:** `[]`
- **Explanation:** There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Intersection of Multiple Arrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4]`.
4. **Verification:** The only integers present in each of nums[0] = [

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        n = len(nums)
        freq = [0] * 1001
        
        for arr in nums:
            for num in arr:
                freq[num] += 1
                
        return [num for num in range(1, 1001) if freq[num] == n]
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [349. Intersection of Two Arrays](../../0001-0500/0349-intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](../../0001-0500/0350-intersection-of-two-arrays-ii/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/intersection-of-multiple-arrays/)
