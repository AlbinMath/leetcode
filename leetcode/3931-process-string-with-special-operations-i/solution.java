class Solution {
    public String processStr(String s) {
        StringBuilder result = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                // Append character
                result.append(c);

            } else if (c == '*') {
                // Remove last character if it exists
                if (result.length() > 0) {
                    result.deleteCharAt(result.length() - 1);
                }

            } else if (c == '#') {
                // Duplicate current result
                result.append(result);

            } else if (c == '%') {
                // Reverse current result
                result.reverse();
            }
        }

        return result.toString();
    }
}
