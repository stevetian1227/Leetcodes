def maxSubArray(nums) -> int:
        overallMaxSum = nums[0]
        currentMaxSum = nums[0]
        for i in range(len(nums)) :
            currentMaxSum = max(nums[i], currentMaxSum+nums[i])
            overallMaxSum = max(overallMaxSum, currentMaxSum)
        return overallMaxSum