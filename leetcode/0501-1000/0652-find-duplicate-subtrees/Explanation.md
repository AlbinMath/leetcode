# LeetCode 652: Find Duplicate Subtrees

**LeetCode Problem #652 — Find Duplicate Subtrees**
Solve LeetCode Find Duplicate Subtrees using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Duplicate Subtrees |
| LeetCode | #652 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return all **duplicate subtrees**.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are **duplicate** if they have the **same structure** with the **same node values**.

## Constraints
- The number of the nodes in the tree will be in the range `[1, 5000]`
- `-200 <= Node.val <= 200`

## Examples
### Example 1
- **Input:** `root = [1,2,3,4,null,2,4,null,null,4]`
- **Output:** `[[2,4],[4]]`

### Example 2
- **Input:** `root = [2,1,1]`
- **Output:** `[[1]]`

### Example 3
- **Input:** `root = [2,2,2,3,null,3,null]`
- **Output:** `[[2,3],[3]]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Duplicate Subtrees**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,4,null,2,4,null,null,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,4],[4]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import sys
from collections import defaultdict
from typing import List, Optional

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sys.setrecursionlimit(10000)
        ids = {}                    # (left_id, val, right_id) -> id
        count = defaultdict(int)    # id -> occurrences
        ans = []

        def dfs(node):
            if not node:
                return 0
            key = (dfs(node.left), node.val, dfs(node.right))
            if key not in ids:
                ids[key] = len(ids) + 1
            i = ids[key]
            count[i] += 1
            if count[i] == 2:
                ans.append(node)
            return i

        dfs(root)
        return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [287. Find the Duplicate Number](../../0001-0500/0287-find-the-duplicate-number/)
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1617-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-duplicate-subtrees/)
