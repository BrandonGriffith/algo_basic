class BinarySearch:
    def iterativeBinarySearch(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1

    def recursiveBinarySearch(nums, target):
        l, r = 0, len(nums) - 1
        def helper(l, r):
            if l > r:
                return -1
            m = l + ((r -l) // 2)
            if nums[m] == target:
                return m
            if nums[m] < target:
                return helper(m + 1, r)
            return helper(l, m - 1)
        return helper(l, r)
