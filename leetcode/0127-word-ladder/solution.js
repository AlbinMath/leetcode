
var ladderLength = function(beginWord, endWord, wordList) {
    const words = new Set(wordList);

    if (!words.has(endWord)) return 0;

    const queue = [[beginWord, 1]];
    let front = 0;

    while (front < queue.length) {
        const [word, length] = queue[front++];

        if (word === endWord) {
            return length;
        }

        for (let i = 0; i < word.length; i++) {
            for (let c = 97; c <= 122; c++) {
                const char = String.fromCharCode(c);

                if (char === word[i]) continue;

                const nextWord =
                    word.slice(0, i) +
                    char +
                    word.slice(i + 1);

                if (words.has(nextWord)) {
                    words.delete(nextWord);
                    queue.push([nextWord, length + 1]);
                }
            }
        }
    }

    return 0;
};

