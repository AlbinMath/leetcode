# LeetCode 138: Copy List with Random Pointer

**LeetCode Problem #138 — Copy List with Random Pointer**
Solve LeetCode Copy List with Random Pointer using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Copy List with Random Pointer |
| LeetCode | #138 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

`val`: an integer representing `Node.val` 
 `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

## Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

## Examples
### Example 1
- **Input:** `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
- **Output:** `[[7,null],[13,0],[11,4],[10,2],[1,0]]`

### Example 2
- **Input:** `head = [[1,1],[2,1]]`
- **Output:** `[[1,1],[2,1]]`

### Example 3
- **Input:** `head = [[3,null],[3,0],[3,null]]`
- **Output:** `[[3,null],[3,0],[3,null]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Copy List with Random Pointer**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[7,null],[13,0],[11,4],[10,2],[1,0]]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var copyRandomList = function(head) {
    if (head === null) return null;

    const map = new Map();

    // Step 1: Create a copy of every node
    let current = head;

    while (current !== null) {
        map.set(current, new Node(current.val));
        current = current.next;
    }

    // Step 2: Connect next and random pointers
    current = head;

    while (current !== null) {
        const copy = map.get(current);

        copy.next = current.next
            ? map.get(current.next)
            : null;

        copy.random = current.random
            ? map.get(current.random)
            : null;

        current = current.next;
    }

    return map.get(head);
};
```

### Python
```python
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        d = {None: None}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
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
- [382. Linked List Random Node](../../0001-0500/0382-linked-list-random-node/)
- [398. Random Pick Index](../../0001-0500/0398-random-pick-index/)
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)
