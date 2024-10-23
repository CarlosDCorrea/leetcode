from typing import List


def main2(nums: List[int]) -> bool:
    l = float("inf")
    r = float("inf")

    # What is the logic behind it?
    for num in nums:
        if num <= l:
            l = num
        elif num <= r:
            r = num
        else:
            return True
    return False


def main(nums: List[int]) -> bool:
    n = len(nums)

    min_left = [0] * n
    max_right = [0] * n

    min_till_now = nums[0]
    max_till_now = nums[-1]
    # [6,7,1,2]
    for i in range(n):
        min_till_now = min(min_till_now, nums[i])
        min_left[i] = min_till_now

    for i in range(n - 1, -1, -1):
        max_till_now = max(max_till_now, nums[i])
        max_right[i] = max_till_now
    
    for i in range(n):
        if min_left[i] < nums[i] < max_right[i]:
            return True
    else:
        return False
        

test1 = [1,2,3,4,5]
test2 = [5,4,3,2,1]
test3 = [2,1,5,0,4,6]
test4 = [1,5,0,4,1,3]
test5 = [6,7,1,2]
test6 = [6, 7, 8, 1, 9, 2, 3]
test7 = [1,2,1,3]
test8 = [1,6,2,5,1]
test9 = [20,100,10,12,5,13]
test10 = [4,5,2147483647,1,2]
test11 = [6,7,1,2]

print(main2(test10))