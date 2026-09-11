class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        ans = []
        heap = []
        # each time we shift the window, append heap[0] to ans
        for i in range(left, k):
            heapq.heappush(heap, (-nums[i], i))
        ans.append(-heap[0][0]) # first max
        while right < len(nums) - 1:
            left += 1
            right += 1
            heapq.heappush(heap, (-nums[right], right))
            while heap[0][1] < left:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
            