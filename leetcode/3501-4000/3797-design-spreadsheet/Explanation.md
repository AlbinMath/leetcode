# LeetCode 3484: Design Spreadsheet

**LeetCode Problem #3484 — Design Spreadsheet**
Solve LeetCode Design Spreadsheet using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Spreadsheet |
| LeetCode | #3484 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A spreadsheet is a grid with 26 columns (labeled from `'A'` to `'Z'`) and a given number of `rows`. Each cell in the spreadsheet can hold an integer value between 0 and 10^5.

Implement the `Spreadsheet` class:

`Spreadsheet(int rows)` Initializes a spreadsheet with 26 columns (labeled `'A'` to `'Z'`) and the specified number of rows. All cells are initially set to 0. 
 `void setCell(String cell, int value)` Sets the value of the specified `cell`. The cell reference is provided in the format `"AX"` (e.g., `"A1"`, `"B10"`), where the letter represents the column (from `'A'` to `'Z'`) and the number represents a **1-indexed** row. 
 `void resetCell(String cell)` Resets the specified cell to 0. 
 `int getValue(String formula)` Evaluates a formula of the form `"=X+Y"`, where `X` and `Y` are **either** cell references or non-negative integers, and returns the computed sum.

**Note:** If `getValue` references a cell that has not been explicitly set using `setCell`, its value is considered 0.

## Constraints
- `1 <= rows <= 10^3`
- `0 <= value <= 10^5`
- The formula is always in the format `"=X+Y"`, where `X` and `Y` are either valid cell references or **non-negative** integers with values less than or equal to `10^5`.
- Each cell reference consists of a capital letter from `'A'` to `'Z'` followed by a row number between `1` and `rows`.
- At most `10^4` calls will be made in **total** to `setCell`, `resetCell`, and `getValue`.

## Examples
### Example 1
- **Input:** `["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"] 
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]`
- **Output:** `[null, 12, null, 16, null, 25, null, 15]`
- **Explanation:** Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns 
spreadsheet.getValue("=5+7"); // returns 12 (5+7) 
spreadsheet.setCell("A1", 10); // sets A1 to 10 
spreadsheet.getValue("=A1+6"); // returns 16 (10+6) 
spreadsheet.setCell("B2", 15); // sets B2 to 15 
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15) 
spreadsheet.resetCell("A1"); // resets A1 to 0 
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Spreadsheet**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"] 
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 12, null, 16, null, 25, null, 15]`.
4. **Verification:** Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns 
spreadsheet.getValue("=5+7"); // returns 12 (5+7) 
spreadsheet.setCell("A1", 10); // sets A1 to 10 
spreadsheet.getValue("=A1+6"); // returns 16 (10+6) 
spreadsheet.setCell("B2", 15); // sets B2 to 15 
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15) 
spreadsheet.resetCell("A1"); // resets A1 to 0 
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var Spreadsheet = function(rows) {
    this.cells = new Map();
};
Spreadsheet.prototype.setCell = function(cell, value) {
    this.cells.set(cell, value);
};
Spreadsheet.prototype.resetCell = function(cell) {
    this.cells.delete(cell);
};
Spreadsheet.prototype.getValue = function(formula) {
    const [x, y] = formula.slice(1).split('+');
    
    const resolve = (token) => {
        const code = token.charCodeAt(0);
        if (code >= 65 && code <= 90) {
            return this.cells.get(token) || 0;
        }
        return Number(token);
    };
    
    return resolve(x) + resolve(y);
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0860-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-spreadsheet/)
