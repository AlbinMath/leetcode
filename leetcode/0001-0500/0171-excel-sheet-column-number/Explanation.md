# LeetCode 171: Excel Sheet Column Number

**LeetCode Problem #171 — Excel Sheet Column Number**
Solve LeetCode Excel Sheet Column Number using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Excel Sheet Column Number |
| LeetCode | #171 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return *its corresponding column number*.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

## Constraints
- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

## Examples
### Example 1
- **Input:** `columnTitle = "A"`
- **Output:** `1`

### Example 2
- **Input:** `columnTitle = "AB"`
- **Output:** `28`

### Example 3
- **Input:** `columnTitle = "ZY"`
- **Output:** `701`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Excel Sheet Column Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `columnTitle = "A"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function titleToNumber($columnTitle) {
        $result = 0;

        for ($i = 0; $i < strlen($columnTitle); $i++) {
            $value = ord($columnTitle[$i]) - ord('A') + 1;

            $result = $result * 26 + $value;
        }

        return $result;
    }
}
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [168. Excel Sheet Column Title](../../0001-0500/0168-excel-sheet-column-title/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0947-most-stones-removed-with-same-row-or-column/)
- [1605. Find Valid Matrix Given Row and Column Sums](../../1501-2000/1605-find-valid-matrix-given-row-and-column-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)
