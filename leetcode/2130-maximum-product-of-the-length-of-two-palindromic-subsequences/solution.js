
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const n = s.length;
    const totalMasks = 1 << n;
    const palindromeLength = new Array(totalMasks).fill(0);

    // Calculate the length of each palindromic subsequence.
    for (let mask = 1; mask < totalMasks; mask++) {
        let left = 0;
        let right = n - 1;
        let length = 0;
        let isPalindrome = true;

        while (left <= right) {
            while (left < n && !(mask & (1 << left))) {
                left++;
            }

            while (right >= 0 && !(mask & (1 << right))) {
                right--;
            }

            if (left > right) break;

            if (s[left] !== s[right]) {
                isPalindrome = false;
                break;
            }

            if (left === right) {
                length++;
            } else {
                length += 2;
            }

            left++;
            right--;
        }

        if (isPalindrome) {
            palindromeLength[mask] = length;
        }
    }

    let answer = 0;

    // Try every pair of disjoint subsequences.
    for (let mask1 = 1; mask1 < totalMasks; mask1++) {
        if (palindromeLength[mask1] === 0) continue;

        for (let mask2 = mask1 + 1; mask2 < totalMasks; mask2++) {
            // The masks must not share any selected index.
            if ((mask1 & mask2) !== 0) continue;
            if (palindromeLength[mask2] === 0) continue;

            answer = Math.max(
                answer,
                palindromeLength[mask1] * palindromeLength[mask2]
            );
        }
    }

    return answer;
};

