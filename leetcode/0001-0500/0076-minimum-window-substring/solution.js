
var minWindow = function(s, t) {
    if (s.length < t.length) return "";

    const need = new Map();

    for (const char of t) {
        need.set(char, (need.get(char) || 0) + 1);
    }

    let left = 0;
    let required = t.length;
    let minLength = Infinity;
    let start = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        if (need.has(char)) {
            if (need.get(char) > 0) {
                required--;
            }

            need.set(char, need.get(char) - 1);
        }

        // When all required characters are included
        while (required === 0) {
            const windowLength = right - left + 1;

            if (windowLength < minLength) {
                minLength = windowLength;
                start = left;
            }

            const leftChar = s[left];

            if (need.has(leftChar)) {
                need.set(leftChar, need.get(leftChar) + 1);

                if (need.get(leftChar) > 0) {
                    required++;
                }
            }

            left++;
        }
    }

    return minLength === Infinity
        ? ""
        : s.substring(start, start + minLength);
};

