# LeetCode 168: Excel Sheet Column Title

**LeetCode Problem #168 — Excel Sheet Column Title**
Solve LeetCode Excel Sheet Column Title using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Excel Sheet Column Title |
| LeetCode | #168 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.

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
- `1 <= columnNumber <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `columnNumber = 1`
- **Output:** `"A"`

### Example 2
- **Input:** `columnNumber = 28`
- **Output:** `"AB"`

### Example 3
- **Input:** `columnNumber = 701`
- **Output:** `"ZY"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Excel Sheet Column Title**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `columnNumber = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"A"`.

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
    function convertToTitle($columnNumber) {
        $result = "";

        while ($columnNumber > 0) {
            // Convert 1-26 into 0-25
            $columnNumber--;

            // Get character A-Z
            $remainder = $columnNumber % 26;
            $result = chr(ord('A') + $remainder) . $result;

            // Move to the next position
            $columnNumber = intdiv($columnNumber, 26);
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
- [171. Excel Sheet Column Number](../../0001-0500/0171-excel-sheet-column-number/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0947-most-stones-removed-with-same-row-or-column/)
- [2352. Equal Row and Column Pairs](../../2001-2500/2352-equal-row-and-column-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/)
