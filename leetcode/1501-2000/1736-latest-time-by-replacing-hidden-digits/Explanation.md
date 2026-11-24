# LeetCode 1736: Latest Time by Replacing Hidden Digits

**LeetCode Problem #1736 — Latest Time by Replacing Hidden Digits**
Solve LeetCode Latest Time by Replacing Hidden Digits using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Latest Time by Replacing Hidden Digits |
| LeetCode | #1736 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `time` in the form of ` hh:mm`, where some of the digits in the string are hidden (represented by `?`).

The valid times are those inclusively between `00:00` and `23:59`.

Return *the latest valid time you can get from* `time`* by replacing the hidden* *digits*.

## Constraints
- `time` is in the format `hh:mm`.
- It is guaranteed that you can produce a valid time from the given string.

## Examples
### Example 1
- **Input:** `time = "2?:?0"`
- **Output:** `"23:50"`
- **Explanation:** The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

### Example 2
- **Input:** `time = "0?:3?"`
- **Output:** `"09:39"`

### Example 3
- **Input:** `time = "1?:22"`
- **Output:** `"19:22"`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Latest Time by Replacing Hidden Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `time = "2?:?0"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"23:50"`.
4. **Verification:** The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string maximumTime(string time) {
        if (time[0] == '?') {
            time[0] = (time[1] == '?' || time[1] <= '3') ? '2' : '1';
        }

        if (time[1] == '?') {
            time[1] = (time[0] == '2') ? '3' : '9';
        }

        if (time[3] == '?') {
            time[3] = '5';
        }

        if (time[4] == '?') {
            time[4] = '9';
        }

        return time;
    }
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
- [3114. Latest Time You Can Obtain After Replacing Characters](../../3001-3500/3114-latest-time-you-can-obtain-after-replacing-characters/)
- [949. Largest Time for Given Digits](../../0501-1000/0949-largest-time-for-given-digits/)
- [2332. The Latest Time to Catch a Bus](../../2001-2500/2332-the-latest-time-to-catch-a-bus/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/)
