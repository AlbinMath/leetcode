
var createSortedArray = function(instructions) {
    const MOD = 1000000007;
    const maxVal = 100000;
    const bit = new Array(maxVal + 1).fill(0);

    // Add one occurrence of value to the Fenwick Tree
    function update(index) {
        while (index <= maxVal) {
            bit[index]++;
            index += index & -index;
        }
    }

    // Count inserted elements with values <= index
    function query(index) {
        let sum = 0;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    let cost = 0;

    for (let i = 0; i < instructions.length; i++) {
        const x = instructions[i];

        // Number of elements strictly smaller than x
        const smaller = query(x - 1);

        // Number of elements strictly greater than x
        const greater = i - query(x);

        cost = (cost + Math.min(smaller, greater)) % MOD;

        // Insert x into the frequency structure
        update(x);
    }

    return cost;
};

