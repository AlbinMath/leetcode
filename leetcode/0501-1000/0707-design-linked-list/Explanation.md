# LeetCode 707: Design Linked List

**LeetCode Problem #707 — Design Linked List**
Solve LeetCode Design Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Linked List |
| LeetCode | #707 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design your implementation of the linked list. You can choose to use a singly or doubly linked list. 
A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are **0-indexed**.

Implement the `MyLinkedList` class:

`MyLinkedList()` Initializes the `MyLinkedList` object. 
 `int get(int index)` Get the value of the `index^th` node in the linked list. If the index is invalid, return `-1`. 
 `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list. 
 `void addAtIndex(int index, int val)` Add a node of value `val` before the `index^th` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node **will not be inserted**. 
 `void deleteAtIndex(int index)` Delete the `index^th` node in the linked list, if the index is valid.

## Constraints
- `0 <= index, val <= 1000`
- Please do not use the built-in LinkedList library.
- At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex` and `deleteAtIndex`.

## Examples
### Example 1
- **Input:** `["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]`
- **Output:** `[null, null, null, null, 2, null, 3]`
- **Explanation:** MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2); // linked list becomes 1->2->3
myLinkedList.get(1); // return 2
myLinkedList.deleteAtIndex(1); // now the linked list is 1->3
myLinkedList.get(1); // return 3

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Design Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, 2, null, 3]`.
4. **Verification:** MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2); // linked list becomes 1->2->3
myLinkedList.get(1); // return 2
myLinkedList.deleteAtIndex(1); // now the linked list is 1->3
myLinkedList.get(1); // return 3

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var MyLinkedList = function() {
    this.head = null;
    this.size = 0;
};

// Node structure
var ListNode = function(val) {
    this.val = val;
    this.next = null;
};

// Get value at index
MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.size) {
        return -1;
    }

    let current = this.head;

    for (let i = 0; i < index; i++) {
        current = current.next;
    }

    return current.val;
};

// Add node at head
MyLinkedList.prototype.addAtHead = function(val) {
    let node = new ListNode(val);

    node.next = this.head;
    this.head = node;

    this.size++;
};

// Add node at tail
MyLinkedList.prototype.addAtTail = function(val) {
    let node = new ListNode(val);

    if (!this.head) {
        this.head = node;
    } else {
        let current = this.head;

        while (current.next) {
            current = current.next;
        }

        current.next = node;
    }

    this.size++;
};

// Add node at given index
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if (index < 0) {
        index = 0;
    }

    if (index > this.size) {
        return;
    }

    if (index === 0) {
        this.addAtHead(val);
        return;
    }

    let current = this.head;

    for (let i = 0; i < index - 1; i++) {
        current = current.next;
    }

    let node = new ListNode(val);

    node.next = current.next;
    current.next = node;

    this.size++;
};

// Delete node at given index
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.size) {
        return;
    }

    if (index === 0) {
        this.head = this.head.next;
    } else {
        let current = this.head;

        for (let i = 0; i < index - 1; i++) {
            current = current.next;
        }

        current.next = current.next.next;
    }

    this.size--;
};
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
- [92. Reverse Linked List II](../../0001-0500/0092-reverse-linked-list-ii/)
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-linked-list/)
