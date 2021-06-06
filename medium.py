# 1 Multiply Vectors

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

# 2 Matrix Addition

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
#   # warning to user
#   # comments removed (same as above)
#   print('WARNING lists are NOT of equal size')
#   list_of_lists_of_numbers.append([])
#   while index <= len(list_of_lists_of_numbers[0]) or len(list_of_lists_of_numbers[1]):
#     list_of_lists_of_numbers[2].append(list_of_lists_of_numbers[0].pop() + list_of_lists_of_numbers[1].pop())
#     index += 1
#   list = list_of_lists_of_numbers[2]
#   # output should be [6, 5, 3, 4]
#   print(list[::-1]) 

# # 3 Matrix Addition II

# print('I accidentally solved this in number 2 :-D')

# 4 De-dup

# list_of_numbers_with_duplicates = [0,1,2,3,0,1,2,3]
# list_of_strings_with_duplicates = ['a','b','c','d','a','b','c','d']

# for num in list_of_numbers_with_duplicates:
#   while list_of_numbers_with_duplicates.count(num) != 1:
#     list_of_numbers_with_duplicates.pop(list_of_numbers_with_duplicates.index(num))

# for string in list_of_strings_with_duplicates:
#   while list_of_strings_with_duplicates.count(string) != 1:
#     list_of_strings_with_duplicates.pop(list_of_strings_with_duplicates.index(string))

# print(list_of_numbers_with_duplicates)
# print(list_of_strings_with_duplicates)

# # 5 Leetspeak

# user_input = input(
# """I'm a babelfish. I can translate any language into another language.
# Here I'll show you...
# I'll translate anything you type into leetspeak
# """
# )

# translated_text = ""

# # check for and replace every letter
# for letter in user_input:
#   if letter.capitalize() == "A":
#     translated_text += "4"
#   elif letter.capitalize() == "E":
#     translated_text += "3"
#   elif letter.capitalize() == "G":
#     translated_text += "6"
#   elif letter.capitalize() == "I":
#     translated_text += "1"
#   elif letter.capitalize() == "O":
#     translated_text += "0"
#   elif letter.capitalize() == "S":
#     translated_text += "5"
#   elif letter.capitalize() == "T":
#     translated_text += "7"
#   # since no letters matched, add it to the translated text unaltered
#   else:
#     translated_text += letter

# print(translated_text)

# 6

