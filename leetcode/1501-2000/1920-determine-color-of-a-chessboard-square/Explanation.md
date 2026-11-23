# LeetCode 1812: Determine Color of a Chessboard Square

**LeetCode Problem #1812 — Determine Color of a Chessboard Square**
Solve LeetCode Determine Color of a Chessboard Square using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Determine Color of a Chessboard Square |
| LeetCode | #1812 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given `coordinates`, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return `true`* if the square is white, and *`false`* if the square is black*.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

## Constraints
- `coordinates.length == 2`
- `'a' <= coordinates[0] <= 'h'`
- `'1' <= coordinates[1] <= '8'`

## Examples
### Example 1
- **Input:** `coordinates = "a1"`
- **Output:** `false`
- **Explanation:** From the chessboard above, the square with coordinates "a1" is black, so return false.

### Example 2
- **Input:** `coordinates = "h3"`
- **Output:** `true`
- **Explanation:** From the chessboard above, the square with coordinates "h3" is white, so return true.

### Example 3
- **Input:** `coordinates = "c7"`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Determine Color of a Chessboard Square**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coordinates = "a1"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** From the chessboard above, the square with coordinates "a1" is black, so return false.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool squareIsWhite(string coordinates) {
        int column = coordinates[0] - 'a';
        int row = coordinates[1] - '1';

        return (row + column) % 2 == 1;
    }
};
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
- [3127. Make a Square with the Same Color](../../3001-3500/3398-make-a-square-with-the-same-color/)
- [221. Maximal Square](../../0001-0500/0221-maximal-square/)
- [367. Valid Perfect Square](../../0001-0500/0367-valid-perfect-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)
