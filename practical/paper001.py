"""
Q1:
How to reverse a string?
"""
# str1 = 'welcome'
# revStr1 = 'welcome'[::-1]
# print(revStr1)
# revStr2 = ''.join(reversed(str1))
# print(revStr2)

"""
Q2:
Write a python program for below problem statement:
input: 'my23name45is'
output: 'si23eman45ym'
"""
# str1 = 'my23name45is'
# print(str1)
# output = ''
# alphas = [char for char in reversed(str1) if char.isalpha()]
# print(alphas)
# i = 0
# for char in str1:
#     if char.isalpha():
#         output += alphas[i]
#         i += 1
#     else:
#         output += char
# print(output)

"""
Q3:
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
output: [(1,4,7), (2,5,8), (3,6,9)]
"""
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
# print(list(zip(list1, list2, list3)))

"""
Q4: 
Take the below two lists and print as expected.
list1 = ['my', 'name']
list2 = ['is', 'john']
output: my name is john
"""
# list1 = ['my', 'name']
# list2 = ['is', 'john']
# list1.extend(list2)
# print(list1)
# print(' '.join(list1))

"""
Q5:
Combine two lists and convert it to dictionary
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
"""
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# print(dict(zip(list1, list2)))

"""
Q6:
Write a python program to find duplicate characters in the below list
list1 = ['india', 'is', 'my', 'country']
"""
# list1 = ['india', 'is', 'my', 'country']
# dupList = []
# listStr = ''.join(list1)
# print(listStr)
# for char in listStr:
#     if listStr.count(char) > 1 and char not in dupList:
#         dupList.append(char)
# print(dupList)
# print(','.join(dupList))
# print(*dupList)

"""
Q7:
Write a program to print unique character in a string
str1 = 'test'
"""
# str1 = 'test'
# unique = []
# for char in str1:
#     if str1.count(char) == 1 and char not in unique:
#         unique.append(char)
# print(unique)
# print(*unique)

"""
Q8:
Write a one line for loop to print all the words in the below list which starts with character 'i'
list1 = ['india', 'is', 'my', 'country']
"""
# list1 = ['india', 'is', 'my', 'country']
# print([word for word in list1 if word.startswith('i')])

"""
Q9:
What would be the output if we declare the below variable.
data = 2E3
"""
# data = 2E3  # 2 is mantissa, E is base, 3 is exponent [2 * 10 to the power 3] and class type is float
# print(data)

"""
Q10: How to check a number is prime or not
"""
# num = 6
# flag = 0
# if num < 2:
#     print("The given number is not a prime number")
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 1:
#     print("Not a prime number")
# else:
#     print("Prime number")

"""
Q:11: Check factorial of a number. [3 -> 3 x 2 x 1]
"""
# num = 3
# factorial = 1
# if num < 0:
#     print("Factorial does not exists for negative number")
# elif num == 0:
#     print("The factorial for 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of number is: ", factorial)

"""
Q12:
Find 2nd largest number in a list
list1 = [8, 2, 45, 9, 23, 32]
"""
# list1 = [8, 2, 45, 9, 23, 32]
# list1.sort()
# print(list1)
# print("Second largest number: ", list1[-2])

"""
Q13:
Find duplicate items in a list
list1 = ["this", "is", "very", "good", "and", "this", "are", "also", "good"]
"""
