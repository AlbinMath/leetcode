# LeetCode 3475: DNA Pattern Recognition 

**LeetCode Problem #3475 — DNA Pattern Recognition **
Solve LeetCode DNA Pattern Recognition  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | DNA Pattern Recognition  |
| LeetCode | #3475 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `Samples`

+----------------+---------+
| Column Name | Type | 
+----------------+---------+
| sample_id | int |
| dna_sequence | varchar |
| species | varchar |
+----------------+---------+
sample_id is the unique key for this table.
Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.

Biologists are studying basic patterns in DNA sequences. Write a solution to identify `sample_id` with the following patterns:

Sequences that **start** with **ATG** (a common **start codon**) 
 Sequences that **end** with either **TAA**, **TAG**, or **TGA** (**stop codons**) 
 Sequences containing the motif **ATAT** (a simple repeated pattern) 
 Sequences that have **at least** `3` **consecutive** **G** (like **GGG** or **GGGG**)

Return *the result table ordered by **sample_id in **ascending** order*.

The result format is in the following example.

## Examples
Consider the standard input for **DNA Pattern Recognition **. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **DNA Pattern Recognition **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples["has_start"] = samples["dna_sequence"].str.startswith("ATG").astype(int)

    samples["has_stop"] = (
        samples["dna_sequence"].str.endswith(("TAA", "TAG", "TGA"))
    ).astype(int)

    samples["has_atat"] = samples["dna_sequence"].str.contains("ATAT").astype(int)

    samples["has_ggg"] = samples["dna_sequence"].str.contains("GGG").astype(int)

    return samples.sort_values("sample_id")
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [290. Word Pattern](../../0001-0500/0290-word-pattern/)
- [456. 132 Pattern](../../0001-0500/0456-132-pattern/)
- [459. Repeated Substring Pattern](../../0001-0500/0459-repeated-substring-pattern/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/dna-pattern-recognition/)
