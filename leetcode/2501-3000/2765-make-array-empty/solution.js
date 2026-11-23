
var countOperationsToEmptyArray = function(nums) {
    const n = nums.length;

    // Sort values by their original indices
    const sorted = nums
        .map((value, index) => [value, index])
        .sort((a, b) => a[0] - b[0]);

    // Fenwick Tree: 1 means the element is still present
    const bit = new Array(n + 1).fill(0);

    function update(index, delta) {
        index++;

        while (index <= n) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    function query(index) {
        let sum = 0;
        index++;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    // Initially, every element is present
    for (let i = 0; i < n; i++) {
        update(i, 1);
    }

    let operations = 0;
    let previousIndex = 0;

    for (const [, index] of sorted) {
        if (index >= previousIndex) {
            // Count remaining elements from previousIndex to index
            operations += query(index) -
                (previousIndex > 0 ? query(previousIndex - 1) : 0);
        } else {
            // Wrap around the end of the array
            operations +=
                query(n - 1) -
                (previousIndex > 0 ? query(previousIndex - 1) : 0) +
                query(index);
        }

        // Remove the current smallest element
        update(index, -1);
        previousIndex = index;
    }

    return operations;
};

