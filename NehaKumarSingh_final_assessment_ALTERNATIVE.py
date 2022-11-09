"""
TASK 1

(A)
Design a parent class called Animal

It must have general attributes: name, date of birth, colour, owner's name
Also it must have a method that gives you the age of an animal.

For example, if animal's date of birth is 2021/08/21 and today is
11 January 2021, the when you call get_age()
<name your method whatever you want> method, it should give us the age in
YEAR and MONTH like this: {'years': 0, 'months': 4}

(B)
B.1
Design a child class called Dog, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Grr', 'Bark', whatever you want)

B.2
Design a child class called Cat, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Meow', 'Purr', whatever you want)

(C)
Design an independent class called PetOwner. It is a small class, which should
have the __init__ method only accepting the 'name of an owner' and 'pet's id'.

SEE THE STARTER CODE BELOW

"""

from datetime import date
class Animal:

    def __init__(self, name, dob, colour, owner):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.owner = owner

    def get_age(self):
        today = date.today()
        year = today.year - self.dob.year -   ((today.month, today.day) <  (self.dob.month, self.dob.day))

        delta = today - self.dob
        months = delta.days/30
        if(months - year *12 > 12):
            months = months - year *12 - 12
        else:
            months = months - year *12

        return {'years': int(year), 'months':  int(months)}


class Dog(Animal):
    def __init__(self, name, dob, colour, owner,pet_id,bread):
        self.pet_id = pet_id
        self.bread = bread
        super(Dog, self).__init__(name, dob, colour, owner)

    def Sound(self):
        return 'Grr'

class Cat(Animal):
    def __init__(self, name, dob, colour, owner,pet_id,bread):
        self.pet_id = pet_id
        self.bread = bread
        super(Cat, self).__init__(name, dob, colour, owner)

    def Sound(self):
        return 'Meow'


class PetOwner:
    def __init__(self, name, pet_id):
        self.name = name
        self.pet_id = pet_id


animal = Animal('Neha', date(1997, 2, 3), 'white', 'ABC')
print(animal.get_age())

petId = '12345'
dog = Dog('Neha', date(1997, 2, 3), 'white', 'ABC', petId, 'Bread 1')
print(dog.get_age())
print(dog.Sound())

petId = '12345'
cat = Cat('Neha', date(1997, 2, 3), 'white', 'ABC', petId, 'Bread 2')
print(cat.get_age())
print(cat.Sound())


petOwner = PetOwner('Neha',petId)


# <class Dog with additional attributes: pet_id and breed, sound method HERE>

# <class Cat with additional attributes: pet_id and breed, sound method HERE>

# <independent class PetOwner with name and pet_id attributes HERE>


"""
TASK 2

We are going to utilize classes that we created as part of TASK 1. 

Let's imagine that we are a local vet clinic and given the input below, we 
need to add all pets to our register (register is just a dict). 

Please write a function, which parses given input and initializes a class for
each animal, as well as its owner and adds it to the register by id. 

EXAMPLE OUTPUT:

{
 10025: <__main__.Dog object at 0x0829DFB8>,
 10026: <__main__.Cat object at 0x082B4D90>,
 10042: <__main__.Dog object at 0x082B4130>,
 10053: <__main__.Dog object at 0x082B47F0>,
 10058: <__main__.Cat object at 0x07C80B50>
 }

 Each key is a pet id and each value is a newly initialized  Dog or Cat class. 
 Note that within each Dog and Cat class the variable "self.owner" is also 
 a class PetOwner with all relevant attributes.

SEE THE STARTER CODE BELOW

"""
# this is the input for your function

pet_info = [
    {'breed': 'German Shepherd',
     'colour': 'brown',
     'dob': '2021/09/21',
     'pet_id': 10025,
     'name': 'Lola',
     'owner': 'Maria Smith',
     'type': 'dog'},
    {'breed': 'Blue Russian',
     'colour': 'white',
     'dob': '2010/03/06',
     'pet_id': 10058,
     'name': 'Snowy',
     'owner': 'Malcolm Graham',
     'type': 'cat'},
    {'breed': 'Border Collie',
     'colour': 'beige',
     'dob': '2019/11/18',
     'pet_id': 10042,
     'name': 'Bailey',
     'owner': 'Priya Patel',
     'type': 'dog'},
    {'breed': 'Pug',
     'colour': 'black',
     'dob': '2021/10/16',
     'pet_id': 10053,
     'name': 'Ziggy',
     'owner': 'Mohamed Moussa',
     'type': 'dog'},
    {'breed': 'Sphynx',
     'colour': 'white',
     'dob': '2015/08/23',
     'pet_id': 10026,
     'name': 'Coco',
     'owner': 'Jennifer Coley',
     'type': 'cat'}
]


def register_pets(data):
    pets = dict()

    # <your code goes HERE>
    # don't forget to:
    # initialize the pet Owner as a class and reassign it to its Key
    # check the type to know which class to use for initialization
    # add a newly created pet (Cat or Dog) to your register by its id
    # name, dob, colour, owner, pet_id, bread
    for pet in data:

        if pet['type'] == 'dog':
            dog = Dog(pet['name'],date(1997, 2, 3),pet['colour'],pet['owner'],str(pet['pet_id']),pet['breed'])
            key = pet['pet_id']
            value= dog
            pets.update({key:value})
        else:
            cat = Cat(pet['name'], date(1997, 2, 3), pet['colour'], pet['owner'], str(pet['pet_id']), pet['breed'])
            key = pet['pet_id']
            value = cat
            pets.update({key: value})

    return pets


print(register_pets(pet_info))

"""
TASK 3

Write a function to sum up the digits of a given number.

EXAMPLE:

num = 78
result = 15

num = 333
result = 9

num = 12345
result = 15
===============================

Using recursion = 25 points

Any non recursive solution = 15 points

===============================

Hints for recursive approach:

1) Get the rightmost digit of the number with help of remainder 
‘%’ operator by dividing it with 10

2) Dividing a number by 10 with help of ‘/’ operator and converting it to int
helps you to 'move or iterate' through a number
"""

# <your code goes HERE>

def sum_of_digit(n):
    if n< 10:
        return n
    else:
        return n%10 + sum_of_digit(n/10)

# Read number
num = 78
digit_sum = sum_of_digit(num)
print(int(digit_sum))

num = 333
digit_sum = sum_of_digit(num)
print(int(digit_sum))

num = 12345
digit_sum = sum_of_digit(num)
print(int(digit_sum))
# Function call


# Display output


"""
TASK 4

CODING TASK

Write a function that takes in a non-empty string and returns its 
run-length encoding.

● For example, the run “AAA” will be “3A”
● The input string can contain special characters, including numbers 
● Long runs(10 or more chars) must be encoded in a split fashion:  
  “AAAAAAAAAAAA” (12 “A” s) → encoded as “9A3A”


Sample Input
string = "AAAAAAAAAAAAABBCCCCDD"

Sample Output
expected = "9A4A2B4C2D"

HINTS: 
● Traverse the input string and count the length of each run. 
As you traverse the string, what would you do when you reach a 
run of length 9 or the end of a run?
● When you reach a run of length 9 or the end of a run, 
store the computed count for the run, as well as its character.
● Make sure that your solution correctly handles the last run in the string. 
"""


def rle_encoding(string):
    char=string[0]
    count = 0
    list=[]
    for index in range(1,len(string)):
        if(char == string[index]):
            count = count+1
            if(count == 9):
                list.append(str(count) + char)
                count = 1
        else:
            list.append(str(count) + char)
            char = string[index]
            count =1
    list.append(str(count) + char)
    return list



string = "AAAAAAAAAAAAABBCCCCDD"
print(''.join(rle_encoding(string)))  # Expected "9A4A2B4C2D"

