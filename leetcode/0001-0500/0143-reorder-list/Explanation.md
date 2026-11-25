# LeetCode 143: Reorder List

**LeetCode Problem #143 — Reorder List**
Solve LeetCode Reorder List using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reorder List |
| LeetCode | #143 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the head of a singly linked-list. The list can be represented as:

L_0 &rarr; L_1 &rarr; &hellip; &rarr; L_n - 1 &rarr; L_n

*Reorder the list to be on the following form:*

L_0 &rarr; L_n &rarr; L_1 &rarr; L_n - 1 &rarr; L_2 &rarr; L_n - 2 &rarr; &hellip;

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Constraints
- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4]`
- **Output:** `[1,4,2,3]`

### Example 2
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[1,5,2,4,3]`

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reorder List**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,4,2,3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var reorderList = function(head) {
    if (!head || !head.next) return;

    // Step 1: Find the middle of the linked list
    let slow = head;
    let fast = head;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Step 2: Reverse the second half
    let second = slow.next;
    slow.next = null;

    let prev = null;

    while (second) {
        let nextNode = second.next;
        second.next = prev;
        prev = second;
        second = nextNode;
    }

    // Step 3: Merge the two halves alternately
    let first = head;
    second = prev;

    while (second) {
        let temp1 = first.next;
        let temp2 = second.next;

        first.next = second;
        second.next = temp1;

        first = temp1;
        second = temp2;
    }
};
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [937. Reorder Data in Log Files](../../0501-1000/0937-reorder-data-in-log-files/)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../../1001-1500/1466-reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reorder-list/)
