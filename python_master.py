from functools import reduce

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

# Higher order function MAP
name_list_uppercase = list(map(str.upper(), name_list))

# Higher order function FILTER
another_number_list = [1,2,3,3,4,7,0,5,5]
is_odd = list(filter( lambda n: n%2==0 , another_number_list ))

# Higher order function SORT
students = [
    ('Dante', 22, 100),
    ('Blanca', 21, 100)
]
sorted_list_students = list(sorted( lambda x: x[1] ,students ))

# Higher order function REDUCE
numbers = [6,6,6,6,6,6,6,6]
total = reduce( lambda x,y : (x + y) * 2 , numbers)

# Classes
class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def say_something(self):
        return "I hate communists"
    
# Inherence
class Student(User):
    def __init__(self, name, password, registration):
        super().__init__(name, password)
        self.registration = registration

    @property
    def registration(self):
        return self._registration

    @registration.setter
    def registration(self, registration):
        self._registration = registration
