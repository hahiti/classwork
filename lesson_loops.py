#print ('hello world')
#print ('hello world')
#print ('hello world')
#print ('hello world')
#print ('hello world')
import random

#for i in range (10):
#    if i % 2 == 0:
#        print ('hello world!', i)
#    else :
#         print ('happy new year!', i)


s='abcabc'
print (s[1:-1:2])
for i in range (100, 20, -2) :
    print ('Iteration#:', i)


for _ in range (10):
    print ('print smth!')



 #################################
print('--------------------')
for char in 'abc':
    print(char)

print ('--------------------')
for week_day in 'Mo', 'Tue', 'Wd', 'Th':
    print (week_day)


###########
for i in range (0, 101, 2):
    print (i)


def sum_of_n (n) :
    sum_total = 0
    for i in range (1, n + 1):
     sum_total += i
    return (sum_total)


print (sum_of_n (100))
print (sum_of_n (10))
print (sum_of_n (3))
print (sum_of_n (42))


text = 'Вы перешли в режим инкогнито.'
print (len(s.split (' '))-1)
print (s.count (' '))

def find_num_of_uppers (text):
     upper_total= 0
     for char in text:
        if char.isupper ():
           upper_total += 1

           return upper_total

print (find_num_of_uppers(text))

#########################

def camelize_me (var_name):
    var_name_Lst = var_name.split ('_')
    result = ''
    print (var_name_Lst)
    for part_name in var_name_Lst:
        #print (part_name, part_name.capitalize())
        result += part_name.capitalize()
    return result


print (camelize_me('This_is_a_long_snake_style_var_name'))
print (camelize_me('Style_var_me'))
print (camelize_me('a_b_c_d_e'))


def rand_num(args):
    pass


def avr_whatever_of_n(n, lower_bound, upper_bound):
    rand_total = 0
    for _ in range (n):
        rand_num = random.randint(lower_bound,upper_bound)
        print (rand_num)
        rand_total += rand_num
    avr_rand = rand_total / n
    return avr_rand

print (avr_whatever_of_n (11, 100, 200))
