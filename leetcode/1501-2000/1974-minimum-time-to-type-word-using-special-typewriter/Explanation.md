# LeetCode 1974: Minimum Time to Type Word Using Special Typewriter

**LeetCode Problem #1974 — Minimum Time to Type Word Using Special Typewriter**
Solve LeetCode Minimum Time to Type Word Using Special Typewriter using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Type Word Using Special Typewriter |
| LeetCode | #1974 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a special typewriter with lowercase English letters `'a'` to `'z'` arranged in a **circle** with a **pointer**. A character can **only** be typed if the pointer is pointing to that character. The pointer is **initially** pointing to the character `'a'`.

Each second, you may perform one of the following operations:

Move the pointer one character **counterclockwise** or **clockwise**. 
 Type the character the pointer is **currently** on.

Given a string `word`, return the** minimum** number of seconds to type out the characters in `word`.

## Constraints
- `1 <= word.length <= 100`
- `word` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "abc"`
- **Output:** `5`
- **Explanation:** The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.

### Example 2
- **Input:** `word = "bza"`
- **Output:** `7`
- **Explanation:** The characters are printed as follows:
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer counterclockwise to 'z' in 2 seconds.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'a' in 1 second.
- Type the character 'a' in 1 second.

### Example 3
- **Input:** `word = "zjpc"`
- **Output:** `34`
- **Explanation:** The characters are printed as follows:
- Move the pointer counterclockwise to 'z' in 1 second.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'j' in 10 seconds.
- Type the character 'j' in 1 second.
- Move the pointer clockwise to 'p' in 6 seconds.
- Type the character 'p' in 1 second.
- Move the pointer counterclockwise to 'c' in 13 seconds.
- Type the character 'c' in 1 second.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Type Word Using Special Typewriter**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "abc"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minTimeToType = function(word) {
    let time = 0;
    let current = 0; // 'a' = 0

    for (const char of word) {
        let target = char.charCodeAt(0) - 'a'.charCodeAt(0);

        let distance = Math.abs(target - current);

        time += Math.min(distance, 26 - distance) + 1;

        current = target;
    }

    return time;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1320-minimum-distance-to-type-a-word-using-two-fingers/)
- [3014. Minimum Number of Pushes to Type Word I](../../3001-3500/3014-minimum-number-of-pushes-to-type-word-i/)
- [3016. Minimum Number of Pushes to Type Word II](../../3001-3500/3016-minimum-number-of-pushes-to-type-word-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/)
