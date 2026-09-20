# 0013 - Roman to Integer

## Approach
We define a dictionary `values` that maps each Roman numeral character to its corresponding integer value.
We initialize a `total` variable to `0`.
We iterate through the string `s`. For each character at index `i`:
- If there is a next character (`i + 1 < len(s)`) and its value is strictly greater than the current character's value, it represents a subtractive combination (like `IV` or `IX`). We subtract the current character's value from `total`.
- Otherwise, we add the current character's value to `total`.

## Complexity
- **Time Complexity:** $O(N)$ where $N$ is the length of the string, since we iterate through it once.
- **Space Complexity:** $O(1)$ because the dictionary of values has a fixed size (7 symbols).
