# 0014 - Longest Common Prefix

## Approach
We assume the first string `strs[0]` is the longest common prefix.
Then, we iterate through the rest of the strings.
For each string, we check if it starts with the current `prefix`.
If it doesn't, we shorten the `prefix` by removing the last character (`prefix[:-1]`) until the string starts with the prefix.
If at any point the `prefix` becomes empty, it means there is no common prefix among the strings, and we can immediately return `""`.
If the loop finishes, we return the remaining `prefix`.

## Complexity
- **Time Complexity:** $O(S)$ where $S$ is the sum of all characters in all strings. In the worst case, all strings are identical.
- **Space Complexity:** $O(1)$ as we only modify the prefix string in place and use constant extra space.
