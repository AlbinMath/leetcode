# LeetCode 17: Letter Combinations of a Phone Number

**LeetCode Problem #17 — Letter Combinations of a Phone Number**
Solve LeetCode Letter Combinations of a Phone Number using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Letter Combinations of a Phone Number |
| LeetCode | #17 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Constraints
- `1 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Examples
### Example 1
- **Input:** `digits = "23"`
- **Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

### Example 2
- **Input:** `digits = "2"`
- **Output:** `["a","b","c"]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Backtracking** to explore all possible letter combinations.

1. **Base Case:** If the input string is empty, it returns an empty array immediately.
2. **Digit-to-Letter Map:** A `map` object stores the mapping from each digit (`'2'` through `'9'`) to its corresponding letters.
3. **Backtracking Function:** The recursive function `backtrack(index, current)` builds one combination at a time:
   - **Termination:** When `index` equals the length of `digits`, the current combination `current` is complete and is pushed to the `result` array.
   - **Branching:** Otherwise, it looks up the letters for `digits[index]` and iterates over each letter. For each letter, it recurses with `index + 1` and `current + letter`, which extends the current combination by one character.
4. The function is initially called with `backtrack(0, "")`, starting from the first digit with an empty string.

Since each digit maps to at most 4 letters, the time complexity is $O(4^N)$ where $N$ is the number of digits, and space complexity is $O(N)$ for the recursion stack.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `digits = "23"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var letterCombinations = function(digits) {
    if (digits.length === 0) return [];

    const phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };

    let result = [''];

    for (const digit of digits) {
        const letters = phone[digit];
        const combinations = [];

        for (const combination of result) {
            for (const letter of letters) {
                combinations.push(combination + letter);
            }
        }

        result = combinations;
    }

    return result;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2056. Number of Valid Move Combinations On Chessboard](../../2001-2500/2056-number-of-valid-move-combinations-on-chessboard/)
- [1694. Reformat Phone Number](../../1501-2000/1694-reformat-phone-number/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0744-find-smallest-letter-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
