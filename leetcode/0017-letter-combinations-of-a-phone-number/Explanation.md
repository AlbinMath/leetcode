# Letter Combinations Of A Phone Number

## Problem Explanation
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is the same as on telephone buttons (e.g., `2 -> abc`, `3 -> def`, `7 -> pqrs`, etc.). Return the answer in any order.

For example, if `digits = "23"`:
- The output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

## How the Code Works
The code uses **Backtracking** to explore all possible letter combinations.

1. **Base Case:** If the input string is empty, it returns an empty array immediately.
2. **Digit-to-Letter Map:** A `map` object stores the mapping from each digit (`'2'` through `'9'`) to its corresponding letters.
3. **Backtracking Function:** The recursive function `backtrack(index, current)` builds one combination at a time:
   - **Termination:** When `index` equals the length of `digits`, the current combination `current` is complete and is pushed to the `result` array.
   - **Branching:** Otherwise, it looks up the letters for `digits[index]` and iterates over each letter. For each letter, it recurses with `index + 1` and `current + letter`, which extends the current combination by one character.
4. The function is initially called with `backtrack(0, "")`, starting from the first digit with an empty string.

Since each digit maps to at most 4 letters, the time complexity is $O(4^N)$ where $N$ is the number of digits, and space complexity is $O(N)$ for the recursion stack.
