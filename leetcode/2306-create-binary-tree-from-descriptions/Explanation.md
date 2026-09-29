# Create Binary Tree From Descriptions

## Problem Explanation
Given descriptions `[parent, child, isLeft]`, build the binary tree and return its root.

## How the Code Works
1. Create all nodes in a hash map (value → TreeNode).
2. Process each description: link parent to child as left or right child. Track which nodes are children.
3. The root is the only node that never appears as a child.
