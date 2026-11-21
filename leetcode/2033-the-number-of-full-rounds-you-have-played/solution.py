class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def to_min(t: str) -> int:
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        login = to_min(loginTime)
        logout = to_min(logoutTime)
        if logout < login:
            logout += 1440

        start = (login + 14) // 15   # ceil(login / 15)
        end = logout // 15           # floor(logout / 15)

        return max(0, end - start)
