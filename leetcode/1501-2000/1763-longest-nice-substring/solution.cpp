
class Solution {
public:
    bool isNice(string s) {
        for (char c : s) {
            if (islower(c) && s.find(toupper(c)) == string::npos) {
                return false;
            }

            if (isupper(c) && s.find(tolower(c)) == string::npos) {
                return false;
            }
        }

        return true;
    }

    string longestNiceSubstring(string s) {
        string result = "";

        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j <= s.size(); j++) {
                string sub = s.substr(i, j - i);

                if (sub.size() > result.size() && isNice(sub)) {
                    result = sub;
                }
            }
        }

        return result;
    }
};

