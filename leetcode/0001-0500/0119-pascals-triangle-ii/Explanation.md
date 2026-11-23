# LeetCode 119: Pascal's Triangle II

**LeetCode Problem #119 — Pascal's Triangle II**
Solve LeetCode Pascal's Triangle II using PHP and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pascal's Triangle II |
| LeetCode | #119 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `rowIndex`, return the `rowIndex^th` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

## Constraints
- `0 <= rowIndex <= 33`

## Examples
### Example 1
- **Input:** `rowIndex = 3`
- **Output:** `[1,3,3,1]`

### Example 2
- **Input:** `rowIndex = 0`
- **Output:** `[1]`

### Example 3
- **Input:** `rowIndex = 1`
- **Output:** `[1,1]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pascal's Triangle II**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rowIndex = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,3,1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function getRow($rowIndex) {
        $row = array_fill(0, $rowIndex + 1, 0);
        $row[0] = 1;

        for ($i = 1; $i <= $rowIndex; $i++) {
            // Traverse backwards so previous values
            // are not overwritten before they are used.
            for ($j = $i; $j >= 1; $j--) {
                $row[$j] = $row[$j] + $row[$j - 1];
            }
        }

        return $row;
    }
}
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
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)
- [120. Triangle](../../0001-0500/0120-triangle/)
- [610. Triangle Judgement](../../0501-1000/0610-triangle-judgement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)
