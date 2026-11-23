# LeetCode 2042: Check if Numbers Are Ascending in a Sentence

**LeetCode Problem #2042 — Check if Numbers Are Ascending in a Sentence**
Solve LeetCode Check if Numbers Are Ascending in a Sentence using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Numbers Are Ascending in a Sentence |
| LeetCode | #2042 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A sentence is a list of **tokens** separated by a **single** space with no leading or trailing spaces. Every token is either a **positive number** consisting of digits `0-9` with no leading zeros, or a **word** consisting of lowercase English letters.

For example, `"a puppy has 2 eyes 4 legs"` is a sentence with seven tokens: `"2"` and `"4"` are numbers and the other tokens such as `"puppy"` are words.

Given a string `s` representing a sentence, you need to check if **all** the numbers in `s` are **strictly increasing** from left to right (i.e., other than the last number, **each** number is **strictly smaller** than the number on its **right** in `s`).

Return `true`* if so, or *`false`* otherwise*.

## Constraints
- `3 <= s.length <= 200`
- `s` consists of lowercase English letters, spaces, and digits from `0` to `9`, inclusive.
- The number of tokens in `s` is between `2` and `100`, inclusive.
- The tokens in `s` are separated by a single space.
- There are at least **two** numbers in `s`.
- Each number in `s` is a **positive** number **less** than `100`, with no leading zeros.
- `s` contains no leading or trailing spaces.

## Examples
### Example 1
- **Input:** `s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"`
- **Output:** `true`
- **Explanation:** The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

### Example 2
- **Input:** `s = "hello world 5 x 5"`
- **Output:** `false`
- **Explanation:** The numbers in s are:

### Example 3
- **Input:** `s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"`
- **Output:** `false`
- **Explanation:** The numbers in s are: 7,

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if Numbers Are Ascending in a Sentence**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var areNumbersAscending = function(s) {
    const words = s.split(" ");
    let prev = 0;

    for (const word of words) {
        if (!isNaN(word)) {
            const num = Number(word);

            if (num <= prev) {
                return false;
            }

            prev = num;
        }
    }

    return true;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1832. Check if the Sentence Is Pangram](../../1501-2000/1960-check-if-the-sentence-is-pangram/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/)
