class Solution:
    def similarPairs(self, words: List[str]) -> int:
        arr = []
        count = 0
        for i in range(len(words)):
            arr.append("".join(sorted(set(words[i]))))
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1
        return count