class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        length = len(tickets)
        for i in range(length):
            if i <= k:
                count += min( tickets[k] , tickets[i])
            else:
                if  tickets[k] - 1 < tickets[i]:
                    count += tickets[k] - 1
                else:
                    count += tickets[i]
            
        return count
            