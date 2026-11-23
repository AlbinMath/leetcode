# LeetCode 12: Integer to Roman

**LeetCode Problem #12 — Integer to Roman**
Solve LeetCode Integer to Roman using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Integer to Roman |
| LeetCode | #12 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Seven different symbols represent Roman numerals with the following values:

Symbol 
 Value 
 
 
 
 
 I 
 1 
 
 
 V 
 5 
 
 
 X 
 10 
 
 
 L 
 50 
 
 
 C 
 100 
 
 
 D 
 500 
 
 
 M 
 1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral. 
 If the value starts with 4 or 9 use the **subtractive form** representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`). 
 Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the **subtractive form**.

Given an integer, convert it to a Roman numeral.

## Constraints
- `1 <= num <= 3999`

## Examples
### Example 1
- **Input:** `num = 3749`
- **Output:** `"MMMDCCXLIX"`
- **Explanation:** 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
 40 = XL as 10 (X) less of 50 (L)
 9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

### Example 2
- **Input:** `num = 58`
- **Output:** `"LVIII"`
- **Explanation:** 50 = L
 8 = VIII

### Example 3
- **Input:** `num = 1994`
- **Output:** `"MCMXCIV"`
- **Explanation:** 1000 = M
 900 = CM
 90 = XC
 4 = IV

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a greedy approach to convert the integer by repeatedly subtracting the largest possible Roman numeral values.

1. **Mapping Values and Symbols:** It defines two parallel arrays: `values` and `symbols`. These arrays map the numerical values to their corresponding Roman numeral strings. Crucially, this list includes the special subtraction cases (like `900 -> CM`, `400 -> CD`, `90 -> XC`, `40 -> XL`, `9 -> IX`, and `4 -> IV`) so they can be treated just like normal numerals. They are arranged in descending order from largest (`1000`) to smallest (`1`).
2. **Greedy Subtraction:** It initializes an empty `result` string. Then, it loops through the `values` array.
3. For each value, it uses a `while (num >= values[i])` loop. As long as the remaining `num` is greater than or equal to the current Roman value, it:
   - Appends the corresponding Roman `symbol` to the `result` string.
   - Subtracts the `value` from `num`.
4. Because the values are checked from largest to smallest, the algorithm guarantees the correct Roman numeral format (e.g., it will always use `M` before it attempts to use `CM` or `D`).
5. **Completion:** The loop continues until `num` is reduced to 0, at which point the complete Roman numeral string is returned.

The time complexity is $O(1)$ because the number of values is fixed (13 symbols) and the `while` loop will run at most a constant number of times (since the maximum input is 3999). The space complexity is also $O(1)$ since the arrays are of fixed size.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `num = 3749`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"MMMDCCXLIX"`.
4. **Verification:** 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
 40 = XL as 10 (X) less of 50 (L)
 9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ];
    const symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ];
    let result = "";
    for (let i = 0; i < values.length; i++) {
        while (num >= values[i]) {
            result += symbols[i];
            num -= values[i];
        }
    }
    return result;
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [13. Roman to Integer](../../0001-0500/0013-roman-to-integer/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/integer-to-roman/)
