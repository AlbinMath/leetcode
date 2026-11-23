
var minCost = function(nums1, nums2) {
    const MAX = 80000;
    const count1 = new Array(MAX + 1).fill(0);
    const count2 = new Array(MAX + 1).fill(0);

    // Count frequencies in both arrays
    for (let x of nums1) {
        count1[x]++;
    }

    for (let x of nums2) {
        count2[x]++;
    }

    let answer = 0;

    for (let x = 1; x <= MAX; x++) {
        const total = count1[x] + count2[x];

        // Every number must have an even total frequency
        if (total % 2 !== 0) {
            return -1;
        }

        // Count excess elements in nums1
        const target = total / 2;

        if (count1[x] > target) {
            answer += count1[x] - target;
        }
    }

    return answer;
};

