def replace_in_list(my_list, idx, element):
    my_list = [1, 2, 3, 4, 5]
    idx = int(input("Enter an index to replace the element: "))
    element = input("Enter the new element: ")
    my_list[idx] = element
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        print("The new list is", my_list)
replace_in_list(my_list = '', idx = '', element = '')