# Container With Most Water

## Problem Explanation
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

For example, if `height = [1,8,6,2,5,4,8,3,7]`:
- The maximum area is formed by the line at index 1 (`height = 8`) and the line at index 8 (`height = 7`).
- The width is `8 - 1 = 7`.
- The height is limited by the shorter line, which is `7`.
- The area is `7 * 7 = 49`.

## How the Code Works
This solution uses the **Two Pointers** approach to find the maximum area in $O(N)$ time.

1. **Initialization:** We start with two pointers, `left` at the beginning (`0`) and `right` at the end (`height.length - 1`) of the array. This gives us the maximum possible width.
2. **Calculating Area:** Inside a `while (left < right)` loop, we calculate the width as `right - left`. The height of the water is determined by the shorter of the two lines: `Math.min(height[left], height[right])`.
3. **Updating Max:** We calculate the area (`width * h`) and update `maxWater` if this area is larger than the previous maximum.
4. **Moving the Pointers:** The key logic is deciding which pointer to move. Since the width is always decreasing as we move the pointers inward, the only way to potentially find a *larger* area is to find a *taller* line. Therefore, we always move the pointer that points to the shorter line.
   - If `height[left] < height[right]`, we increment `left`.
   - Otherwise, we decrement `right`.
5. **Termination:** The loop continues until the two pointers meet, at which point all possible maximum combinations have been considered, and we return `maxWater`.

This approach evaluates the array in a single pass, resulting in an $O(N)$ time complexity and $O(1)$ space complexity.
