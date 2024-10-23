from typing import List


def product_of_array_except_self(nums: List[int]) -> List[int]:
    # Two arrays for prefix and sufix results are created
    # for 
    prefix = [1] * len(nums)
    sufix = [1] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
        # last item is not evaluated since it does no thave sufix
        # print("===============================")
        # print(f"sufix [{i}]: {sufix[i]}")
        # print(f"nums [{i}]: {nums[i]}")

        # print(f"sufix [{i + 1}]: {sufix[i + 1]}")
        # print(f"nums [{i + 1}]: {nums[i + 1]}")

        if i == len(nums) - 2:
            sufix[i] = nums[i + 1]
        else:
            sufix[i] = sufix[i + 1] * nums[i + 1]

    for i in range(1, len(nums)):
        if i == 1:
            prefix[i] = nums[i - 1]
        else:
            prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(len(nums)):
        nums[i] = prefix[i] * sufix[i]

    return nums

test1 = [1, 2, 3, 4]
test2 = [-1,1,0,-3,3]

print(test1)
print(product_of_array_except_self(test2))
