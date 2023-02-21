class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k
        while k < len(self.minHeap):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)