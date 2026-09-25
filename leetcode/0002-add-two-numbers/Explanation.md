# Add Two Numbers

## Problem Explanation
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, which means the head of the linked list contains the least significant digit (ones place). Each node in the list contains a single digit. Your task is to add the two numbers together and return the sum as a new linked list, also in reverse order.

For example, `[2, 4, 3]` and `[5, 6, 4]` represent the numbers 342 and 465. Adding them gives 807, which is represented as `[7, 0, 8]` in the linked list.

## How the Code Works
The code uses a simulated digit-by-digit addition, similar to how you would add numbers on paper:
1. It initializes a `dummy` node to act as the head of the result list, and a `current` pointer to build the new list.
2. It uses a `carry` variable (initially 0) to keep track of values that carry over to the next place value (e.g., if sum >= 10).
3. A `while` loop runs as long as there is a node in `l1`, a node in `l2`, or a remaining `carry` greater than 0.
4. Inside the loop, it safely extracts the values from `l1` and `l2` (defaulting to 0 if one list is shorter than the other).
5. It calculates the `total` sum for the current position (`val1 + val2 + carry`).
6. The `digit` to store in the new node is `total % 10`, and the new `carry` for the next iteration is `total // 10`.
7. It creates a new node with this `digit`, attaches it to the result list, and moves all pointers (`l1`, `l2`, and `current`) forward.
8. Finally, it returns `dummy.next`, which is the head of the newly constructed sum list.
