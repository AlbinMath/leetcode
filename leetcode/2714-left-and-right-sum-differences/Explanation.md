# Left And Right Sum Differences

## Problem Explanation
Return an array where `answer[i] = |leftSum[i] - rightSum[i]|`, where leftSum is the sum of elements to the left and rightSum is the sum to the right.

## How the Code Works
Compute prefix sums for left sums and suffix sums for right sums, then calculate the absolute difference at each index.
