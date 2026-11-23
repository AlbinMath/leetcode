# LeetCode 2807: Insert Greatest Common Divisors in Linked List

**LeetCode Problem #2807 — Insert Greatest Common Divisors in Linked List**
Solve LeetCode Insert Greatest Common Divisors in Linked List using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Greatest Common Divisors in Linked List |
| LeetCode | #2807 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the head of a linked list `head`, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.

Return *the linked list after insertion*.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

## Constraints
- The number of nodes in the list is in the range `[1, 5000]`.
- `1 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `head = [18,6,10,3]`
- **Output:** `[18,6,6,2,10,1,3]`
- **Explanation:** The 1^st diagram denotes the initial linked list and the 2^nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1^st and the 2^nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2^nd and the 3^rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3^rd and the 4^th nodes.
There are no more adjacent nodes, so we return the linked list.

### Example 2
- **Input:** `head = [7]`
- **Output:** `[7]`
- **Explanation:** The 1^st diagram denotes the initial linked list and the 2^nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Insert Greatest Common Divisors in Linked List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [18,6,10,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[18,6,6,2,10,1,3]`.
4. **Verification:** The 1^st diagram denotes the initial linked list and the 2^nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1^st and the 2^nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2^nd and the 3^rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3^rd and the 4^th nodes.
There are no more adjacent nodes, so we return the linked list.

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
var insertGreatestCommonDivisors = function(head) {

    // Calculate GCD using Euclidean Algorithm
    function gcd(a, b) {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    let current = head;

    // Traverse the linked list
    while (current && current.next) {

        // Calculate GCD of adjacent nodes
        let value = gcd(current.val, current.next.val);

        // Create new node
        let node = new ListNode(value);

        // Insert new node between current and next
        node.next = current.next;
        current.next = node;

        // Move to the next original node
        current = node.next;
    }

    return head;
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
- [1071. Greatest Common Divisor of Strings](../../1001-1500/1146-greatest-common-divisor-of-strings/)
- [1979. Find Greatest Common Divisor of Array](../../2001-2500/2106-find-greatest-common-divisor-of-array/)
- [2709. Greatest Common Divisor Traversal](../../2501-3000/2827-greatest-common-divisor-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/)
