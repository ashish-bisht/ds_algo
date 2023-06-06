# https: // leetcode.com/problems/missing-number/

def missing_number(nums):
    current_index = 0

    while current_index < len(nums):
        correct_index = nums[current_index]

        if correct_index < len(nums) and correct_index != current_index:
            nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]
        else:
            current_index += 1

    for index in range(len(nums)):
        if nums[index] != index:
            return index
    return len(nums)


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
