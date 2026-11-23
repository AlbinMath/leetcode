
class Solution {
public:
    int getValue(string word) {
        int value = 0;

        for (char c : word) {
            value = value * 10 + (c - 'a');
        }

        return value;
    }

    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        int first = getValue(firstWord);
        int second = getValue(secondWord);
        int target = getValue(targetWord);

        return first + second == target;
    }
};

