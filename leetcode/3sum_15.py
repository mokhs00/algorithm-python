from typing import List

'''
O(n^2)에 해결해야함
투 포인터 기법을 이용
- 배열을 미리 정렬해두고 O(n log n) 
- 배열을 순회하면서 다음 규칙을 따름
  - 현재 index는 i 그리고 left, right 라는 포인터를 두고 
  - i를 기준으로 nums[i] + nums[left] + nums[right] == 0인 값을 찾아서
  - results 에 append 한다.
  - 포인터가 움직이는 기준은 다음과 같다
    - sum < 0 이라면 left + 1, sum > 0 이라면 right - 1 (정렬 해둠을 기억)
  - results에 값이 겹치면 안되므로 results 에 append 한 이후에 
    left right 포인터를 겹치는 만큼 이동시킨다. 
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
