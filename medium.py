# # 1 Multiply Vectors

# # create lists
# list_of_numbers = [2,4,5]
# another_list_of_numbers = [2,3,6]
# list_of_products = []

# # keep track of for loop steps
# step = 0

# for num in list_of_numbers:
#   try:
#     # multiply same index positions from each list together
#     list_of_products.append(list_of_numbers[step] * another_list_of_numbers[step])

#     # this also works but not as clear
#     # list_of_products.append(num * another_list_of_numbers[step])

#     step += 1
#   except IndexError:
#     print('WARNING lists are NOT of equal size')
#     break

# print(f'{list_of_numbers} x {another_list_of_numbers} = {list_of_products}')

# # 2 Matrix Addition

# # create list of lists
# list_of_lists_of_numbers = [[1,3,2,4],[5,2,1,0]]

# index = 0

# # check if length of list 1 == list 2
# if len(list_of_lists_of_numbers[0]) == len(list_of_lists_of_numbers[1]):
#   # add an empty list
#   list_of_lists_of_numbers.append([])
#   # while index is less than either length of lists
#   while index <= len(list_of_lists_of_numbers[0]) or len(list_of_lists_of_numbers[1]):
#     # append the addition of each numbers in the same index to the empty list we appended earlier
#     list_of_lists_of_numbers[2].append(list_of_lists_of_numbers[0].pop() + list_of_lists_of_numbers[1].pop())
#     index += 1
#   # save to a new list
#   list = list_of_lists_of_numbers[2]
#   # print the reverse of new list
#   print(list[::-1])
# else:
#   print('WARNING lists are NOT of equal size')
#   # add an empty list
#   list_of_lists_of_numbers.append([])
#   # while index is less than either length of lists
#   while index <= len(list_of_lists_of_numbers[0]) or len(list_of_lists_of_numbers[1]):
#     # append the addition of each numbers in the same index to the empty list we appended earlier
#     list_of_lists_of_numbers[2].append(list_of_lists_of_numbers[0].pop() + list_of_lists_of_numbers[1].pop())
#     index += 1
#   # save to a new list
#   list = list_of_lists_of_numbers[2]
#   # print the reverse of new list
#   print(list[::-1])

# 3 Matrix Addition II

