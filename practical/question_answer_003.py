"""
14. Write a python program to get the duplicate characters in a list?
"""
# listData = ['india', 'is', 'my', 'country']
# listStr = ''.join(listData)
# print(listStr)
# duplicates = []
# for char in listStr:
#     if listStr.count(char) > 1 and char not in duplicates:
#         duplicates.append(char)
# print("Duplicate characters in a list: ", duplicates)


# =============================================================
""" Convert list of numbers into comma separated string """
# listNum = [1, 2, 3, 4, 5, 6]
# listNumStr = ','.join(str(i) for i in listNum)
# print(listNumStr)

# =============================================================
""" Count the duplicate words and with a particular count of occurrence  """
# strExample = "thisistest"
#
# duplicates = []
#
# for char in strExample:
#     if strExample.count(char) > 1 and strExample.count(char) == 3 and char not in duplicates:
#         print(char + "::" + str(strExample.count(char)))
#         duplicates.append(char)
# print(duplicates)

# ==============================================================
""" 
Objective: Get duplicate words in list
1. Take input a sentence
2. Take input desired number of words to be displayed
"""
# str1 = input("Enter a sentence: ")
# n = int(input("Enter a count: "))
# str1 = str1.split()
# print(str1)
# counts = dict()
# for word in str1:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# print(counts)
# final_list = []
# for key in counts:
#     if counts[key] >= 2 and key not in final_list:
#         final_list.append(key)
#
# if len(final_list) > 0:
#     print(final_list)
# else:
#     print("NA")
# =================================================================
"""
Reverse words in a sentence 
"""
# exm_string = "This is test automation"
# list_exm_string = exm_string.split()
# print(list_exm_string)
# rev_list_exm_string = list_exm_string[::-1]
# print(rev_list_exm_string)
# rev_exm_string = ' '.join(rev_list_exm_string)
# print(rev_exm_string)
# =============================================
""" 
Create a list from another list with unique numbers
"""
# list1 = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
# list2 = []
# for num in list1:
#     if list1.count(num) == 1 and num not in list2:
#         list2.append(num)
# print(list2)
# =============================================================
"""
q. mystr = "a,a,a,b,b,c,c,c"
result: a:3, b:2, c:3
"""
# mystr = "a,a,a,b,b,c,c,c"
# list_mystr = mystr.split(",")
# visited = []
# for char in list_mystr:
#     if char not in visited:
#         print(f"{char}:{list_mystr.count(char)}", end=",")
#         visited.append(char)

"""
Get count of duplicate char
listtest = ["my", "country", "name", "is", "india"]
"""
# listtest = ["my", "country", "name", "is", "india"]
# str_liststr = ''.join(listtest)
# print(str_liststr)
# for char in str_liststr:
#     if str_liststr.count(char) > 2:
#         print(char + "::" + str(str_liststr.count(char)), end=",")
# ==============================================
""" max and min in a list """
# list1 = [10, 34, 23, 5, 2, 67, 87, 44]
# min = list1[0]
# max = list1[0]
# for num in list1:
#     if num < min:
#         min = num
#     if num > max:
#         max = num
# print("The min number: " + str(min))
# print("The max number: " + str(max))
# =====================================================
"""
get a list of square of even numbers in another list
"""
# list_test = [23, 4, 53, 21, 8, 1, 6, 5]
# list_even = []
# for num in list_test:
#     if num % 2 == 0:
#         list_even.append(num * num)
# print(list_even)
# =====================================================
"""
get a list of square of even numbers in another list with list comprehension
"""
# list_test1 = [23, 4, 53, 21, 8, 1, 6, 5]
#
# list_even1 = [num * num for num in list_test1 if num % 2 == 0]
# print(list_even1)
# ======================================================
""" 
Objective: Get duplicate words in list
1. Take input a sentence
2. Take input desired number of words to be displayed
"""
# str1 = input("Enter a sentence: ")
# number = int(input("Enter a number: "))
# list_word = str1.split()
# word_dict = dict()
# for word in list_word:
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1
# print(word_dict)
# final_list = []
# for key in word_dict:
#     if word_dict[key] >= number:
#         final_list.append(key)
# print(final_list)
# ========================================================
""" Dictionary traversing """
# dict1 = {"name": "subhendu", "age": 25, "address": "kolkata"}
# dict1["phone"] = 1234
# print(dict1)
# print(dict1.keys())

str1 = "subhendu"
str2 = str1[::-1]
print(str2)



