
class Solution {
public:
    string reorderSpaces(string text) {
        int spaces = 0;
        vector<string> words;
        string word;

        // Count spaces and extract words
        for (char c : text) {
            if (c == ' ') {
                spaces++;
            } else {
                word += c;
            }

            if (c == ' ' && !word.empty()) {
                words.push_back(word);
                word.clear();
            }
        }

        // Add the last word, if any
        if (!word.empty()) {
            words.push_back(word);
        }

        int n = words.size();
        int between = 0;
        int extra = spaces;

        if (n > 1) {
            between = spaces / (n - 1);
            extra = spaces % (n - 1);
        }

        string result;

        for (int i = 0; i < n; i++) {
            result += words[i];

            if (i < n - 1) {
                result += string(between, ' ');
            }
        }

        result += string(extra, ' ');

        return result;
    }
};

