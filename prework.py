def hello_name(user_name):
    print('Hello ' + user_name.title() + '!')

# hello_name('Joel')

def greeting(user_name):
    print('Hello {}'.format(user_name.title())) # *args
    print(f'Hello again {user_name.title()}')

# greeting('Joel')


# Question 2
def odd_numbers():
    for i in range(0, 101):
        if i % 2 != 0:
            print(i)

def odd_numbers2():
    for i in range(1, 101, 2):
        print(i)



# odd_numbers2()

# Question 3
def max_num_in_list(a_list):
    return max(a_list)

def max(a_list):
    a_list.sort()
    return a_list[-1]


the_list = [45,46,200,250,24,1,0,1000]
# print(max(the_list))

def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 400 == 0:
        return True
    else:
        return False


a_list = [5,4,7,1,9]
another_one = [1,2,3,4,5]
def consecutive(a_list):
    for num in a_list[1:]:
        last_num = num
        last_num += 1
        if num != last_num:
            return False
        else:
            return True

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

print(consecutive(another_one))