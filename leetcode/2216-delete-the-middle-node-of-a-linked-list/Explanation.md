# Delete The Middle Node Of A Linked List

## Problem Explanation
Delete the middle node of a linked list. If there are two middle nodes, delete the second one.

## How the Code Works
Use **fast and slow pointers**. Fast moves 2 steps while slow moves 1. When fast reaches the end, slow is just before the middle. Delete the middle by setting `slow.next = slow.next.next`.
