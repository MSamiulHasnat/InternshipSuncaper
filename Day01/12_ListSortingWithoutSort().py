def sort_list(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

input_list = [5, 3, 8, 6, 2, 7, 4, 1]
print("Sorted List:", sort_list(input_list))