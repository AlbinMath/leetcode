# Integer To Roman

## Problem Explanation
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`. 
You are given an integer, and you need to convert it to a Roman numeral.

For example:
- `3` is written as `III` in Roman numeral, just three ones added together.
- `4` is written as `IV`. `58` is written as `LVIII`, which is `L = 50, V = 5, III = 3`.
- `1994` is written as `MCMXCIV`, which is `M = 1000, CM = 900, XC = 90, IV = 4`.

## How the Code Works
The code uses a greedy approach to convert the integer by repeatedly subtracting the largest possible Roman numeral values.

1. **Mapping Values and Symbols:** It defines two parallel arrays: `values` and `symbols`. These arrays map the numerical values to their corresponding Roman numeral strings. Crucially, this list includes the special subtraction cases (like `900 -> CM`, `400 -> CD`, `90 -> XC`, `40 -> XL`, `9 -> IX`, and `4 -> IV`) so they can be treated just like normal numerals. They are arranged in descending order from largest (`1000`) to smallest (`1`).
2. **Greedy Subtraction:** It initializes an empty `result` string. Then, it loops through the `values` array.
3. For each value, it uses a `while (num >= values[i])` loop. As long as the remaining `num` is greater than or equal to the current Roman value, it:
   - Appends the corresponding Roman `symbol` to the `result` string.
   - Subtracts the `value` from `num`.
4. Because the values are checked from largest to smallest, the algorithm guarantees the correct Roman numeral format (e.g., it will always use `M` before it attempts to use `CM` or `D`).
5. **Completion:** The loop continues until `num` is reduced to 0, at which point the complete Roman numeral string is returned.

The time complexity is $O(1)$ because the number of values is fixed (13 symbols) and the `while` loop will run at most a constant number of times (since the maximum input is 3999). The space complexity is also $O(1)$ since the arrays are of fixed size.
