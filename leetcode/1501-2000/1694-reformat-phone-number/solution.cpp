
class Solution {
public:
    string reformatNumber(string number) {
        string digits = "";

        // Remove spaces and dashes
        for (char c : number) {
            if (isdigit(c)) {
                digits += c;
            }
        }

        string result = "";
        int i = 0;
        int n = digits.size();

        // Create blocks of 3 while more than 4 digits remain
        while (n - i > 4) {
            result += digits.substr(i, 3) + "-";
            i += 3;
        }

        // Handle the remaining digits
        int remaining = n - i;

        if (remaining == 4) {
            result += digits.substr(i, 2) + "-" + digits.substr(i + 2, 2);
        } else {
            result += digits.substr(i, remaining);
        }

        return result;
    }
};

