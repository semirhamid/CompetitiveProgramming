class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        k = len(p) - 1
        st2 = dict(Counter(p))
        p = i + k
        st1= dict(Counter(s[i:p+1]))
        stack = []
        p += 1

        while p <len(s):
            if st1==st2:
                stack.append(i)
            if st1[s[i]] == 1:
                del st1[s[i]]
            elif st1[s[i]] > 1:
                st1[s[i]] -= 1

            if s[p ] in st1:
                st1[s[p]] += 1
            else:
                st1[s[p ]] = 1
            i += 1
            p += 1
        if st1 == st2:
            stack.append(i)
        return stack