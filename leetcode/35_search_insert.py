from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)
    while low<=high:
        mid = (low+high)//2
        print(nums[low:high], nums[mid], mid, low, high)
        if target == nums[mid]:
            return mid
        if len(nums[low:high]) == 1:
            return mid+1
        elif target < nums[mid]:
            high = mid
        else:
            low = mid
    return mid

# print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 0))
# print(searchInsert([1,3,5,6], 7))