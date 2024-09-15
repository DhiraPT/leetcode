class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = [num for _, num in sorted(zip(nums2, nums1), reverse=True)]
        nums2.sort(reverse=True)

        max_sum = sum(nums1[:k])
        min_heap = nums1[:k-1]
        heapq.heapify(min_heap)
        max_score = max_sum * nums2[k-1]
        for i in range(k, len(nums2)):
            heapq.heappush(min_heap, nums1[i-1])
            max_sum += nums1[i] - heapq.heappop(min_heap)
            max_score = max(max_score, max_sum * nums2[i])

        return max_score