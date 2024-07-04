"""
Q1:
nums=[3,6,8,12,14,15]
Using list comprehension we need to get square value of all the numbers, and we need add in a list
"""
# nums = [3, 6, 8, 12, 14, 15]
# print([num*num for num in nums])

"""
Q2:
nums=[3,6,8,12,14,15]
Using list comprehension we need to get square value of even numbers, and we need add in a list
"""
# nums = [3, 6, 8, 12, 14, 15]
# print([num * num for num in nums if num % 2 == 0])

"""
Q3:
nums=[3,6,8,12,14,15]
Using list comprehension we need to get square value of numbers divisible by 2 and 3, and we need add in a list
"""
# nums = [3, 6, 8, 12, 14, 15]
# print([num * num for num in nums if num % 2 == 0 if num % 3 == 0])

"""
Q4: 
nums=[3,6,8,12,14,15]
Using list comprehension get square of even numbers and cube of odd numbers
"""
# nums = [3, 6, 8, 12, 14, 15]
# print([num*num if num % 2 == 0 else num*num*num for num in nums])

"""
Q5: If we have nested for loop how we can do it using list comprehension
lst = []
for i in range(3, 6):
    for j in range(5, 7):
        lst.append(i*j)
print(lst) 
"""
print([i*j for i in range(3, 6) for j in range(5, 7)])

