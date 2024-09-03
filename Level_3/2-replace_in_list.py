def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        print("Index is out of range.")
        return my_list
    else:
        my_list[idx] = element
        return my_list
    
my_list = [1, 2, 3, 4, 5]
idx = int(input("Enter an index to replace the element: "))
element = input("Enter the new element: ")

new_list = replace_in_list(my_list, idx, element)
print("The new list is:", new_list)