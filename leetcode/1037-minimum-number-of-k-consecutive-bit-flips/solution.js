/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minKBitFlips = function (nums, k) {
    const n = nums.length;
    const ends = new Uint8Array(n + 1); // ends[i] = 1 if a flip expires at i
    let flipped = 0;
    let count = 0;

    for (let i = 0; i < n; i++) {
        if (ends[i]) flipped ^= 1;           // a flip stops covering index i
        if ((nums[i] ^ flipped) === 0) {     // current effective bit is 0
            if (i + k > n) return -1;        // not enough room for a flip
            flipped ^= 1;
            ends[i + k] = 1;
            count++;
        }
    }
    return count;
};
