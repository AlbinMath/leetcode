type MultiDimensionalArray = (number | MultiDimensionalArray)[];

function* inorderTraversal(
    arr: MultiDimensionalArray
): Generator<number> {

    for (const item of arr) {
        if (Array.isArray(item)) {
            yield* inorderTraversal(item);
        } else {
            yield item;
        }
    }
}
