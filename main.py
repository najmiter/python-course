# age = 21
# gender = 'female'

# is_eligible = age >= 18 and gender == 'male'

# if is_eligible:
#     print('This dude is eligible!')
#     if age == 21:
#         print('Age is 21')
# elif age > 30:
#     print('This dude is OLD')
# elif age == 21:
#     pass
# else:
#     print('This dude NOT is eligible!')

# print('The end')

# color = 'indigo'

# if color == 'indigo':
#     pass
# elif color == 'red':
#     pass
# elif color == 'green':
#     pass

# color = 'red'
# has_pencil = True
# age = 10

# match color:
#     case 'indigo':
#         print('this color is indigo')
#     case 'red' if has_pencil:
#         print('this color is red')
#     case 'green':
#         print('this color is green')
#     case _:
#         print('this is a universal color')

value = 'some string'

match value:
    case '1':
        print('The value is 1')
    case 2:
        print('The value is 2')
    case int():
        print('The value is an integer')
    case float():
        print('The value is a float')
    case str():
        print('The value is a str')
    case _:
        print('This is an unknown value')

print('The end')