# Count Nodes Equal To Average Of Subtree

## Problem Explanation
Return the number of nodes where the node's value equals the average of values in its subtree.

## How the Code Works
Use **DFS** (post-order traversal). Each recursive call returns the `(sum, count)` of the subtree. At each node, compute `average = sum / count` and check if it equals the node's value.
