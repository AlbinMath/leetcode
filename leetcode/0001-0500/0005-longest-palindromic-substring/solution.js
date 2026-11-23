
var longestPalindrome = function(s) {
    let start = 0;
    let maxLength = 0;

    function expandAroundCenter(left, right) {
        while (
            left >= 0 &&
            right < s.length &&
            s[left] === s[right]
        ) {
            left--;
            right++;
        }

        // The pointers have moved one step beyond the palindrome.
        const length = right - left - 1;

        if (length > maxLength) {
            maxLength = length;
            start = left + 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        // Odd-length palindrome
        expandAroundCenter(i, i);

        // Even-length palindrome
        expandAroundCenter(i, i + 1);
    }

    return s.substring(start, start + maxLength);
};

