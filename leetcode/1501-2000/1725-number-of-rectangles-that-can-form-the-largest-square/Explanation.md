# LeetCode 1725: Number Of Rectangles That Can Form The Largest Square

**LeetCode Problem #1725 — Number Of Rectangles That Can Form The Largest Square**
Solve LeetCode Number Of Rectangles That Can Form The Largest Square using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number Of Rectangles That Can Form The Largest Square |
| LeetCode | #1725 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `rectangles` where `rectangles[i] = [l_i, w_i]` represents the `i^th` rectangle of length `l_i` and width `w_i`.

You can cut the `i^th` rectangle to form a square with a side length of `k` if both `k <= l_i` and `k <= w_i`. For example, if you have a rectangle `[4,6]`, you can cut it to get a square with a side length of at most `4`.

Let `maxLen` be the side length of the **largest** square you can obtain from any of the given rectangles.

Return *the **number** of rectangles that can make a square with a side length of *`maxLen`.

## Constraints
- `1 <= rectangles.length <= 1000`
- `rectangles[i].length == 2`
- `1 <= l_i, w_i <= 10^9`
- `l_i != w_i`

## Examples
### Example 1
- **Input:** `rectangles = [[5,8],[3,9],[5,12],[16,5]]`
- **Output:** `3`
- **Explanation:** The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.

### Example 2
- **Input:** `rectangles = [[2,3],[3,7],[4,3],[3,7]]`
- **Output:** `3`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number Of Rectangles That Can Form The Largest Square**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rectangles = [[5,8],[3,9],[5,12],[16,5]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int maxLen = 0;
        int count = 0;

        for (auto& rectangle : rectangles) {
            int side = min(rectangle[0], rectangle[1]);

            if (side > maxLen) {
                maxLen = side;
                count = 1;
            }
            else if (side == maxLen) {
                count++;
            }
        }

        return count;
    }
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3047-find-the-largest-area-of-square-inside-two-rectangles/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2791-count-paths-that-can-form-a-palindrome-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/)
