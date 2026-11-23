
var minDistinctFreqPair = function(nums) {
    const freq = new Array(101).fill(0);

    // Step 1: Count frequencies
    for (let num of nums) {
        freq[num]++;
    }

    // Step 2: Find the smallest number
    let x = -1;

    for (let i = 1; i <= 100; i++) {
        if (freq[i] > 0) {
            x = i;
            break;
        }
    }

    // Step 3: Find the smallest valid y
    for (let y = x + 1; y <= 100; y++) {
        if (freq[y] > 0 && freq[y] !== freq[x]) {
            return [x, y];
        }
    }

    return [-1, -1];
};

