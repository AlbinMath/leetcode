# LeetCode 2645: Minimum Additions to Make Valid String

**LeetCode Problem #2645 — Minimum Additions to Make Valid String**
Solve LeetCode Minimum Additions to Make Valid String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Additions to Make Valid String |
| LeetCode | #2645 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `word` to which you can insert letters "a", "b" or "c" anywhere and any number of times, return *the minimum number of letters that must be inserted so that `word` becomes **valid**.*

A string is called **valid **if it can be formed by concatenating the string "abc" several times.

## Constraints
- `1 <= word.length <= 50`
- `word` consists of letters "a", "b" and "c" only.

## Examples
### Example 1
- **Input:** `word = "b"`
- **Output:** `2`
- **Explanation:** Insert the letter "a" right before "b", and the letter "c" right next to "b" to obtain the valid string "

### Example 2
- **Input:** `word = "aaa"`
- **Output:** `6`
- **Explanation:** Insert letters "b" and "c" next to each "a" to obtain the valid string "a

### Example 3
- **Input:** `word = "abc"`
- **Output:** `0`
- **Explanation:** word is already valid. No modifications are needed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Additions to Make Valid String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "b"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Insert the letter "a" right before "b", and the letter "c" right next to "b" to obtain the valid string "

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def addMinimum(self, word: str) -> int:
        k = 1 + sum(word[i] <= word[i - 1] for i in range(1, len(word)))
        return 3 * k - len(word)
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
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)
- [1249. Minimum Remove to Make Valid Parentheses](../../1001-1500/1249-minimum-remove-to-make-valid-parentheses/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1312-minimum-insertion-steps-to-make-a-string-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-additions-to-make-valid-string/)
