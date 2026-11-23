/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let write = 0;
    let read = 0;

    while (read < chars.length) {
        let char = chars[read];
        let count = 0;

        // Count consecutive occurrences
        while (read < chars.length && chars[read] === char) {
            read++;
            count++;
        }

        // Write the character
        chars[write++] = char;

        // Write the count if greater than 1
        if (count > 1) {
            for (const digit of String(count)) {
                chars[write++] = digit;
            }
        }
    }

    return write;
};
