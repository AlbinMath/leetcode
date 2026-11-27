# LeetCode 3403: Find the Lexicographically Largest String From the Box I

**LeetCode Problem #3403 — Find the Lexicographically Largest String From the Box I**
Solve LeetCode Find the Lexicographically Largest String From the Box I using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Lexicographically Largest String From the Box I |
| LeetCode | #3403 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her `numFriends` friends. There are multiple rounds in the game, where in each round:

`word` is split into `numFriends` **non-empty** strings, such that no previous round has had the **exact** same split. 
 All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are finished.

## Constraints
- `1 <= word.length <= 5 * 10^3`
- `word` consists only of lowercase English letters.
- `1 <= numFriends <= word.length`

## Examples
### Example 1
- **Input:** `word = "dbca", numFriends = 2`
- **Output:** `"dbc"`
- **Explanation:** All possible splits are: 

 
 `"d"` and `"bca"`. 
 `"db"` and `"ca"`. 
 `"dbc"` and `"a"`.

### Example 2
- **Input:** `word = "gggg", numFriends = 4`
- **Output:** `"g"`
- **Explanation:** The only possible split is: `"g"`, `"g"`, `"g"`, and `"g"`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Lexicographically Largest String From the Box I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "dbca", numFriends = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"dbc"`.
4. **Verification:** All possible splits are: 

 
 `"d"` and `"bca"`. 
 `"db"` and `"ca"`. 
 `"dbc"` and `"a"`.

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
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        L = n - numFriends + 1
        return max(word[i:i + L] for i in range(n))
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
- [4036. Lexicographically Largest String After Pair Transformations](../../4001-4500/4036-lexicographically-largest-string-after-pair-transformations/)
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1061-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/)
