# LeetCode 129: Sum Root to Leaf Numbers

**LeetCode Problem #129 — Sum Root to Leaf Numbers**
Solve LeetCode Sum Root to Leaf Numbers using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum Root to Leaf Numbers |
| LeetCode | #129 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`.

## Examples
### Example 1
- **Input:** `root = [1,2,3]`
- **Output:** `25`
- **Explanation:** The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = `25`.

### Example 2
- **Input:** `root = [4,9,0,5,1]`
- **Output:** `1026`
- **Explanation:** The root-to-leaf path `4->9->5` represents the number 495.
The root-to-leaf path `4->9->1` represents the number 491.
The root-to-leaf path `4->0` represents the number 40.
Therefore, sum = 495 + 491 + 40 = `1026`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum Root to Leaf Numbers**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `25`.
4. **Verification:** The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = `25`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sumNumbers = function(root) {
    let total = 0;

    function dfs(node, currentNumber) {
        if (node === null) {
            return;
        }

        currentNumber = currentNumber * 10 + node.val;

        // Check if this is a leaf node
        if (node.left === null && node.right === null) {
            total += currentNumber;
            return;
        }

        dfs(node.left, currentNumber);
        dfs(node.right, currentNumber);
    }

    dfs(root, 0);

    return total;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1022. Sum of Root To Leaf Binary Numbers](../../1001-1500/1022-sum-of-root-to-leaf-binary-numbers/)
- [1080. Insufficient Nodes in Root to Leaf Paths](../../1001-1500/1080-insufficient-nodes-in-root-to-leaf-paths/)
- [633. Sum of Square Numbers](../../0501-1000/0633-sum-of-square-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
