# LeetCode 2196: Create Binary Tree From Descriptions

**LeetCode Problem #2196 — Create Binary Tree From Descriptions**
Solve LeetCode Create Binary Tree From Descriptions using Java, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Binary Tree From Descriptions |
| LeetCode | #2196 |
| Difficulty | Medium |
| Language | Java, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the **parent** of `child_i` in a **binary** tree of **unique** values. Furthermore,

If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`. 
 If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.

Construct the binary tree described by `descriptions` and return *its **root***.

The test cases will be generated such that the binary tree is **valid**.

## Constraints
- `1 <= descriptions.length <= 10^4`
- `descriptions[i].length == 3`
- `1 <= parent_i, child_i <= 10^5`
- `0 <= isLeft_i <= 1`
- The binary tree described by `descriptions` is valid.

## Examples
### Example 1
- **Input:** `descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`
- **Output:** `[50,20,80,15,17,19]`
- **Explanation:** The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

### Example 2
- **Input:** `descriptions = [[1,2,1],[2,3,0],[3,4,1]]`
- **Output:** `[1,2,null,null,3,4]`
- **Explanation:** The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. Create all nodes in a hash map (value → TreeNode).
2. Process each description: link parent to child as left or right child. Track which nodes are children.
3. The root is the only node that never appears as a child.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[50,20,80,15,17,19]`.
4. **Verification:** The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

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
Java, Python

## Source Code
- [solution.java](./solution.java)
- [solution.py](./solution.py)


### Java
```java
class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> map = new HashMap<>();
        Set<Integer> children = new HashSet<>();

        for (int[] d : descriptions) {
            int parent = d[0];
            int child = d[1];
            int isLeft = d[2];

            // Create nodes if they don't exist
            map.putIfAbsent(parent, new TreeNode(parent));
            map.putIfAbsent(child, new TreeNode(child));

            // Connect parent and child
            if (isLeft == 1) {
                map.get(parent).left = map.get(child);
            } else {
                map.get(parent).right = map.get(child);
            }

            // Child cannot be the root
            children.add(child);
        }

        // Find the node that never appeared as a child
        for (int value : map.keySet()) {
            if (!children.contains(value)) {
                return map.get(value);
            }
        }

        return null;
    }
}
```

### Python
```python
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes, children = {}, set()

        for p, c, left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            children.add(c)

        return nodes[next(iter(set(nodes) - children))]
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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/)
