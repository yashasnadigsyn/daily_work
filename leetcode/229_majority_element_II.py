from typing import List

def majorityElement(nums: List[int]) -> List[int]:
    cnd = int(len(nums)/3)
    hashy = {}
    for i in range(len(nums)):
        if nums[i] in hashy:
            hashy[nums[i]] += 1
        else:
            hashy[nums[i]] = 1

    return [k for k, v in hashy.items() if v > cnd]

print(majorityElement([1,2]))
    