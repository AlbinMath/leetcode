# LeetCode 61: Rotate List

**LeetCode Problem #61 — Rotate List**
Solve LeetCode Rotate List using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate List |
| LeetCode | #61 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `head` of a linked list, rotate the list to the right by `k` places.

## Constraints
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Examples
### Example 1
- **Input:** `head = [1,2,3,4,5], k = 2`
- **Output:** `[4,5,1,2,3]`

### Example 2
- **Input:** `head = [0,1,2], k = 4`
- **Output:** `[2,0,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
1. **Edge Cases:** Returns immediately if the list is empty, has one node, or `k` is 0.
2. **Find Length and Tail:** Traverses the list to find its length `n` and a pointer to the `tail` node.
3. **Effective Rotations:** Computes `k = k % n` to avoid redundant full rotations. If `k` becomes 0, no rotation is needed.
4. **Make Circular:** Connects the tail to the head (`tail->next = head`), creating a circular list.
5. **Find the New Tail:** The new tail is the node at position `n - k - 1` from the current head (i.e., `steps = n - k` steps from the beginning). This is where the list will be "cut."
6. **Break the Circle:** The new head is `newTail->next`, and the circle is broken by setting `newTail->next = nullptr`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `head = [1,2,3,4,5], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,5,1,2,3]`.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // Empty list or single node
        if (head == nullptr || head->next == nullptr || k == 0) {
            return head;
        }

        // Find length and tail
        int n = 1;
        ListNode* tail = head;

        while (tail->next != nullptr) {
            tail = tail->next;
            n++;
        }

        // Avoid unnecessary rotations
        k = k % n;

        if (k == 0) {
            return head;
        }

        // Make the list circular
        tail->next = head;

        // Find the new tail
        int steps = n - k;
        ListNode* newTail = head;

        for (int i = 1; i < steps; i++) {
            newTail = newTail->next;
        }

        // New head comes after the new tail
        ListNode* newHead = newTail->next;

        // Break the circle
        newTail->next = nullptr;

        return newHead;
    }
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
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)
- [82. Remove Duplicates from Sorted List II](../../0001-0500/0082-remove-duplicates-from-sorted-list-ii/)
- [83. Remove Duplicates from Sorted List](../../0001-0500/0083-remove-duplicates-from-sorted-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-list/)
