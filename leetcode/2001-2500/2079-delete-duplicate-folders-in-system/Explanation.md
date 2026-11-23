# LeetCode 1948: Delete Duplicate Folders in System

**LeetCode Problem #1948 — Delete Duplicate Folders in System**
Solve LeetCode Delete Duplicate Folders in System using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Duplicate Folders in System |
| LeetCode | #1948 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array `paths`, where `paths[i]` is an array representing an absolute path to the `i^th` folder in the file system.

For example, `["one", "two", "three"]` represents the path `"/one/two/three"`.

Two folders (not necessarily on the same level) are **identical** if they contain the **same non-empty** set of identical subfolders and underlying subfolder structure. The folders **do not** need to be at the root level to be identical. If two or more folders are **identical**, then **mark** the folders as well as all their subfolders.

For example, folders `"/a"` and `"/b"` in the file structure below are identical. They (as well as their subfolders) should **all** be marked:

`/a` 
 `/a/x` 
 `/a/x/y` 
 `/a/z` 
 `/b` 
 `/b/x` 
 `/b/x/y` 
 `/b/z` 
 
 
 However, if the file structure also included the path `"/b/w"`, then the folders `"/a"` and `"/b"` would not be identical. Note that `"/a/x"` and `"/b/x"` would still be considered identical even with the added folder.

Once all the identical folders and their subfolders have been marked, the file system will **delete** all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return *the 2D array *`ans` *containing the paths of the **remaining** folders after deleting all the marked folders. The paths may be returned in **any** order*.

## Constraints
- `1 <= paths.length <= 2 * 10^4`
- `1 <= paths[i].length <= 500`
- `1 <= paths[i][j].length <= 10`
- `1 <= sum(paths[i][j].length) <= 2 * 10^5`
- `path[i][j]` consists of lowercase English letters.
- No two paths lead to the same folder.
- For any folder not at the root level, its parent folder will also be in the input.

## Examples
### Example 1
- **Input:** `paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]`
- **Output:** `[["d"],["d","a"]]`
- **Explanation:** The file structure is as shown.
Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
folder named "b".

### Example 2
- **Input:** `paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]`
- **Output:** `[["c"],["c","b"],["a"],["a","b"]]`
- **Explanation:** The file structure is as shown. 
Folders "/a/b/x" and "/w" (and their subfolders) are marked for deletion because they both contain an empty folder named "y".
Note that folders "/a" and "/c" are identical after the deletion, but they are not deleted because they were not marked beforehand.

### Example 3
- **Input:** `paths = [["a","b"],["c","d"],["c"],["a"]]`
- **Output:** `[["c"],["c","d"],["a"],["a","b"]]`
- **Explanation:** All folders are unique in the file system.
Note that the returned array can be in a different order as the order does not matter.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Delete Duplicate Folders in System**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["d"],["d","a"]]`.
4. **Verification:** The file structure is as shown.
Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
folder named "b".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class Node:
            __slots__ = ("children", "sig")
            def __init__(self):
                self.children = {}
                self.sig = ""

        root = Node()
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = Node()
                node = node.children[name]

        freq = defaultdict(int)

        # post-order, iterative to avoid recursion limits (depth up to 500)
        stack = [(root, False)]
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node, True))
                for child in node.children.values():
                    stack.append((child, False))
            else:
                if node.children:
                    parts = [name + "(" + c.sig + ")"
                             for name, c in sorted(node.children.items())]
                    node.sig = "".join(parts)
                    freq[node.sig] += 1

        ans = []
        path = []

        def collect(node: Node) -> None:
            for name, child in node.children.items():
                if child.sig and freq[child.sig] > 1:
                    continue                 # marked: skip this whole subtree
                path.append(name)
                ans.append(path[:])
                collect(child)
                path.pop()

        collect(root)
        return ans
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)
- [196. Delete Duplicate Emails](../../0001-0500/0196-delete-duplicate-emails/)
- [1233. Remove Sub-Folders from the Filesystem](../../1001-1500/1350-remove-sub-folders-from-the-filesystem/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-duplicate-folders-in-system/)
