
var minInteger = function(num, k) {
    const n = num.length;

    // Store the original positions of each digit
    const positions = Array.from({ length: 10 }, () => []);

    for (let i = 0; i < n; i++) {
        positions[Number(num[i])].push(i);
    }

    // Fenwick Tree: tracks digits already removed
    const bit = new Array(n + 1).fill(0);

    function update(index, delta) {
        index++; // Convert to 1-based indexing

        while (index <= n) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    function query(index) {
        // Count removed positions strictly before index
        let sum = 0;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    const used = new Array(10).fill(0);
    let result = "";

    for (let step = 0; step < n; step++) {
        let chosen = false;

        // Try digits from smallest to largest
        for (let digit = 0; digit <= 9; digit++) {
            if (used[digit] >= positions[digit].length) {
                continue;
            }

            const originalIndex = positions[digit][used[digit]];

            // Remaining swaps needed to move this digit forward
            const cost = originalIndex - query(originalIndex);

            if (cost <= k) {
                k -= cost;
                result += digit;
                used[digit]++;
                update(originalIndex, 1);
                chosen = true;
                break;
            }
        }

        if (!chosen) break;
    }

    return result;
};

