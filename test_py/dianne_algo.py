

# inputs

value1 = [11,1,1980]
value2 = [10,8,1931]
value3 = [9,13,1958]

# data set hold all of the date of births

set_of_values = []

set_of_values.append(value1)
set_of_values.append(value2)
set_of_values.append(value3)



def base_num_generator(set_of_values_list):
    set_of_final_values = []
    """
    Expects a list
    """
    for each_set in set_of_values_list:
        set_of_final_values.append(sum(each_set))
    
    return set_of_final_values


#  if we get 9 it needs to be a 0

def set_nine_to_zero(num):

    if num == 0:
        return 0


    # number stack
    final_number_list = []
    updated_number = num

    while updated_number > 8:
        # this grabs our last digit
        last_digit = updated_number % 10
        # switch 9 to 0
        if last_digit == 9:
            last_digit = 0

        # take the digit and add it to the number lsit
        print("adding number : " + str(last_digit) + " to the stack")
        final_number_list.append(last_digit)

        changed_number = updated_number // 10
        updated_number = changed_number
    final_number_list.append(updated_number)

    # reverse the array
    fixed_number_list = final_number_list[::-1]
    return fixed_number_list
    



test_value = set_nine_to_zero(1992)
