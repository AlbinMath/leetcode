
class Solution {
public:
    bool checkZeroOnes(string s) {
        int maxOnes = 0, maxZeros = 0;
        int currentOnes = 0, currentZeros = 0;

        for (char c : s) {
            if (c == '1') {
                currentOnes++;
                currentZeros = 0;
                maxOnes = max(maxOnes, currentOnes);
            } else {
                currentZeros++;
                currentOnes = 0;
                maxZeros = max(maxZeros, currentZeros);
            }
        }

        return maxOnes > maxZeros;
    }
};

