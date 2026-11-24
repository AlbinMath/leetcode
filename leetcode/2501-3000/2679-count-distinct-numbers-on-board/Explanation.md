# LeetCode 2549: Count Distinct Numbers on Board

**LeetCode Problem #2549 — Count Distinct Numbers on Board**
Solve LeetCode Count Distinct Numbers on Board using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Distinct Numbers on Board |
| LeetCode | #2549 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`, that is initially placed on a board. Every day, for `10^9` days, you perform the following procedure:

For each number `x` present on the board, find all numbers `1 <= i <= n` such that `x % i == 1`. 
 Then, place those numbers on the board.

Return* the number of **distinct** integers present on the board after* `10^9` *days have elapsed*.

**Note:**

Once a number is placed on the board, it will remain on it until the end. 
 `%` stands for the modulo operation. For example, `14 % 3` is `2`.

## Constraints
- `1 <= n <= 100`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `4`
- **Explanation:** Initially, 5 is present on the board. 
The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. 
After that day, 3 will be added to the board because 4 % 3 == 1. 
At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.

### Example 2
- **Input:** `n = 3`
- **Output:** `2`
- **Explanation:** Since 3 % 2 == 1, 2 will be added to the board. 
After a billion days, the only two distinct numbers on the board are 2 and 3.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Distinct Numbers on Board**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Initially, 5 is present on the board. 
The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. 
After that day, 3 will be added to the board because 4 % 3 == 1. 
At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.

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
var distinctIntegers = function(n) {
    return Math.max(n - 1, 1);
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
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2501-3000/2525-count-number-of-distinct-integers-after-reverse-operations/)
- [3569. Maximize Count of Distinct Primes After Split](../../3501-4000/3878-maximize-count-of-distinct-primes-after-split/)
- [3859. Count Subarrays With K Distinct Integers](../../4001-4500/4002-count-subarrays-with-k-distinct-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-distinct-numbers-on-board/)
