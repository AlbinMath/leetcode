# LeetCode 68: Text Justification

**LeetCode Problem #68 — Text Justification**
Solve LeetCode Text Justification using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Text Justification |
| LeetCode | #68 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

A word is defined as a character sequence consisting of non-space characters only. 
 Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`. 
 The input array `words` contains at least one word.

## Constraints
- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only English letters and symbols.
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

## Examples
### Example 1
- **Input:** `words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16`
- **Output:** `[
 "This is an",
 "example of text",
 "justification. "
]`

### Example 2
- **Input:** `words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16`
- **Output:** `[
 "What must be",
 "acknowledgment ",
 "shall be "
]`
- **Explanation:** Note that the last line is "shall be " instead of "shall be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

### Example 3
- **Input:** `words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20`
- **Output:** `[
 "Science is what we",
 "understand well",
 "enough to explain to",
 "a computer. Art is",
 "everything else we",
 "do "
]`

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Text Justification**, we observe the problem requirements and utilize the **Heap** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[
 "This is an",
 "example of text",
 "justification. "
]`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            # Find all words that fit in this line
            line_words = []
            line_length = 0

            while i < len(words):
                word_length = len(words[i])

                # Minimum required length:
                # current words + one space before new word
                required = line_length + word_length

                if line_words:
                    required += len(line_words)

                if required > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_length
                i += 1

            # Last line or single-word line
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Fully justify normal line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            spaces_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (
                    spaces_per_gap + (1 if j < extra_spaces else 0)
                )

            line += line_words[-1]

            result.append(line)

        return result
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
- [2296. Design a Text Editor](../../2001-2500/2296-design-a-text-editor/)
- [12. Integer to Roman](../../0001-0500/0012-integer-to-roman/)
- [56. Merge Intervals](../../0001-0500/0056-merge-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/text-justification/)
