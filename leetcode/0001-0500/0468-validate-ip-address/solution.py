class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def valid_v4(ip: str) -> bool:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p or not p.isdigit() or len(p) > 3:
                    return False
                if len(p) > 1 and p[0] == '0':
                    return False
                if int(p) > 255:
                    return False
            return True

        def valid_v6(ip: str) -> bool:
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_chars = set("0123456789abcdefABCDEF")
            for p in parts:
                if not 1 <= len(p) <= 4:
                    return False
                if any(ch not in hex_chars for ch in p):
                    return False
            return True

        if '.' in queryIP and valid_v4(queryIP):
            return "IPv4"
        if ':' in queryIP and valid_v6(queryIP):
            return "IPv6"
        return "Neither"
