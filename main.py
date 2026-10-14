from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Return the indices of two different elements whose sum is target."""
    seen = {}

    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index

    return []
