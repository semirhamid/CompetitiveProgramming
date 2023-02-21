class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        count = 0
        abebe = {}
        for i in range(len(garbage)):
            count += len(garbage[i])
            if "P" in garbage[i]: abebe["P"] = i
            if "G" in garbage[i]: abebe["G"] = i
            if "M" in garbage[i]: abebe["M"] = i
        prefix = 0
        for i in range(len(travel)):
            prefix += travel[i]
            travel[i] = prefix
        for key in abebe.keys():
            count += travel[abebe[key] - 1] if abebe[key] != 0 else 0
        return count