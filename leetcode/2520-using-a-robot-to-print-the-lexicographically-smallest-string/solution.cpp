#include <string>
using namespace std;

class Solution {
public:
    string robotWithString(string s) {
        int n = s.length();
        int freq[26] = {0};
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        string t;
        t.reserve(n);
        string res;
        res.reserve(n);
        
        int min_char = 0; // 0 represents 'a'
        
        for (char c : s) {
            t.push_back(c);
            freq[c - 'a']--;
            
            // Advance min_char to the smallest character still remaining in s
            while (min_char < 26 && freq[min_char] == 0) {
                min_char++;
            }
            
            // Pop from stack t while its top is <= smallest remaining character in s
            while (!t.empty() && (t.back() - 'a') <= min_char) {
                res.push_back(t.back());
                t.pop_back();
            }
        }
        
        return res;
    }
};
