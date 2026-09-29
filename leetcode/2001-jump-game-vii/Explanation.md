# Jump Game VII

## Problem Explanation
Given a binary string `s`, starting at index 0, you can jump to index `i` if `s[i] == '0'` and the jump length is between `minJump` and `maxJump`. Return whether you can reach the last index.

## How the Code Works
The code uses **BFS/DP with a sliding window** to avoid redundant checks. It maintains a window of reachable positions and uses a prefix sum or queue to efficiently determine which new positions can be reached within the `[minJump, maxJump]` range.

Time complexity is $O(N)$ and space complexity is $O(N)$.
