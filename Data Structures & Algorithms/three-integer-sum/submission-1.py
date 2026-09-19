class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        groups = []
        n = len(nums)
        
        for i in range(n):
            # Пропускаем дубликаты для nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    groups.append([nums[i], nums[left], nums[right]])
                    # Вместо break двигаем оба указателя,
                    # чтобы найти другие пары для этого nums[i]
                    left += 1
                    right -= 1
                    # Пропускаем дубликаты для left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Пропускаем дубликаты для right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return groups