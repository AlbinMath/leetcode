# Join Two Arrays By Id

## Problem Explanation
Merge two arrays of objects by their `id` field. If both arrays have an object with the same id, merge their properties (arr2 overrides arr1). Return sorted by id.

## How the Code Works
Uses a Map keyed by id. First insert all objects from arr1, then merge/override with objects from arr2 using `Object.assign` or spread. Sort the result by id.
