class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {}
        for name, col_count in zip(names, columns):
            self.tables[name] = {
                "cols": col_count,
                "next_id": 1,
                "rows": {}
            }

    def ins(self, name: str, row: list[str]) -> bool:
        table = self.tables.get(name)
        if not table or len(row) != table["cols"]:
            return False
            
        row_id = table["next_id"]
        table["next_id"] += 1
        table["rows"][row_id] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        table = self.tables.get(name)
        if table:
            table["rows"].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables.get(name)
        if not table or rowId not in table["rows"] or not (1 <= columnId <= table["cols"]):
            return "<null>"
            
        return table["rows"][rowId][columnId - 1]

    def exp(self, name: str) -> list[str]:
        table = self.tables.get(name)
        if not table:
            return []
            
        return [f"{row_id},{','.join(row)}" for row_id, row in table["rows"].items()]
