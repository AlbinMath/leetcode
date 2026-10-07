# LeetCode 11: Container With Most Water

**LeetCode Problem #11 — Container With Most Water**
Solve LeetCode Container With Most Water using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Container With Most Water |
| LeetCode | #11 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  height  of length  n . There are  n  vertical lines drawn such that the two endpoints of the  i th   line are  (i, 0)  and  (i, height[i]) .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
This solution uses the **Two Pointers** approach to find the maximum area in $O(N)$ time.

1. **Initialization:** We start with two pointers, `left` at the beginning (`0`) and `right` at the end (`height.length - 1`) of the array. This gives us the maximum possible width.
2. **Calculating Area:** Inside a `while (left < right)` loop, we calculate the width as `right - left`. The height of the water is determined by the shorter of the two lines: `Math.min(height[left], height[right])`.
3. **Updating Max:** We calculate the area (`width * h`) and update `maxWater` if this area is larger than the previous maximum.
4. **Moving the Pointers:** The key logic is deciding which pointer to move. Since the width is always decreasing as we move the pointers inward, the only way to potentially find a *larger* area is to find a *taller* line. Therefore, we always move the pointer that points to the shorter line.
   - If `height[left] < height[right]`, we increment `left`.
   - Otherwise, we decrement `right`.
5. **Termination:** The loop continues until the two pointers meet, at which point all possible maximum combinations have been considered, and we return `maxWater`.

This approach evaluates the array in a single pass, resulting in an $O(N)$ time complexity and $O(1)$ space complexity.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Container With Most Water**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

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
- [42. Trapping Rain Water](../0042-trapping-rain-water/)
- [602. Friend Requests II: Who Has the Most Friends](../0602-friend-requests-ii-who-has-the-most-friends/)
- [2958. Length of Longest Subarray With at Most K Frequency](../3225-length-of-longest-subarray-with-at-most-k-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/container-with-most-water/)
