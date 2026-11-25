# LeetCode 1796: Second Largest Digit in a String

**LeetCode Problem #1796 — Second Largest Digit in a String**
Solve LeetCode Second Largest Digit in a String using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Largest Digit in a String |
| LeetCode | #1796 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an alphanumeric string `s`, return *the **second largest** numerical digit that appears in *`s`*, or *`-1`* if it does not exist*.

An **alphanumeric**** **string is a string consisting of lowercase English letters and digits.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of only lowercase English letters and digits.

## Examples
### Example 1
- **Input:** `s = "dfa12321afd"`
- **Output:** `2`
- **Explanation:** The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

### Example 2
- **Input:** `s = "abc1111"`
- **Output:** `-1`
- **Explanation:** The digits that appear in s are [1]. There is no second largest digit.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Second Largest Digit in a String**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "dfa12321afd"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

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
    int secondHighest(string s) {
        bool seen[10] = {false};

        for (char c : s) {
            if (isdigit(c)) {
                seen[c - '0'] = true;
            }
        }

        int count = 0;

        for (int i = 9; i >= 0; i--) {
            if (seen[i]) {
                count++;

                if (count == 2) {
                    return i;
                }
            }
        }

        return -1;
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
- [2243. Calculate Digit Sum of a String](../../2001-2500/2243-calculate-digit-sum-of-a-string/)
- [4022. K-th Digit in Infinite String](../../4001-4500/4022-k-th-digit-in-infinite-string/)
- [1903. Largest Odd Number in String](../../1501-2000/1903-largest-odd-number-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-largest-digit-in-a-string/)
