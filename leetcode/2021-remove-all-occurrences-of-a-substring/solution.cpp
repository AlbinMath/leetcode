#include <string>
using namespace std;

class Solution {
public:
    string removeOccurrences(string s, string part) {
        string res;
        res.reserve(s.size());
        int m = part.size();
        char last_char = part.back();
        
        for (char c : s) {
            res.push_back(c);
            // Quick check on the last character before comparing the full suffix
            if (c == last_char && (int)res.size() >= m) {
                if (res.compare(res.size() - m, m, part) == 0) {
                    res.resize(res.size() - m);
                }
            }
        }
        
        return res;
    }
};
