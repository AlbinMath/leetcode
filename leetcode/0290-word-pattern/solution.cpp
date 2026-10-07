class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word;

        // Split string into words
        stringstream ss(s);
        while (ss >> word) {
            words.push_back(word);
        }

        // Number of characters and words must match
        if (pattern.length() != words.size()) {
            return false;
        }

        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern[i];
            string w = words[i];

            // Character already mapped to a different word
            if (charToWord.count(c) && charToWord[c] != w) {
                return false;
            }

            // Word already mapped to a different character
            if (wordToChar.count(w) && wordToChar[w] != c) {
                return false;
            }

            charToWord[c] = w;
            wordToChar[w] = c;
        }

        return true;
    }
};
