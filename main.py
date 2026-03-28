# ages = [18, 19, 20, 18, 21]
#       0   1   2   3   4

# count = len(ages) # 5
# avg_age = 0

# i = 0
# while i < count: # 5 < 5
#     this_user_age = ages[i]
#     avg_age += this_user_age
    
#     i += 1

# for this_user_age in ages:
#     print('inside the for loop:', this_user_age)
#     avg_age += this_user_age

# avg_age /= count

# print(f'{avg_age=}')

# numbers = []

# print('before appending:', numbers)

# numbers.append(6)
# numbers.append(5)
# numbers.append(6)

# print('after appending:', numbers)

# numbers.clear()

# numbers = [1,2,3,4] # 0 .. 20 -> 4..7 --- 12..15

# copy = numbers.copy()
# copy[0] = 67
# print('copy:', copy)

# numbers = [1,2,3,4,4,1,4]
# count = numbers.count(4)

# numbers = [1,2,3]
# ages = [18, 19, 20, 18, 21]

# numbers.extend(ages) # better

# print(numbers + ages) # good


# numbers = [10, 8, 30]

# index = numbers.index(8)

# numbers = [10, 8, 30] 

# numbers.insert(10, 67) # 10, 67, 8, 30

# numbers = [10, 8, 30] 

# removed = numbers.pop()

# print(f'{removed=}')

# numbers = [10, 8, 30] 
# numbers.remove(8)

# numbers = [10, 8, 30, 5] 

# numbers.reverse()
# numbers.sort()

# print(f'{numbers=}')

# numbers = [1,200,12,4,5]

# slice = numbers[:] # numbers.copy()
# slice = numbers[0::2]
# slice = numbers[3:]
# slice = numbers[-3]
# slice[0] = 123

# numbers = [1,200,12,4,5]
# slice = numbers[:1:-2]

# print(f'{slice=}')
# print(f'{numbers=}')

# string = 'some textual value'
# strings = list(string) # []

# strings = [char.upper() for char in string]

# strings = []
# for char in string:
#     strings.append(char.upper())

# print(f'{strings=}')

# numbers = [1,2,3,4,5]

# for i, number in enumerate(numbers):
#     print(i, number)

# numbers = [1,2,3,4,5]

# first = numbers[0]
# rest = numbers[1:]

# first, second, *rest, last = numbers
# print(f'{first=}')
# print(f'{second=}')
# print(f'{rest=}')
# print(f'{last=}')

numbers = [1]
first, *rest = numbers

print(f'{first=}')
print(f'{rest=}')