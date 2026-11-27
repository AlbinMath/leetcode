# LeetCode 1945: Sum of Digits of String After Convert

**LeetCode Problem #1945 — Sum of Digits of String After Convert**
Solve LeetCode Sum of Digits of String After Convert using C++ and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Digits of String After Convert |
| LeetCode | #1945 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters, and an integer `k`. Your task is to *convert* the string into an integer by a special process, and then *transform* it by summing its digits repeatedly `k` times. More specifically, perform the following steps:

**Convert** `s` into an integer by replacing each letter with its position in the alphabet (i.e. replace `'a'` with `1`, `'b'` with `2`, ..., `'z'` with `26`). 
 **T****ransform** the integer by replacing it with the **sum of its digits**. 
 Repeat the **transform** operation (step 2) `k`** times** in total.

For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be `8` by the following operations:

**Convert**: `"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124` 
 **Transform #1**: `262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17` 
 **Transform #2**: `17 ➝ 1 + 7 ➝ 8`

Return the **resulting** **integer** after performing the **operations** described above.

## Constraints
- `1 <= s.length <= 100`
- `1 <= k <= 10`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "iiii", k = 1`
- **Output:** `36`
- **Explanation:** The operations are as follows: 
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999 
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36 
Thus the resulting integer is 36.

### Example 2
- **Input:** `s = "leetcode", k = 2`
- **Output:** `6`
- **Explanation:** The operations are as follows: 
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545 
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33 
- Transform #2: 33 ➝ 3 + 3 ➝ 6 
Thus the resulting integer is 6.

### Example 3
- **Input:** `s = "zbax", k = 2`
- **Output:** `8`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Digits of String After Convert**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "iiii", k = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `36`.
4. **Verification:** The operations are as follows: 
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999 
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36 
Thus the resulting integer is 36.

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
    int getLucky(string s, int k) {
        int sum = 0;

        // Convert each character to its alphabet position
        for (char c : s) {
            int value = c - 'a' + 1;

            // Add the digits of the position
            sum += value / 10;
            sum += value % 10;
        }

        // Perform the remaining digit-sum transformations
        for (int i = 1; i < k; i++) {
            int digitSum = 0;

            while (sum > 0) {
                digitSum += sum % 10;
                sum /= 10;
            }

            sum = digitSum;
        }

        return sum;
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
- [2160. Minimum Sum of Four Digit Number After Splitting Digits](../../2001-2500/2160-minimum-sum-of-four-digit-number-after-splitting-digits/)
- [3461. Check If Digits Are Equal in String After Operations I](../../3001-3500/3461-check-if-digits-are-equal-in-string-after-operations-i/)
- [3463. Check If Digits Are Equal in String After Operations II](../../3001-3500/3463-check-if-digits-are-equal-in-string-after-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/)
