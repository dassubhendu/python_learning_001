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
Find duplicate items/words/integer in a list
list1 = ["this", "is", "very", "good", "and", "this", "are", "also", "good"]
"""
# list1 = ["this", "is", "very", "good", "and", "this", "are", "also", "good"]
# dupWordList = []
# for i in range(len(list1)):
#     k = i + 1
#     for j in range(k, len(list1)):
#         if list1[i] == list1[j] and list1[i] not in dupWordList:
#             dupWordList.append(list1[i])
# print(dupWordList)       

"""
Q14:
Write a python program to get the duplicate characters in a list.
listData = ['india', 'is', 'my', 'country']
"""
# listData = ['india', 'is', 'my', 'country']
# dupCharList = []
# strListData = ''.join(listData)
# print(strListData)
# for char in strListData:
#     if strListData.count(char) > 1 and char not in dupCharList:
#         dupCharList.append(char)
# print(dupCharList)  
# print(*dupCharList)    
# print(','.join(dupCharList))  

"""
Q15:
Count the duplicate character and with a particular count of occurrence in a string. Let say char appears 3 times
strExample = "thisistest"
"""
# strExample = "thisistest"
# dupList = []
# for char in strExample:
#     if strExample.count(char) == 3 and char not in dupList:
#         dupList.append(char)
# print(dupList)  
# print(*dupList)  
# print(','.join(dupList))   


"""
Q16:
Reverse words in a sentence.
input: "This is my school"
output: ""
"""
# str1 = "This is my school"
# strList1 = str1.split(' ')
# print(strList1)
# revStrList1 = strList1[::-1]
# print(revStrList1)
# print(' '.join(revStrList1))

"""
Q17:
Reverse a string without any inbuild methods.
str1 = "thisisschool"
"""
# str1 = "thisisschool"
# revStr1 = str1[::-1]
# print(revStr1)
# ==========================
# str1 = "thisisschool"
# reversed_str = ""
# for i in range(1, len(str1) + 1):
#     reversed_str += str1[-i]
# print(reversed_str)    


"""
Q18:
myStr1 = "a,a,a,b,b,c,c,c"
result: a:3, b:2, c:3
"""
# myStr = "a,a,a,b,b,c,c,c"
# visited = []
# listMyStr = myStr.split(",")
# print(listMyStr)
# for char in listMyStr:
#     if char not in visited:
#         print(f"{char}:{listMyStr.count(char)}", end=",")
#         visited.append(char)

"""
Q19:
input: "sky is blue"
output: "blue is sky"
"""
# str1 = "sky is blue"
# listStr1 = str1.split(' ')
# print(listStr1)
# revListStr1 = listStr1[::-1]
# print(revListStr1)
# revWordStr = ' '.join(revListStr1)
# print(revWordStr)

"""
Q20:
list1 = [1,2,2,3,3,4,5,5,5,6,6]
output = [1, 4]
"""
# list1 = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
# uniqueList = []
# for num in list1:
#     if list1.count(num) == 1 and num not in uniqueList:
#         uniqueList.append(num)
# print(uniqueList)

"""
Q21:
Find max and min number in a list
listNum = ['34', '23', '8', '64', '76', '2']
"""
# list = [34, 23, 8, 64, 76, 2]
# max = list[0]
# min = list[0]
# for num in list:
#     if num < min:
#         min = num
#     if num > max:
#         max = num
# print("The min number: " + str(min))
# print("The max number: " + str(max))

"""
Q22:
Get a list of square of even numbers in another list with list comprehension
list1 = [5, 2, 6, 4, 7, 8]
"""
# list1 = [5, 2, 6, 4, 7, 8]
# print([num * num for num in list1 if num % 2 == 0])

""" 
Q23:
Objective: Get duplicate words in list
list1 = ["he", "is", "my", "friend", "and", "he", "is", "good"]
"""
# list1 = ["he", "is", "my", "friend", "and", "he", "is", "good"]
# dupWord = []
# for i in range(len(list1)):
#     k = i + 1
#     for j in range(k, len(list1)):
#         if list1[i] == list1[j] and list1[i] not in dupWord:
#             dupWord.append(list1[i])
# print(dupWord)










