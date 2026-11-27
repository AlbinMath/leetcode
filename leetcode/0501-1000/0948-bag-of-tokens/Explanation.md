# LeetCode 948: Bag of Tokens

**LeetCode Problem #948 — Bag of Tokens**
Solve LeetCode Bag of Tokens using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bag of Tokens |
| LeetCode | #948 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You start with an initial **power** of `power`, an initial **score** of `0`, and a bag of tokens given as an integer array `tokens`, where each `tokens[i]` denotes the value of token*_i*.

Your goal is to **maximize** the total **score** by strategically playing these tokens. In one move, you can play an **unplayed** token in one of the two ways (but not both for the same token):

**Face-up**: If your current power is **at least** `tokens[i]`, you may play token*_i*, losing `tokens[i]` power and gaining `1` score. 
 **Face-down**: If your current score is **at least** `1`, you may play token*_i*, gaining `tokens[i]` power and losing `1` score.

Return *the **maximum** possible score you can achieve after playing **any** number of tokens*.

## Constraints
- `0 <= tokens.length <= 1000`
- `0 <= tokens[i], power < 10^4`

## Examples
### Example 1
- **Input:** `tokens = [100], power = 50`
- **Output:** `0`

### Example 2
- **Input:** `tokens = [200,100], power = 150`
- **Output:** `1`
- **Explanation:** Play token*_1* (`100`) face-up, reducing your power to `50` and increasing your score to `1`. 

 There is no need to play token*_0*, since you cannot play it face-up to add to your score. The maximum score achievable is `1`.

### Example 3
- **Input:** `tokens = [100,200,300,400], power = 200`
- **Output:** `2`
- **Explanation:** Play the tokens in this order to get a score of `2`: 

 
 Play token*_0* (`100`) face-up, reducing power to `100` and increasing score to `1`. 
 Play token*_3* (`400`) face-down, increasing power to `500` and reducing score to `0`. 
 Play token*_1* (`200`) face-up, reducing power to `300` and increasing score to `1`. 
 Play token*_2* (`300`) face-up, reducing power to `0` and increasing score to `2`. 
 

 The maximum score achievable is 2 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Bag of Tokens**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tokens = [100], power = 50`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var bagOfTokensScore = function(tokens, power) {
    tokens.sort((a, b) => a - b);

    let left = 0;
    let right = tokens.length - 1;

    let score = 0;
    let maxScore = 0;

    while (left <= right) {

        if (power >= tokens[left]) {
            power -= tokens[left];
            score++;
            left++;

            maxScore = Math.max(maxScore, score);
        }

        else if (score > 0 && left < right) {
            power += tokens[right];
            score--;
            right--;
        }

        else {
            break;
        }
    }

    return maxScore;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1760. Minimum Limit of Balls in a Bag](../../1501-2000/1760-minimum-limit-of-balls-in-a-bag/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bag-of-tokens/)
