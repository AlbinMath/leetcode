# LeetCode 2115: Find All Possible Recipes from Given Supplies

**LeetCode Problem #2115 — Find All Possible Recipes from Given Supplies**
Solve LeetCode Find All Possible Recipes from Given Supplies using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Possible Recipes from Given Supplies |
| LeetCode | #2115 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The `i^th` recipe has the name `recipes[i]`, and you can **create** it if you have **all** the needed ingredients from `ingredients[i]`. A recipe can also be an ingredient for **other **recipes, i.e., `ingredients[i]` may contain a string that is in `recipes`.

You are also given a string array `supplies` containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return *a list of all the recipes that you can create. *You may return the answer in **any order**.

Note that two recipes may contain each other in their ingredients.

## Constraints
- `n == recipes.length == ingredients.length`
- `1 <= n <= 100`
- `1 <= ingredients[i].length, supplies.length <= 100`
- `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
- `recipes[i], ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
- All the values of `recipes` and `supplies` combined are unique.
- Each `ingredients[i]` does not contain any duplicate values.

## Examples
### Example 1
- **Input:** `recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]`
- **Output:** `["bread"]`
- **Explanation:** We can create "bread" since we have the ingredients "yeast" and "flour".

### Example 2
- **Input:** `recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]`
- **Output:** `["bread","sandwich"]`
- **Explanation:** We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

### Example 3
- **Input:** `recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]`
- **Output:** `["bread","sandwich","burger"]`
- **Explanation:** We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find All Possible Recipes from Given Supplies**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["bread"]`.
4. **Verification:** We can create "bread" since we have the ingredients "yeast" and "flour".

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
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
    const n = recipes.length;
    const users = new Map(); // ingredient -> indices of recipes needing it
    const indeg = new Array(n);

    for (let i = 0; i < n; i++) {
        indeg[i] = ingredients[i].length;
        for (const ing of ingredients[i]) {
            if (!users.has(ing)) users.set(ing, []);
            users.get(ing).push(i);
        }
    }

    const queue = [...supplies];
    const res = [];
    let head = 0;
    while (head < queue.length) {
        const x = queue[head++];
        const list = users.get(x);
        if (!list) continue;
        for (const r of list) {
            if (--indeg[r] === 0) {
                res.push(recipes[r]);
                queue.push(recipes[r]);
            }
        }
    }
    return res;
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
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [797. All Paths From Source to Target](../../0501-1000/0813-all-paths-from-source-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)
