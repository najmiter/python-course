# while loop

# number = 1

# while number < 10:
#     print('Inside the loop:', number)
#     number += 1

#############################

# for number in range(2, 10, 2):
#     print('Inside the loop:', number)

#############################

# for number in range(20, 10, -1):
#     print('Inside the loop:', number)

#############################

# for number in range(10):
#     if number == 5:
#         break
#     print('Inside the loop:', number)

#############################

# while True:
#     number = input('Type 5: ')

#     if number == '5':
#         print('Bye')
#         break
    
#     print('The number you input:', number)

#############################

# for number in range(5):
#     print('Before the check')

#     if number == 3:
#         continue

#     print('Inside the loop:', number)

#############################

# number = 1

# while number < 5:
#     number += 1
#     if number == 10:
#         break
# else:
#     print('The loop was not broken')

#############################

for number in range(10):
    if number == 50:
        break
else:
    print('The loop was not broken')