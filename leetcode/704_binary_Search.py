from typing import List

def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)
    count = 0
    while True:
        if count == 5:
            exit()
        count += 1
        middle_idx = (low + high) // 2
        print(middle_idx, nums[middle_idx], nums[low:high])
        if target == nums[middle_idx]:
            return middle_idx
        if len(nums[low:high]) == 1:
            return -1
        elif target < nums[middle_idx]:
            high = middle_idx
        else:
            low = middle_idx

nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))