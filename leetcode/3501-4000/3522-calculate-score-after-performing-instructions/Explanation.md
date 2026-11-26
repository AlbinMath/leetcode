# LeetCode 3522: Calculate Score After Performing Instructions

**LeetCode Problem #3522 — Calculate Score After Performing Instructions**
Solve LeetCode Calculate Score After Performing Instructions using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculate Score After Performing Instructions |
| LeetCode | #3522 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two arrays, `instructions` and `values`, both of size `n`.

You need to simulate a process based on the following rules:

You start at the first instruction at index `i = 0` with an initial score of 0. 
 If `instructions[i]` is `"add"`:
 
 Add `values[i]` to your score. 
 Move to the next instruction `(i + 1)`. 
 
 
 If `instructions[i]` is `"jump"`:
 
 Move to the instruction at index `(i + values[i])` without modifying your score.

The process ends when you either:

Go out of bounds (i.e., `i < 0 or i >= n`), or 
 Attempt to revisit an instruction that has been previously executed. The revisited instruction is not executed.

Return your score at the end of the process.

## Constraints
- `n == instructions.length == values.length`
- `1 <= n <= 10^5`
- `instructions[i]` is either `"add"` or `"jump"`.
- `-10^5 <= values[i] <= 10^5`

## Examples
### Example 1
- **Input:** `instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]`
- **Output:** `1`
- **Explanation:** Simulate the process starting at instruction 0: 

 
 At index 0: Instruction is `"jump"`, move to index `0 + 2 = 2`. 
 At index 2: Instruction is `"add"`, add `values[2] = 3` to your score and move to index 3. Your score becomes 3. 
 At index 3: Instruction is `"jump"`, move to index `3 + 1 = 4`. 
 At index 4: Instruction is `"add"`, add `values[4] = -2` to your score and move to index 5. Your score becomes 1. 
 At index 5: Instruction is `"jump"`, move to index `5 + (-3) = 2`. 
 At index 2: Already visited. The process ends.

### Example 2
- **Input:** `instructions = ["jump","add","add"], values = [3,1,1]`
- **Output:** `0`
- **Explanation:** Simulate the process starting at instruction 0: 

 
 At index 0: Instruction is `"jump"`, move to index `0 + 3 = 3`. 
 At index 3: Out of bounds. The process ends.

### Example 3
- **Input:** `instructions = ["jump"], values = [0]`
- **Output:** `0`
- **Explanation:** Simulate the process starting at instruction 0: 

 
 At index 0: Instruction is `"jump"`, move to index `0 + 0 = 0`. 
 At index 0: Already visited. The process ends.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Calculate Score After Performing Instructions**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Simulate the process starting at instruction 0: 

 
 At index 0: Instruction is `"jump"`, move to index `0 + 2 = 2`. 
 At index 2: Instruction is `"add"`, add `values[2] = 3` to your score and move to index 3. Your score becomes 3. 
 At index 3: Instruction is `"jump"`, move to index `3 + 1 = 4`. 
 At index 4: Instruction is `"add"`, add `values[4] = -2` to your score and move to index 5. Your score becomes 1. 
 At index 5: Instruction is `"jump"`, move to index `5 + (-3) = 2`. 
 At index 2: Already visited. The process ends.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var calculateScore = function(instructions, values) {
    const n = instructions.length;
    const visited = new Uint8Array(n);
    let score = 0;
    let i = 0;

    while (i >= 0 && i < n && !visited[i]) {
        visited[i] = 1;
        if (instructions[i] === "add") {
            score += values[i];
            i++;
        } else {
            i += values[i];
        }
    }

    return score;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2011. Final Value of Variable After Performing Operations](../../2001-2500/2011-final-value-of-variable-after-performing-operations/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3001-3500/3346-maximum-frequency-of-an-element-after-performing-operations-i/)
- [3347. Maximum Frequency of an Element After Performing Operations II](../../3001-3500/3347-maximum-frequency-of-an-element-after-performing-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculate-score-after-performing-instructions/)
