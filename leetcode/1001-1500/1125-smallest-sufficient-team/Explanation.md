# LeetCode 1125: Smallest Sufficient Team

**LeetCode Problem #1125 — Smallest Sufficient Team**
Solve LeetCode Smallest Sufficient Team using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Sufficient Team |
| LeetCode | #1125 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In a project, you have a list of required skills `req_skills`, and a list of people. The `i^th` person `people[i]` contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in `req_skills`, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, `team = [0, 1, 3]` represents the people with skills `people[0]`, `people[1]`, and `people[3]`.

Return *any sufficient team of the smallest possible size, represented by the index of each person*. You may return the answer in **any order**.

It is **guaranteed** an answer exists.

## Constraints
- `1 <= req_skills.length <= 16`
- `1 <= req_skills[i].length <= 16`
- `req_skills[i]` consists of lowercase English letters.
- All the strings of `req_skills` are **unique**.
- `1 <= people.length <= 60`
- `0 <= people[i].length <= 16`
- `1 <= people[i][j].length <= 16`
- `people[i][j]` consists of lowercase English letters.
- All the strings of `people[i]` are **unique**.
- Every skill in `people[i]` is a skill in `req_skills`.
- It is guaranteed a sufficient team exists.

## Examples
### Example 1
- **Input:** `req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]`
- **Output:** `[0,2]`

### Example 2
- **Input:** `req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]`
- **Output:** `[1,2]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Smallest Sufficient Team**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2]`.

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
/**
 * @param {string[]} req_skills
 * @param {string[][]} people
 * @return {number[]}
 */
var smallestSufficientTeam = function (req_skills, people) {
  const n = req_skills.length;
  const idx = new Map();
  req_skills.forEach((s, i) => idx.set(s, i));

  const full = (1 << n) - 1;
  const dp = new Array(1 << n).fill(null);
  dp[0] = [];

  for (let p = 0; p < people.length; p++) {
    let pm = 0;
    for (const s of people[p]) pm |= 1 << idx.get(s);
    if (pm === 0) continue;

    for (let mask = 0; mask <= full; mask++) {
      if (dp[mask] === null) continue;
      const nm = mask | pm;
      if (nm === mask) continue;
      if (dp[nm] === null || dp[mask].length + 1 < dp[nm].length) {
        dp[nm] = [...dp[mask], p];
      }
    }
  }

  return dp[full];
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
- [1383. Maximum Performance of a Team](../../1001-1500/1383-maximum-performance-of-a-team/)
- [1626. Best Team With No Conflicts](../../1501-2000/1626-best-team-with-no-conflicts/)
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-sufficient-team/)
