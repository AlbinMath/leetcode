# LeetCode 212: Word Search II

**LeetCode Problem #212 — Word Search II**
Solve LeetCode Word Search II using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Search II |
| LeetCode | #212 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

## Examples
### Example 1
- **Input:** `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]`
- **Output:** `["eat","oath"]`

### Example 2
- **Input:** `board = [["a","b"],["c","d"]], words = ["abcb"]`
- **Output:** `[]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Word Search II**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["eat","oath"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findWords = function(board, words) {
    const root = {};

    // Build the Trie
    for (const word of words) {
        let node = root;

        for (const char of word) {
            if (!node[char]) {
                node[char] = {};
            }
            node = node[char];
        }

        node.word = word;
    }

    const m = board.length;
    const n = board[0].length;
    const result = [];

    function dfs(row, col, node) {
        const char = board[row][col];
        const nextNode = node[char];

        if (!nextNode) return;

        // Found a complete word
        if (nextNode.word !== undefined) {
            result.push(nextNode.word);

            // Prevent finding the same word again
            nextNode.word = undefined;
        }

        // Mark this cell as visited
        board[row][col] = "#";

        const directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ];

        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;

            if (
                nr >= 0 &&
                nr < m &&
                nc >= 0 &&
                nc < n &&
                board[nr][nc] !== "#"
            ) {
                dfs(nr, nc, nextNode);
            }
        }

        // Restore the original character
        board[row][col] = char;
    }

    // Start DFS from every cell
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            dfs(row, col, root);
        }
    }

    return result;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [79. Word Search](../../0001-0500/0079-word-search/)
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-search-ii/)
