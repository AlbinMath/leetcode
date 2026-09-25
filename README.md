# LeetCode Solutions

Here are my solutions to various LeetCode problems along with brief explanations. 
For a complete list of problems, check out the [All Problems Directory](All_Problems.md).

## Problem List
- [0001 - Two Sum](leetcode/0001-two-sum/Explanation.md): Uses a hash map to find the pair of numbers that add up to a target in $O(N)$ time.
- [0002 - Add Two Numbers](leetcode/0002-add-two-numbers/Explanation.md): Simulates digit-by-digit addition for two linked lists representing reversed numbers.
- [0003 - Longest Substring Without Repeating Characters](leetcode/0003-longest-substring-without-repeating-characters/Explanation.md): Uses a sliding window and a set to find the longest substring of unique characters.
- [0004 - Median of Two Sorted Arrays](leetcode/0004-median-of-two-sorted-arrays/Explanation.md): Uses binary search to find the correct partition between the two arrays in $O(\log(m+n))$ time.
- [0005 - Longest Palindromic Substring](leetcode/0005-longest-palindromic-substring/Explanation.md): Uses the expand-around-center approach to find palindromes from each character index.
- [0006 - Zigzag Conversion](leetcode/0006-zigzag-conversion/Explanation.md): Simulates filling rows by traversing down and up to build the zigzag pattern.
- [0009 - Palindrome Number](leetcode/0009-palindrome-number/Explanation.md): Reverses the number mathematically without converting it to a string.
- [0013 - Roman to Integer](leetcode/0013-roman-to-integer/Explanation.md): Iterates through the Roman numeral string and subtracts values when a smaller numeral precedes a larger one.
- [0014 - Longest Common Prefix](leetcode/0014-longest-common-prefix/Explanation.md): Compares the prefix of the first string with subsequent strings, progressively shortening it.
- [1188 - Brace Expansion II](leetcode/1188-brace-expansion-ii/Explanation.md): Implements a recursive descent parser to expand and combine sets of strings using union and cartesian product.
- [1776 - Minimum Operations to Reduce X to Zero](leetcode/1776-minimum-operations-to-reduce-x-to-zero/Explanation.md): Reverses the problem to find the longest contiguous subarray that sums to the total array sum minus x.
- [3811 - Reverse Degree of a String](leetcode/3811-reverse-degree-of-a-string/Explanation.md): Calculates reverse degree by multiplying each character's reversed alphabet position with its string position.
- [3831 - Find X-Value of Array I](leetcode/3831-find-x-value-of-array-i/Explanation.md): Uses dynamic programming to count subarrays whose product leaves a specific remainder modulo $k$.
- [3840 - Find X-Value of Array II](leetcode/3840-find-x-value-of-array-ii/Explanation.md): Employs a Segment Tree to efficiently query products and counts after point updates in the array.
- [3869 - Smallest Index With Digit Sum Equal to Index](leetcode/3869-smallest-index-with-digit-sum-equal-to-index/Explanation.md): Iterates the array checking if the sum of digits of the value equals its index, returning the first match.
