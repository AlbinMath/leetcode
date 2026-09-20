# 0001 - Two Sum

## Approach
We use a hash map (dictionary in Python) to keep track of the numbers we've seen so far and their indices.
For each number `num` in the array `nums`, we calculate its `complement` (i.e., `target - num`).
If the `complement` is already in our hash map, it means we have found the two numbers that add up to the target, and we return their indices.
If not, we add the current `num` and its index to the hash map and continue.

## Complexity
- **Time Complexity:** $O(N)$ because we iterate through the array once and hash map lookups take $O(1)$ time on average.
- **Space Complexity:** $O(N)$ because we might need to store up to $N$ elements in the hash map.
