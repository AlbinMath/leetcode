
class Solution {
public:
    string sortSentence(string s) {
        vector<string> words(10);
        stringstream ss(s);
        string word;

        while (ss >> word) {
            int position = word.back() - '0';
            word.pop_back();

            words[position] = word;
        }

        string result = "";

        for (int i = 1; i <= 9; i++) {
            if (!words[i].empty()) {
                if (!result.empty()) {
                    result += " ";
                }

                result += words[i];
            }
        }

        return result;
    }
};

