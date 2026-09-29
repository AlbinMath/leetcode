# Largest Rectangle In Histogram

## Problem Explanation
Given an array of integers `heights` representing the histogram's bar heights (each bar has width 1), find the area of the largest rectangle that can be formed in the histogram.

For example, if `heights = [2,1,5,6,2,3]`:
- The largest rectangle has area `10` (formed by bars at indices 2 and 3 with heights 5 and 6, width = 2, height = 5).

## How the Code Works
The code uses a **Monotonic Stack** to efficiently compute the largest rectangle in $O(N)$ time.

1. **Stack of Indices:** The stack stores indices of bars in increasing order of their heights.
2. **Iteration:** It iterates from index `0` to `heights.length` (inclusive). At index `heights.length`, a virtual bar of height `0` is used to flush all remaining bars from the stack.
3. **Popping Taller Bars:** Whenever the current bar's height is less than the bar at the top of the stack, bars are popped. For each popped bar:
   - The `height` is the height of the popped bar.
   - The `width` extends from the current index `i` back to the bar just after the new top of the stack. If the stack is empty, the width is `i` (extends all the way to the left).
   - The area `height * width` is computed and `maxArea` is updated.
4. **Push Current Index:** The current index is pushed onto the stack.

The stack ensures each bar is pushed and popped at most once, giving $O(N)$ time complexity and $O(N)$ space complexity.
