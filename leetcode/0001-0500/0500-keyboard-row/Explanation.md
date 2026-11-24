# LeetCode 500: Keyboard Row

**LeetCode Problem #500 — Keyboard Row**
Solve LeetCode Keyboard Row using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Keyboard Row |
| LeetCode | #500 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

**Note** that the strings are **case-insensitive**, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the **American keyboard**:

the first row consists of the characters `"qwertyuiop"`, 
 the second row consists of the characters `"asdfghjkl"`, and 
 the third row consists of the characters `"zxcvbnm"`.

## Constraints
- `1 <= words.length <= 20`
- `1 <= words[i].length <= 100`
- `words[i]` consists of English letters (both lowercase and uppercase).

## Examples
### Example 1
- **Input:** `words = ["Hello","Alaska","Dad","Peace"]`
- **Output:** `["Alaska","Dad"]`
- **Explanation:** Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

### Example 2
- **Input:** `words = ["omk"]`
- **Output:** `[]`

### Example 3
- **Input:** `words = ["adsdf","sfd"]`
- **Output:** `["adsdf","sfd"]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Keyboard Row**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["Hello","Alaska","Dad","Peace"]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["Alaska","Dad"]`.
4. **Verification:** Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            lower_word = word.lower()

            for row in rows:
                if all(ch in row for ch in lower_word):
                    result.append(word)
                    break

        return result
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [623. Add One Row to Tree](../../0501-1000/0623-add-one-row-to-tree/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0947-most-stones-removed-with-same-row-or-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/keyboard-row/)
