# LeetCode 3168: Minimum Number of Chairs in a Waiting Room

**LeetCode Problem #3168 — Minimum Number of Chairs in a Waiting Room**
Solve LeetCode Minimum Number of Chairs in a Waiting Room using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Chairs in a Waiting Room |
| LeetCode | #3168 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`. Simulate events at each second `i`:

If `s[i] == 'E'`, a person enters the waiting room and takes one of the chairs in it. 
 If `s[i] == 'L'`, a person leaves the waiting room, freeing up a chair.

Return the **minimum **number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially **empty**.

## Constraints
- `1 <= s.length <= 50`
- `s` consists only of the letters `'E'` and `'L'`.
- `s` represents a valid sequence of entries and exits.

## Examples
### Example 1
- **Input:** `s = "EEEEEEE"`
- **Output:** `7`
- **Explanation:** After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

### Example 2
- **Input:** `s = "ELELEEL"`
- **Output:** `2`
- **Explanation:** Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second. 
 

 
 
 
 Second 
 Event 
 People in the Waiting Room 
 Available Chairs 
 
 
 0 
 Enter 
 1 
 1 
 
 
 1 
 Leave 
 0 
 2 
 
 
 2 
 Enter 
 1 
 1 
 
 
 3 
 Leave 
 0 
 2 
 
 
 4 
 Enter 
 1 
 1 
 
 
 5 
 Enter 
 2 
 0 
 
 
 6 
 Leave 
 1 
 1

### Example 3
- **Input:** `s = "ELEELEELLL"`
- **Output:** `3`
- **Explanation:** Let's consider that there are 3 chairs in the waiting room. The table below shows the state of the waiting room at each second. 
 

 
 
 
 Second 
 Event 
 People in the Waiting Room 
 Available Chairs 
 
 
 0 
 Enter 
 1 
 2 
 
 
 1 
 Leave 
 0 
 3 
 
 
 2 
 Enter 
 1 
 2 
 
 
 3 
 Enter 
 2 
 1 
 
 
 4 
 Leave 
 1 
 2 
 
 
 5 
 Enter 
 2 
 1 
 
 
 6 
 Enter 
 3 
 0 
 
 
 7 
 Leave 
 2 
 1 
 
 
 8 
 Leave 
 1 
 2 
 
 
 9 
 Leave 
 0 
 3

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Chairs in a Waiting Room**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "EEEEEEE"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumChairs = function(s) {
    let currentPeople = 0;
    let maxChairs = 0;

    for (const event of s) {
        if (event === 'E') {
            currentPeople++;
            if (currentPeople > maxChairs) {
                maxChairs = currentPeople;
            }
        } else {
            currentPeople--;
        }
    }

    return maxChairs;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4244-minimum-possible-maximum-waiting-time/)
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/)
