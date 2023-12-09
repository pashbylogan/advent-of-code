def _get_number_using_derivative(nums):
    if all(num == 0 for num in nums):
        return 0

    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append(nums[i + 1] - nums[i])

    return _get_number_using_derivative(new_nums) + new_nums[-1]


def p1(file):
    answer = 0

    for line in file:
        nums = [int(num) for num in line.split()]
        answer += nums[-1] + _get_number_using_derivative(nums)

    return answer


def _get_number_using_derivative_p2(nums):
    if all(num == 0 for num in nums):
        return 0

    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append(nums[i + 1] - nums[i])

    return new_nums[0] - _get_number_using_derivative_p2(new_nums)


def p2(file):
    answer = 0

    for line in file:
        nums = [int(num) for num in line.split()]
        answer += nums[0] - _get_number_using_derivative_p2(nums)

    return answer


with open('inputs/d9') as file:
    # print(p1(file))
    print(p2(file))
