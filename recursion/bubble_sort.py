my_list = [2,4,3,1,2,4,56,7,88,2,11,33]

for j in range(len(my_list)):
    for i in range(len(my_list)):

        if (i + 1) < len(my_list):
            print("Im in the trap")
            swap_a = my_list[i]
            swap_b = my_list[i + 1]
            
            # determines the sort order
            if swap_a < swap_b:
                print("Im int he swap")
                my_list[i] = swap_b
                my_list[i + 1] = swap_a