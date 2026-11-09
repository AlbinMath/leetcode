
var decodeAtIndex = function(s, k) {
    let size = 0n;
    k = BigInt(k);

    // Calculate decoded string length
    for (const ch of s) {
        if (ch >= '2' && ch <= '9') {
            size *= BigInt(ch);
        } else {
            size++;
        }
    }

    // Traverse backward
    for (let i = s.length - 1; i >= 0; i--) {
        const ch = s[i];

        k %= size;

        // Find the required character
        if (k === 0n && ch >= 'a' && ch <= 'z') {
            return ch;
        }

        if (ch >= '2' && ch <= '9') {
            size /= BigInt(ch);
        } else {
            size--;
        }
    }

    return "";
};

