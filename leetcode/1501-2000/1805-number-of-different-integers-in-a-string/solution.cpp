
class Solution {
public:
    int numDifferentIntegers(string word) {
        unordered_set<string> uniqueNumbers;
        int i = 0;
        int n = word.size();

        while (i < n) {
            if (isdigit(word[i])) {
                string number = "";

                while (i < n && isdigit(word[i])) {
                    number += word[i];
                    i++;
                }

                // Remove leading zeros
                int j = 0;
                while (j < number.size() && number[j] == '0') {
                    j++;
                }

                number = number.substr(j);

                // Handle numbers containing only zeros
                if (number.empty()) {
                    number = "0";
                }

                uniqueNumbers.insert(number);
            } else {
                i++;
            }
        }

        return uniqueNumbers.size();
    }
};

