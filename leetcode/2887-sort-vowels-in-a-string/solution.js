
var sortVowels = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u',
                            'A', 'E', 'I', 'O', 'U']);

    const arr = s.split('');
    const vowelList = [];

    for (const ch of arr) {
        if (vowels.has(ch)) {
            vowelList.push(ch);
        }
    }

    vowelList.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));

    let index = 0;

    for (let i = 0; i < arr.length; i++) {
        if (vowels.has(arr[i])) {
            arr[i] = vowelList[index++];
        }
    }

    return arr.join('');
};

