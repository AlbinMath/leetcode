class Solution:
    def getImportance(self, employees, id):
        emp = {e.id: e for e in employees}

        def dfs(i):
            e = emp[i]
            return e.importance + sum(dfs(s) for s in e.subordinates)

        return dfs(id)
