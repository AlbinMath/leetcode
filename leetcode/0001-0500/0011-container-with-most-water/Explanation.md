# LeetCode 11: Container With Most Water

**LeetCode Problem #11 — Container With Most Water**
Solve LeetCode Container With Most Water using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Container With Most Water |
| LeetCode | #11 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i^th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Examples
### Example 1
- **Input:** `height = [1,8,6,2,5,4,8,3,7]`
- **Output:** `49`
- **Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2
- **Input:** `height = [1,1]`
- **Output:** `1`

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

## Example Walkthrough
1. **Input State:** We begin with `height = [1,8,6,2,5,4,8,3,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `49`.
4. **Verification:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let maxWater = 0;

    while (left < right) {
        const width = right - left;
        const minHeight = Math.min(height[left], height[right]);
        const area = width * minHeight;

        maxWater = Math.max(maxWater, area);

        // Move the pointer at the shorter line
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxWater;
};
```

### Python
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
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
- [42. Trapping Rain Water](../../0001-0500/0042-trapping-rain-water/)
- [365. Water and Jug Problem](../../0001-0500/0365-water-and-jug-problem/)
- [407. Trapping Rain Water II](../../0001-0500/0407-trapping-rain-water-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/container-with-most-water/)
