def count_divisible_in_range(left_limit, right_limit, divisor_value):
    '''
    First task.
    Function return the count of integers that are divisible by number in range.
    '''

    if left_limit > right_limit:
        left_limit, right_limit = right_limit, left_limit
    return (((right_limit - (right_limit % divisor_value)) - left_limit) // divisor_value) + 1


def count_of_digits_and_letters(input_string):
    '''
    Second task.
    Function takes string as a parameter and return count number of letters and digits.
    '''

    digits = sum(map(str.isdigit, input_string))
    letters = sum(map(str.isalpha, input_string))

    return letters, digits


def sort_list_of_tuples(input_list_of_tuples):
    '''
    Function takes list of tuples and return sort it based on the next rule:
    name/age/height/weight
    '''

    return sorted(input_list_of_tuples, key=lambda x: (x[0], int(x[1]), -int(x[2]), int(x[3])))
