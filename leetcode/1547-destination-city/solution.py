class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starting_cities = {path[0] for path in paths}

        for start, destination in paths:
            if destination not in starting_cities:
                return destination
