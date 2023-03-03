class Solution:
    def balancedString(self, s: str) -> int:
        word = Counter(s)
        avg = len(s) // 4
        unsatisfied = {}
        count = 0
        for i in word:
            if word[i] > avg:
                unsatisfied[i] = word[i] - avg
                count += 1
        left = 0
        right = 0
        length = len(s)
        mn = float(inf)
        while right < length and unsatisfied:
            if s[right] in unsatisfied:
                unsatisfied[s[right]] -= 1
                if unsatisfied[s[right]] == 0:
                    count -= 1
            while left < length and right < length and count == 0:
                mn = min(mn, right - left + 1)
                if s[left] in unsatisfied:
                    unsatisfied[s[left]] += 1
                    if unsatisfied[s[left]] == 1:
                        count += 1
                left += 1
            right += 1
                    
        return mn if mn != float(inf) else 0
    