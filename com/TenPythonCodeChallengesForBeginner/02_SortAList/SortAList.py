# This function will take a list of numbers and an input for order. Order value can only be "asc", "desc", or "none".
# This function will then perform based on the order parameter.

valid_order = ('asc', 'desc', 'none')


def sort_list(nums: list, order: str) -> list:
    if order not in valid_order:
        raise ValueError('Please only enter "asc", "desc", or "none" and try again!')

    if order == "asc":
        nums.sort()
        return nums

    elif order == "desc":
        nums.sort(reverse=True)
        return nums

    else:
        return nums


number = [1, 5, 3, 2, 9]
sorted_list = sort_list(number, 'none')
print(f"Final sorted list is: {sorted_list}")
