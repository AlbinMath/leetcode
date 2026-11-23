# LeetCode 735: Asteroid Collision

**LeetCode Problem #735 — Asteroid Collision**
Solve LeetCode Asteroid Collision using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Asteroid Collision |
| LeetCode | #735 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Constraints
- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

## Examples
### Example 1
- **Input:** `asteroids = [5,10,-5]`
- **Output:** `[5,10]`
- **Explanation:** The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

### Example 2
- **Input:** `asteroids = [8,-8]`
- **Output:** `[]`
- **Explanation:** The 8 and -8 collide exploding each other.

### Example 3
- **Input:** `asteroids = [10,2,-5]`
- **Output:** `[10]`
- **Explanation:** The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

### Example 4
- **Input:** `asteroids = [3,5,-6,2,-1,4]​​​​​​​`
- **Output:** `[-6,2,4]`
- **Explanation:** The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Asteroid Collision**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `asteroids = [5,10,-5]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,10]`.
4. **Verification:** The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var asteroidCollision = function(asteroids) {
    const stack = [];

    for (const asteroid of asteroids) {
        let alive = true;

        while (
            alive &&
            asteroid < 0 &&
            stack.length > 0 &&
            stack[stack.length - 1] > 0
        ) {
            const top = stack[stack.length - 1];

            if (top < -asteroid) {
                stack.pop();
            } else if (top === -asteroid) {
                stack.pop();
                alive = false;
            } else {
                alive = false;
            }
        }

        if (alive) {
            stack.push(asteroid);
        }
    }

    return stack;
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
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)
- [32. Longest Valid Parentheses](../../0001-0500/0032-longest-valid-parentheses/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/asteroid-collision/)
