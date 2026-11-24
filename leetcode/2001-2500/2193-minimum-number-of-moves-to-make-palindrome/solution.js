
var minMovesToMakePalindrome = function(s) {
    const chars = s.split("");
    let left = 0;
    let right = chars.length - 1;
    let moves = 0;

    while (left < right) {
        let k = right;

        // Find a matching character for chars[left]
        while (k > left && chars[k] !== chars[left]) {
            k--;
        }

        if (k === left) {
            // No match found: this character belongs in the middle
            [chars[left], chars[left + 1]] =
                [chars[left + 1], chars[left]];

            moves++;
        } else {
            // Move the matching character to the right end
            while (k < right) {
                [chars[k], chars[k + 1]] =
                    [chars[k + 1], chars[k]];

                k++;
                moves++;
            }

            left++;
            right--;
        }
    }

    return moves;
};

