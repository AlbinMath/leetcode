# LeetCode 118: Pascal's Triangle

**LeetCode Problem #118 — Pascal's Triangle**
Solve LeetCode Pascal's Triangle using JavaScript, PHP, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pascal's Triangle |
| LeetCode | #118 |
| Difficulty | Easy |
| Language | JavaScript, PHP, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `numRows`.

Return the first `numRows` of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it and the first and last number on each row must be equal to 1, as shown below:

## Constraints
- `1 <= numRows <= 30`

## Examples
### Example 1
- **Input:** `numRows = 5`
- **Output:** `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

### Example 2
- **Input:** `numRows = 1`
- **Output:** `[[1]]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pascal's Triangle**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numRows = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, PHP, Python

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### JavaScript
```javascript
var generate = function(numRows) {
    const triangle = [];

    for (let i = 0; i < numRows; i++) {
        const row = Array(i + 1).fill(1);

        for (let j = 1; j < i; j++) {
            row[j] = triangle[i - 1][j - 1]
                   + triangle[i - 1][j];
        }

        triangle.push(row);
    }

    return triangle;
};
```

### PHP
```php
class Solution {
    function generate($numRows) {
        $result = [];

        for ($i = 0; $i < $numRows; $i++) {
            $row = [];

            // First element
            $row[] = 1;

            // Middle elements
            for ($j = 1; $j < $i; $j++) {
                $row[] = $result[$i - 1][$j - 1]
                       + $result[$i - 1][$j];
            }

            // Last element
            if ($i > 0) {
                $row[] = 1;
            }

            $result[] = $row;
        }

        return $result;
    }
}
```

### Python
```python
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
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
- [119. Pascal's Triangle II](../../0001-0500/0119-pascals-triangle-ii/)
- [120. Triangle](../../0001-0500/0120-triangle/)
- [610. Triangle Judgement](../../0501-1000/0610-triangle-judgement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pascals-triangle/)
