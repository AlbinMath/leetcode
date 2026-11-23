
var restoreIpAddresses = function(s) {
    const result = [];

    function backtrack(start, parts) {
        // A valid IP must have exactly four parts
        if (parts.length === 4) {
            if (start === s.length) {
                result.push(parts.join("."));
            }
            return;
        }

        // Try segments of length 1, 2, and 3
        for (let len = 1; len <= 3; len++) {
            if (start + len > s.length) break;

            const segment = s.substring(start, start + len);

            // Reject leading zeros
            if (segment.length > 1 && segment[0] === "0") {
                continue;
            }

            const value = Number(segment);

            // Each segment must be between 0 and 255
            if (value > 255) continue;

            parts.push(segment);
            backtrack(start + len, parts);
            parts.pop();
        }
    }

    backtrack(0, []);
    return result;
};

