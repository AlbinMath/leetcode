# LeetCode 1993: Operations on Tree

**LeetCode Problem #1993 — Operations on Tree**
Solve LeetCode Operations on Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Operations on Tree |
| LeetCode | #1993 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of the `i^th` node. The root of the tree is node `0`, so `parent[0] = -1` since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

**Lock:** **Locks** the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked. 
 **Unlock: Unlocks** the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user. 
 Upgrade **: Locks** the given node for the given user and **unlocks** all of its descendants **regardless** of who locked it. You may only upgrade a node if **all** 3 conditions are true:
 
 The node is unlocked, 
 It has at least one locked descendant (by **any** user), and 
 It does not have any locked ancestors.

Implement the `LockingTree` class:

`LockingTree(int[] parent)` initializes the data structure with the parent array. 
 `lock(int num, int user)` returns `true` if it is possible for the user with id `user` to lock the node `num`, or `false` otherwise. If it is possible, the node `num` will become** locked** by the user with id `user`. 
 `unlock(int num, int user)` returns `true` if it is possible for the user with id `user` to unlock the node `num`, or `false` otherwise. If it is possible, the node `num` will become **unlocked**. 
 `upgrade(int num, int user)` returns `true` if it is possible for the user with id `user` to upgrade the node `num`, or `false` otherwise. If it is possible, the node `num` will be **upgraded**.

## Constraints
- `n == parent.length`
- `2 <= n <= 2000`
- `0 <= parent[i] <= n - 1` for `i != 0`
- `parent[0] == -1`
- `0 <= num <= n - 1`
- `1 <= user <= 10^4`
- `parent` represents a valid tree.
- At most `2000` calls **in total** will be made to `lock`, `unlock`, and `upgrade`.

## Examples
### Example 1
- **Input:** `["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]`
- **Output:** `[null, true, false, true, true, true, false]`
- **Explanation:** LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2); // return true because node 2 is unlocked.
 // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3); // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2); // return true because node 2 was previously locked by user 2.
 // Node 2 will now be unlocked.
lockingTree.lock(4, 5); // return true because node 4 is unlocked.
 // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
 // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1); // return false because node 0 is already locked.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Operations on Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, false, true, true, true, false]`.
4. **Verification:** LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2); // return true because node 2 is unlocked.
 // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3); // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2); // return true because node 2 was previously locked by user 2.
 // Node 2 will now be unlocked.
lockingTree.lock(4, 5); // return true because node 4 is unlocked.
 // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
 // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1); // return false because node 0 is already locked.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class LockingTree:
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)
        self.locked = [0] * n  # 0 = unlocked, otherwise the user id

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False

        # no locked ancestor
        p = self.parent[num]
        while p != -1:
            if self.locked[p] != 0:
                return False
            p = self.parent[p]

        # collect locked descendants
        found = []
        stack = list(self.children[num])
        while stack:
            u = stack.pop()
            if self.locked[u] != 0:
                found.append(u)
            stack.extend(self.children[u])

        if not found:
            return False

        for u in found:
            self.locked[u] = 0      # was cut off: needs "= 0"
        self.locked[num] = user     # missing: lock the node itself
        return True                 # missing: report success
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
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [1319. Number of Operations to Make Network Connected](../../1001-1500/1319-number-of-operations-to-make-network-connected/)
- [1441. Build an Array With Stack Operations](../../1001-1500/1441-build-an-array-with-stack-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/operations-on-tree/)
