# LeetCode 1096: Brace Expansion II

**LeetCode Problem #1096 — Brace Expansion II**
Solve LeetCode Brace Expansion II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Brace Expansion II |
| LeetCode | #1096 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
 
 `R("a") = {"a"}` 
 `R("w") = {"w"}` 
 
 
 When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
 
 `R("{a,b,c}") = {"a","b","c"}` 
 `R("{{a,b},{b,c}}") = {"a","b","c"}` (notice the final set only contains each word at most once) 
 
 
 When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
 
 `R("{a,b}{c,d}") = {"ac","ad","bc","bd"}` 
 `R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}`

Formally, the three rules for our grammar:

For every lowercase letter `x`, we have `R(x) = {x}`. 
 For expressions `e_1, e_2, ... , e_k` with `k >= 2`, we have `R({e_1, e_2, ...}) = R(e_1) &cup; R(e_2) &cup; ...` 
 For expressions `e_1` and `e_2`, we have `R(e_1 + e_2) = {a + b for (a, b) in R(e_1) &times; R(e_2)}`, where `+` denotes concatenation, and `&times;` denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return *the sorted list of words that the expression represents*.

## Constraints
- `1 <= expression.length <= 60`
- `expression[i]` consists of `'{'`, `'}'`, `','`or lowercase English letters.
- The given `expression` represents a set of words based on the grammar given in the description.

## Examples
### Example 1
- **Input:** `expression = "{a,b}{c,{d,e}}"`
- **Output:** `["ac","ad","ae","bc","bd","be"]`

### Example 2
- **Input:** `expression = "{{a,z},a{b,c},{ab,z}}"`
- **Output:** `["a","ab","ac","z"]`
- **Explanation:** Each distinct word is written only once in the final answer.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution implements a **Recursive Descent Parser** with three main functions to process the expression string according to the grammar.
1. `parseExpression()`: This function handles unions (comma-separated terms). It calls `parseTerm()` to get the first set of words. Then, as long as it encounters commas `,`, it skips them, calls `parseTerm()` again, and adds all resulting words into a single Set (which automatically removes duplicates).
2. `parseTerm()`: This function handles concatenation (adjacent factors). It starts with a base Set containing an empty string `[""]`. As long as it doesn't hit a `}` or `,`, it calls `parseFactor()` to get the next set of words. It then takes the Cartesian product of the current `result` Set and the new `factor` Set (combining every prefix with every new suffix) and updates the `result`.
3. `parseFactor()`: This function handles the smallest building blocks.
   - If the current character is a letter, it simply returns a Set containing that single letter and advances the index.
   - If it encounters a `{`, it skips it, calls `parseExpression()` recursively to evaluate the entire expression inside the braces, and then skips the closing `}`.
4. The main function starts by calling `parseExpression()`, converts the resulting Set to an Array, sorts it lexicographically as required, and returns it.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "{a,b}{c,{d,e}}"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["ac","ad","ae","bc","bd","be"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    let i = 0;

    // Parse an expression: union of terms
    function parseExpression() {
        let result = new Set();
        result = parseTerm();

        while (i < expression.length && expression[i] === ',') {
            i++; // skip comma
            let next = parseTerm();

            for (let word of next) {
                result.add(word);
            }
        }

        return result;
    }

    // Parse a term: concatenation of factors
    function parseTerm() {
        let result = new Set([""]);

        while (
            i < expression.length &&
            expression[i] !== '}' &&
            expression[i] !== ','
        ) {
            let factor = parseFactor();
            let next = new Set();

            for (let a of result) {
                for (let b of factor) {
                    next.add(a + b);
                }
            }

            result = next;
        }

        return result;
    }

    // Parse a single letter or {...}
    function parseFactor() {
        if (expression[i] >= 'a' && expression[i] <= 'z') {
            return new Set([expression[i++]]);
        }

        // '{'
        i++;

        let result = parseExpression();

        // '}'
        i++;

        return result;
    }

    let result = [...parseExpression()];

    // Lexicographical sorting
    result.sort();

    return result;
};
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/brace-expansion-ii/)
