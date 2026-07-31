class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = [key for key, _ in count.most_common(k)]
        return ans