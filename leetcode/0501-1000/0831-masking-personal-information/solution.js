var maskPII = function(s) {
    if (s.includes("@")) {
        // Email address
        s = s.toLowerCase();
        let at = s.indexOf("@");

        return s[0] + "*****" + s.slice(at - 1);
    } else {
        // Phone number
        let digits = s.replace(/\D/g, "");
        let local = digits.slice(-4);
        let countryCodeLength = digits.length - 10;

        let result = "***-***-" + local;

        if (countryCodeLength > 0) {
            result = "+" + "*".repeat(countryCodeLength) +
                     "-" + result;
        }

        return result;
    }
};
