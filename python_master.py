print('Te amo Blanca')

# Tuple
number_tuple = (1,2,3,3,3,3)

# List
number_list = []
number_list.append(1)
number_list.remove(number_list.index(1))
size = len(number_list)
another_list = [2,2,2,2]
number_list.extend(another_list)
number_list.clear()

# Set
some_set = set([1,2,2,2,2,2])
belongs = 7 in some_set

# Frozen Set
fruits = { 'apple' , 'watermelon' }
fruit_frozen_set = frozenset(fruits)

# Dictionary (Java map)
student_scores = {
    'dante' : [100,100,100],
    'blanca' : [100,100,100]
}

# Ternary operator
message = 'Te amo blanca' if True else 'Como quiera te amo'

# For each
name_list = ['Dante' , 'Blanca']
for name in name_list:
    print(name)
    
# For in range (Java for)
for i in range(5):
    print('Tas bien chula bb')
    
# For enum
another_name_list = ['Dante' , 'Blanca']
for i,value in enumerate(another_name_list):
    print(another_name_list[i])
    
def some_func():
    print('Do something')
    
def another_func(first , second):
    print(first , second)
    
another_func(second='a', first=1)