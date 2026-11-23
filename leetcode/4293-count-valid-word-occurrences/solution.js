
var countWordOccurrences = function(chunks, queries) {
    const s = chunks.join('');

    const words = s.match(/[a-z]+(?:-[a-z]+)*/g) || [];

    const freq = new Map();

    for (const word of words) {
        freq.set(word, (freq.get(word) || 0) + 1);
    }

    return queries.map(query => freq.get(query) || 0);
};

