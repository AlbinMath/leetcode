# LeetCode 388: Longest Absolute File Path

**LeetCode Problem #388 — Longest Absolute File Path**
Solve LeetCode Longest Absolute File Path using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Absolute File Path |
| LeetCode | #388 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:

Here, we have `dir` as the only directory in the root. `dir` contains two subdirectories, `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and subdirectory `subsubdir1`. `subdir2` contains a subdirectory `subsubdir2`, which contains a file `file2.ext`.

In text form, it looks like this (with ⟶ representing the tab character):

dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext

If we were to write this representation in code, it will look like this: `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`. Note that the `'\n'` and `'\t'` are the new-line and tab characters.

Every file and directory has a unique **absolute path** in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by `'/'s`. Using the above example, the **absolute path** to `file2.ext` is `"dir/subdir2/subsubdir2/file2.ext"`. Each directory name consists of letters, digits, and/or spaces. Each file name is of the form `name.extension`, where `name` and `extension` consist of letters, digits, and/or spaces.

Given a string `input` representing the file system in the explained format, return *the length of the **longest absolute path** to a **file** in the abstracted file system*. If there is no file in the system, return `0`.

**Note** that the testcases are generated such that the file system is valid and no file or directory name has length 0.

## Constraints
- `1 <= input.length <= 10^4`
- `input` may contain lowercase or uppercase English letters, a new line character `'\n'`, a tab character `'\t'`, a dot `'.'`, a space `' '`, and digits.
- All file and directory names have **positive** length.

## Examples
### Example 1
- **Input:** `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
- **Output:** `20`
- **Explanation:** We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.

### Example 2
- **Input:** `input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`
- **Output:** `32`
- **Explanation:** We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest absolute path to a file.

### Example 3
- **Input:** `input = "a"`
- **Output:** `0`
- **Explanation:** We do not have any files, just a single directory named "a".

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Absolute File Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var lengthLongestPath = function(input) {
    const paths = input.split('\n');

    // Store path lengths at each depth
    const stack = [0];

    let maxLength = 0;

    for (let path of paths) {
        // Count directory depth
        const depth = path.lastIndexOf('\t') + 1;

        // Remove tab characters
        const name = path.slice(depth);

        // Calculate current absolute path length
        const currentLength = stack[depth] + name.length;

        if (name.includes('.')) {
            // It is a file
            maxLength = Math.max(maxLength, currentLength);
        } else {
            // It is a directory
            stack[depth + 1] = currentLength + 1;
        }
    }

    return maxLength;
};
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
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [687. Longest Univalue Path](../../0501-1000/0687-longest-univalue-path/)
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1474-longest-zigzag-path-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-absolute-file-path/)
