
var countPairs = function(words) {
    const map = new Map();
    let ans = 0;

    for (let word of words) {
        let key = "";
        const first = word.charCodeAt(0);

        // Normalize each character
        for (let ch of word) {
            let diff = (ch.charCodeAt(0) - first + 26) % 26;
            key += diff + ",";
        }

        // Count previous similar strings
        ans += map.get(key) || 0;

        // Update frequency
        map.set(key, (map.get(key) || 0) + 1);
    }

    return ans;
};

