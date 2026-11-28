# LeetCode 2164: Sort Even and Odd Indices Independently

**LeetCode Problem #2164 — Sort Even and Odd Indices Independently**
Solve LeetCode Sort Even and Odd Indices Independently using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Even and Odd Indices Independently |
| LeetCode | #2164 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. Rearrange the values of `nums` according to the following rules:

Sort the values at **odd indices** of `nums` in **non-increasing** order.

For example, if `nums = [4,** 1 **,2, **3** ]` before this step, it becomes `[4, **3** ,2,** 1 **]` after. The values at odd indices `1` and `3` are sorted in non-increasing order. 
 
 
 Sort the values at **even indices** of `nums` in **non-decreasing** order.
 
 For example, if `nums = [ **4** ,1, **2** ,3]` before this step, it becomes `[ **2** ,1, **4** ,3]` after. The values at even indices `0` and `2` are sorted in non-decreasing order.

Return *the array formed after rearranging the values of* `nums`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [4,1,2,3]`
- **Output:** `[2,3,4,1]`
- **Explanation:** First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,

### Example 2
- **Input:** `nums = [2,1]`
- **Output:** `[2,1]`
- **Explanation:** Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sort Even and Odd Indices Independently**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,1,2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,4,1]`.
4. **Verification:** First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sortEvenOdd = function(nums) {
    const even = [];
    const odd = [];
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) {
            even.push(nums[i]);
        } else {
            odd.push(nums[i]);
        }
    }
    even.sort((a, b) => a - b);
    odd.sort((a, b) => b - a);
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) {
            nums[i] = even.shift();
        } else {
            nums[i] = odd.shift();
        }
    }

    return nums;
};
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
- [4099. Minimum Operations to Sort With Locked Indices](../../4001-4500/4099-minimum-operations-to-sort-with-locked-indices/)
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../0501-1000/0975-odd-even-jump/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-even-and-odd-indices-independently/)
