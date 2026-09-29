# Check If There Is A Valid Parentheses String Path

## Problem Explanation
Given a grid of `(` and `)`, determine if there's a path from top-left to bottom-right (moving only right or down) that forms a valid parentheses string.

## How the Code Works
Uses **DP with state tracking**. At each cell, track the set of possible open-parenthesis counts. Moving right or down, increment count for `(` and decrement for `)`. A path is valid if we reach the bottom-right with count exactly 0. Prune states where count goes negative.
