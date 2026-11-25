var getDistances = function(arr) {
    const map = new Map();
    const result = new Array(arr.length).fill(0);
    for (let i = 0; i < arr.length; i++) {
        if (!map.has(arr[i])) {
            map.set(arr[i], []);
        }
        map.get(arr[i]).push(i);
    }
    for (const indices of map.values()) {
        const m = indices.length;
        let totalSum = indices.reduce((sum, x) => sum + x, 0);
        let prefixSum = 0;
        for (let j = 0; j < m; j++) {
            const index = indices[j];
            const leftCount = j;
            const rightCount = m - j - 1;
            const leftDistance =
                index * leftCount - prefixSum;
            const rightSum = totalSum - prefixSum - index;
            const rightDistance =
                rightSum - index * rightCount;
            result[index] = leftDistance + rightDistance;
            prefixSum += index;
        }
    }
    return result;
};
