class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans1, ans2 = sum(nums[0::2]), sum(nums[1::2])
        total = 0

        for i in range(len(nums)):
            if i%2 == 0:
                ans1 -= nums[i]
                if ans1 == ans2:
                    total += 1
                ans2 += nums[i]
            else:
                ans2 -= nums[i]
                if ans1 == ans2:
                    total += 1
                ans1 += nums[i]

        return total