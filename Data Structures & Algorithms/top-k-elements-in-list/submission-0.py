class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        counter = Counter(nums).most_common()

        heap = []
        for num, freq in counter :
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]

        