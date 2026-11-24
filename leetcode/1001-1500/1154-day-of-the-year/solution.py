from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        current_date = datetime.strptime(date, "%Y-%m-%d")
        start_date = datetime(current_date.year, 1, 1)

        return (current_date - start_date).days + 1
