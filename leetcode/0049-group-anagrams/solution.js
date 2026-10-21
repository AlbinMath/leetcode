
var groupAnagrams = function(strs) {
    const map = new Map();

    for (const str of strs) {
        // Sort letters to create a common key
        const key = str.split('').sort().join('');

        if (!map.has(key)) {
            map.set(key, []);
        }

        map.get(key).push(str);
    }

    return Array.from(map.values());
};

