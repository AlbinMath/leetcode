
var findDiagonalOrder = function(nums) {
    const map = new Map();
    let maxKey = 0;

    // Group elements by diagonal
    for (let r = 0; r < nums.length; r++) {
        for (let c = 0; c < nums[r].length; c++) {
            const key = r + c;

            if (!map.has(key)) {
                map.set(key, []);
            }

            map.get(key).push(nums[r][c]);
            maxKey = Math.max(maxKey, key);
        }
    }

    const result = [];

    for (let key = 0; key <= maxKey; key++) {
        const diagonal = map.get(key);

        for (let i = diagonal.length - 1; i >= 0; i--) {
            result.push(diagonal[i]);
        }
    }

    return result;
};

