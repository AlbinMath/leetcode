var minTimeToType = function(word) {
    let time = 0;
    let current = 0; // 'a' = 0

    for (const char of word) {
        let target = char.charCodeAt(0) - 'a'.charCodeAt(0);

        let distance = Math.abs(target - current);

        time += Math.min(distance, 26 - distance) + 1;

        current = target;
    }

    return time;
};
