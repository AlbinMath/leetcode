# Brace Expansion II

## Problem Explanation
You are given a string `expression` that represents a set of words defined by a specific grammar:
- Single letters represent a set with one word: `R("a") = {"a"}`.
- Comma-separated expressions represent the union of sets: `R("{a,b}") = {"a", "b"}`.
- Concatenated expressions represent the Cartesian product of sets (combining each word in the first set with each word in the second set): `R("{a,b}{c,d}") = {"ac", "ad", "bc", "bd"}`.

Your task is to parse the expression, expand it to find all possible resulting words, and return them as a **sorted list** without duplicates.

## How the Code Works
The solution implements a **Recursive Descent Parser** with three main functions to process the expression string according to the grammar.
1. `parseExpression()`: This function handles unions (comma-separated terms). It calls `parseTerm()` to get the first set of words. Then, as long as it encounters commas `,`, it skips them, calls `parseTerm()` again, and adds all resulting words into a single Set (which automatically removes duplicates).
2. `parseTerm()`: This function handles concatenation (adjacent factors). It starts with a base Set containing an empty string `[""]`. As long as it doesn't hit a `}` or `,`, it calls `parseFactor()` to get the next set of words. It then takes the Cartesian product of the current `result` Set and the new `factor` Set (combining every prefix with every new suffix) and updates the `result`.
3. `parseFactor()`: This function handles the smallest building blocks.
   - If the current character is a letter, it simply returns a Set containing that single letter and advances the index.
   - If it encounters a `{`, it skips it, calls `parseExpression()` recursively to evaluate the entire expression inside the braces, and then skips the closing `}`.
4. The main function starts by calling `parseExpression()`, converts the resulting Set to an Array, sorts it lexicographically as required, and returns it.
