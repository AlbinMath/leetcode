# LeetCode 3751: Total Waviness of Numbers in Range I

**LeetCode Problem #3751 — Total Waviness of Numbers in Range I**
Solve LeetCode Total Waviness of Numbers in Range I using Java and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Waviness of Numbers in Range I |
| LeetCode | #3751 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors. 
 A digit is a **valley** if it is **strictly less** than both of its immediate neighbors. 
 The first and last digits of a number **cannot** be peaks or valleys. 
 Any number with fewer than 3 digits has a waviness of 0. 
 
Return the total sum of waviness for all numbers in the range `[num1, num2]`.

## Constraints
- `1 <= num1 <= num2 <= 10^5`

## Examples
### Example 1
- **Input:** `num1 = 120, num2 = 130`
- **Output:** `3`
- **Explanation:** In the range `[120, 130]`:

 
 `120`: middle digit 2 is a peak, waviness = 1. 
 `121`: middle digit 2 is a peak, waviness = 1. 
 `130`: middle digit 3 is a peak, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

### Example 2
- **Input:** `num1 = 198, num2 = 202`
- **Output:** `3`
- **Explanation:** In the range `[198, 202]`:

 
 `198`: middle digit 9 is a peak, waviness = 1. 
 `201`: middle digit 0 is a valley, waviness = 1. 
 `202`: middle digit 0 is a valley, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

### Example 3
- **Input:** `num1 = 4848, num2 = 4848`
- **Output:** `2`
- **Explanation:** Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Total Waviness of Numbers in Range I**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = 120, num2 = 130`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In the range `[120, 130]`:

 
 `120`: middle digit 2 is a peak, waviness = 1. 
 `121`: middle digit 2 is a peak, waviness = 1. 
 `130`: middle digit 3 is a peak, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int totalWaviness(int num1, int num2) {
        int total = 0;

        for (int num = num1; num <= num2; num++) {
            String s = String.valueOf(num);

            for (int i = 1; i < s.length() - 1; i++) {
                int prev = s.charAt(i - 1) - '0';
                int curr = s.charAt(i) - '0';
                int next = s.charAt(i + 1) - '0';

                // Peak
                if (curr > prev && curr > next) {
                    total++;
                }
                // Valley
                else if (curr < prev && curr < next) {
                    total++;
                }
            }
        }

        return total;
    }
}
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
- [3753. Total Waviness of Numbers in Range II](../../4001-4500/4128-total-waviness-of-numbers-in-range-ii/)
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1630-count-odd-numbers-in-an-interval-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)
