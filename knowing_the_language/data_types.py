# num types

num1: int = 1;
num2: float = 2.0;
num3: complex = 3.000053462873642;

print(num1,num2,num3)
print("\n")

# text types

nome: str = "david"

print(nome,"\n")

# sequence

## list 

numbers = [1,2,3,4,5]

### add new number to the list

numbers.append(6)

### access to an element

print(numbers[0],"\n")

### modifying an element

numbers[0] = 10

### showing the list

for number in numbers:
    print(number)

## tuple

### x,y tuple

point = (10,20)

### tuple element access

print(point[0],"\n");

### unpacking tuple

x,y = point

print("x: ",x , "y: ",y ,"\n")


## range

### loop using range

for i in range(5):
    print(i)

print("\n")

### range with defined intervals

for i in range(1, 10, 2):
    print(i)

print("\n")

# map

## dict

### using dict to create some kind of object

person = dict(name = "John", age=20 , city="New York")

print(person,"\n");

### another way to do it

person = dict([('name', 'John'), ('age' ,30), ('city', "New York")])

print(person,"\n");

# Collection(groups like)

## set

my_set = {1, 2, 3, 4, 5}

### adding new element

my_set.add(6)

### removing existing element

my_set.remove(6)

### set operations

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}

#### union

union_set = set1 | set2

#### intersection

inter_set = set1 & set2

#### difference

dif_set = set1 - set2

#### Symmetric difference

symdif_set = set1 ^ set2

#### printing all of them
print("union: ", union_set,"\ninter: ", inter_set, "\ndif: ", dif_set, "\nsymdif: ", symdif_set, "\n")

## frozenset (immutable ver of set)

my_frozenset = {1, 2, 3, 4, 5, 6}

### frozenset operations

frozenset1 = {1, 2, 3, 4}
frozenset2 = {4, 5, 6, 7}

#### union

union_frozenset = frozenset1 | frozenset2

#### intersection

inter_frozenset = frozenset1 & frozenset2

#### difference

dif_frozenset = frozenset1 - frozenset2

#### symmetric difference

syndif_frozenset = frozenset1 ^ frozenset2

### printing all of them

print("union: ", union_frozenset, "\ninter: ", inter_frozenset, "\ndif: ", dif_frozenset, "\nsyndif: ", syndif_frozenset)

# boolean

## bool

sim: bool = True

print(sim)

# binary 

## bytes

### creating bytes

my_bytes = b'hello'

### accessing elements

print(my_bytes[0])

## bytearray

### creating bytearrays

my_bytearray = bytearray(b'hello')

### modifing the bytearray

my_bytearray[0] = 120 #changing h to x 

### printing the bytearray

print(my_bytearray)

## creating memoryview

data = bytearray(b'hello')

my_memoryview = memoryview(data)

## codifying elements

my_memoryview[0] = 121  #changing h to x

##printing the memoryview

print(data) 
