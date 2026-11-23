# LeetCode 71: Simplify Path

**LeetCode Problem #71 — Simplify Path**
Solve LeetCode Simplify Path using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Simplify Path |
| LeetCode | #71 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an *absolute* path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path**.

The *rules* of a Unix-style file system are as follows:

A single period `'.'` represents the current directory. 
 A double period `'..'` represents the previous/parent directory. 
 Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`. 
 Any sequence of periods that does **not match** the rules above should be treated as a **valid directory or** **file ****name**. For example, `'...' `and `'....'` are valid directory or file names.

The simplified canonical path should follow these *rules*:

The path must start with a single slash `'/'`. 
 Directories within the path must be separated by exactly one slash `'/'`. 
 The path must not end with a slash `'/'`, unless it is the root directory. 
 The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.

Return the **simplified canonical path**.

## Constraints
- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.

## Examples
### Example 1
- **Input:** `path = "/home/"`
- **Output:** `"/home"`
- **Explanation:** The trailing slash should be removed.

### Example 2
- **Input:** `path = "/home//foo/"`
- **Output:** `"/home/foo"`
- **Explanation:** Multiple consecutive slashes are replaced by a single one.

### Example 3
- **Input:** `path = "/home/user/Documents/../Pictures"`
- **Output:** `"/home/user/Pictures"`
- **Explanation:** A double period `".."` refers to the directory up a level (the parent directory).

### Example 4
- **Input:** `path = "/../"`
- **Output:** `"/"`
- **Explanation:** Going one level up from the root directory is not possible.

### Example 5
- **Input:** `path = "/.../a/../b/c/../d/./"`
- **Output:** `"/.../b/d"`
- **Explanation:** `"..."` is a valid name for a directory in this problem.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Simplify Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `path = "/home/"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"/home"`.
4. **Verification:** The trailing slash should be removed.

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
    def simplifyPath(self, path):
        stack = []

        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue

            elif part == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(part)

        return '/' + '/'.join(stack)
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [112. Path Sum](../../0001-0500/0112-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/simplify-path/)
