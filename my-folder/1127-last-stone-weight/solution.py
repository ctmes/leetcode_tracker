import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negative for max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)  # Largest
            stone2 = -heapq.heappop(heap)  # Second largest
            if stone1 != stone2:
                heapq.heappush(heap, -(stone1 - stone2))
                
        return -heap[0] if heap else 0
