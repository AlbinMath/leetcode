type MultiDimensionalArray = (number | MultiDimensionalArray)[];

function flat(
    arr: MultiDimensionalArray,
    n: number
): MultiDimensionalArray {
    const result: MultiDimensionalArray = [];

    function flatten(
        current: MultiDimensionalArray,
        depth: number
    ): void {
        for (const item of current) {
            if (Array.isArray(item) && depth < n) {
                flatten(item, depth + 1);
            } else {
                result.push(item);
            }
        }
    }

    flatten(arr, 0);

    return result;
}

