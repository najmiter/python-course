# def drink_tea(cheeni=0, milk=0.5):
#     print('drink: cheeni =', cheeni, ',milk =', milk)

# def make_tea():
#     print('make: 1. take some milk')
#     print('make: 2. take more water')
#     print('make: 3. take some patti')
#     print('make: 4. let him cook')

# def main():
#     print('main: before making the tea')
#     make_tea()
#     drink_tea(1, 7)

#####################################
#####################################

# def user_details(name, age):
#     print('the name is', name)
#     print('the age is', age)

# def user_details(name, /, age, email=''):
#     print('the name is', name)
#     print('the age is', age)

# def user_details(name, /, *args, age):
#     print('user name:', name)
#     i = 0
#     while i < len(args):
#         print('user details:', args[i])
#         i += 1

#     print('user age:', age)

# def user_details(**args):
#     print('user details:', args['old'])

# def user_details(name, age, /, *args, **kwargs):
#     print('user details:', args)
#     print('user details:', kwargs)

# def main():
#     user_details('CodeMite', 90, 'myemail@example.com', 'Other', old=True, other=False)

#####################################
#####################################

def add(num1, num2): # num1=5, num2=5
    result = num1 + num2 # result = 5 + 5
    if result == 5:
        return
    
    result += 10
    return result
    
def main():
    sum = add(5, 5) # 20
    print('the sum is:', sum)


main()
