from functools import reduce

############## Tuple ###############
# Inmutable
number_tuple = (1,2,3,3,3,3)

############## List ###############
number_list = []
number_list.append(1)
number_list.remove(number_list.index(1))
size = len(number_list)
another_list = [2,2,2,2]
number_list.extend(another_list)
number_list.clear()

############## Set ###############
some_set = set([1,2,2,2,2,2])
belongs = 7 in some_set

############## Frozen set ###############
fruits = { 'apple' , 'watermelon' }
fruit_frozen_set = frozenset(fruits)

############## Dictionary ###############
student_scores = {
    'dante' : [100,100,100],
    'blanca' : [100,100,100]
}

############## Ternary operator ###############
message = 'Te amo blanca' if True else 'Como quiera te amo'

############## Foreach ###############
name_list = ['Dante' , 'Blanca']
for name in name_list:
    print(name)

############## For ###############
for i in range(5):
    print('Tas bien chula bb')
    
############## For enum ###############
another_name_list = ['Dante' , 'Blanca']
for i,value in enumerate(another_name_list):
    print(another_name_list[i])

############## Collection MAP ###############
# Higher order function MAP
name_list_uppercase = list(map(str.upper(), name_list))

############## Collection FILTER ###############
# Higher order function FILTER
another_number_list = [1,2,3,3,4,7,0,5,5]
is_odd = list(filter( lambda n: n%2==0 , another_number_list ))

############## Collection SORT ###############
# Higher order function SORT
students = [
    ('Dante', 22, 100),
    ('Blanca', 21, 100)
]
sorted_list_students = list(sorted( lambda x: x[1] ,students ))

# Higher order function REDUCE
numbers = [6,6,6,6,6,6,6,6]
total = reduce( lambda x,y : (x + y) * 2 , numbers)

############## Class ###############
class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password


############## Inheritance ###############
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


############## List comprehention ###############
numbers = [1,2,3,4,5]

numbrers_sqrts = []
for n in numbers:
    numbrers_sqrts.append(n**2)

sqrts = [n**2 for n in numbers if n%2 == 0]

matrix = []
for _ in range(3):
    intern_list = []
    for i in range(3):
        intern_list.append(i)
    matrix.append(intern_list)

matrix2 = [[i for i in range(3)] for _ in range(3)]
