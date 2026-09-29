# Rotate List

## Problem Explanation
Given the `head` of a linked list, rotate the list to the right by `k` places. Each rotation moves the last element to the front.

For example, if the list is `[1, 2, 3, 4, 5]` and `k = 2`:
- After 1 rotation: `[5, 1, 2, 3, 4]`
- After 2 rotations: `[4, 5, 1, 2, 3]`

## How the Code Works
1. **Edge Cases:** Returns immediately if the list is empty, has one node, or `k` is 0.
2. **Find Length and Tail:** Traverses the list to find its length `n` and a pointer to the `tail` node.
3. **Effective Rotations:** Computes `k = k % n` to avoid redundant full rotations. If `k` becomes 0, no rotation is needed.
4. **Make Circular:** Connects the tail to the head (`tail->next = head`), creating a circular list.
5. **Find the New Tail:** The new tail is the node at position `n - k - 1` from the current head (i.e., `steps = n - k` steps from the beginning). This is where the list will be "cut."
6. **Break the Circle:** The new head is `newTail->next`, and the circle is broken by setting `newTail->next = nullptr`.

Time complexity is $O(N)$ and space complexity is $O(1)$.
