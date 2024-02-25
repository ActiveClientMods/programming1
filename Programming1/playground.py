import random
from faker import Faker
from faker import Faker
import random

#  Match-Statement with case
""" def get_type(value):
    match (type(value).__name__):
        case 'int':
            return 'integer'
        case 'float':
            return 'number'
        case'str':
            return'string'
        case 'bool':
            return 'boolean'
        case 'list':
            return 'array'
        case 'tuple':
            return 'array'
        case 'dict':
            return 'object'
        case'set':
            return 'array'
        case 'frozenset':
            return 'array'
        case 'bytes':
            return'string'
        case 'bytearray':
            return'string'
        case'memoryview':
            return'string'
        case 'NoneType':
            return 'null'
        case 'type':
            return'string'

print(get_type(3.14)) """

# Logical Expressions

""" def AND(a, b):
    try:
        if a and b == True:
            print("Light on! a and b are True")
        else:
            print("Light off! a and b are not True")
    except:
        print("Invalid input!")
    

def OR(a, b):
    try:
        if a or b == True:
            print("Light on! a or b are True")
        else:
            print("Light off! Both are not True")
    except:
        print("Invalid input!")

def NOT(a):
    try:
        if not a == True:
            print("Light on! a is not True")
        else:
            print("Light off! a is True")
    except:
        print("Invalid input!")

def NAND(a, b):
    try:
        if not (a and b) == True:
            print("Light on! a and b are not True")
        else:
            print("Light off! a and b are True")
    except:
        print("Invalid input!")

def NOR(a, b):
    try:
        if not (a or b) == True:
            print("Light on! a or b are False")
        else:
            print("Light off!  or b are True")
    except:
        print("Invalid input!")

def XOR(a, b):
    try:
        if a or b and not (a and b) == True:
            print("Light on! either a or b are True")
        else:
            print("Light off! either a or b are False")
    except:
        print("Invalid input!")

def XNOR(a, b):
    try:
        if (a and b) or (not a and not b) == True:
            print("Light on! and b are True")
        else:
            print("Light off! a and b are False")
    except:
        print("Invalid input!") """


# Fibonacci Sequence
""" def fibonacci_sequence(n): """



# Prime numbers check
""" def prime_number1(num):
    checker = 2
    if num == 2:
        print(num, "is a prime number")
    else:
        while checker < num:
            if num % checker == 0:
                print(num, "is not a prime number")
                break  
            else:
                print(num, "is a prime number")
            checker += 1

prime_number1(30) """

# Prime numbers checker

""" def is_prime(num):
    if num < 2:
        return False
        print(num, "is not a prime number")
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            return False
    print(num, "is a prime number")        
    return True

is_prime(20) """


""" transactions = [{"type": "purchase", "date": "25.10.2023", "amount": 22}, 
                {"type": "sale", "date": "10.01.2024", "amount": 472}, 
                {"type": "purchase", "date": "01.01.2023", "amount": 373},
                {"type": "purchase", "date": "29.03.2023", "amount": 105},
                {"type": "sale", "date": "17.6.2022", "amount": 293},
                {"type": "purchase", "date": "03.01.2024", "amount": 583}]

transactions_type =transactions[0]["type"]
transactions_date =transactions[0]["date"]
transactions_amount =transactions[0]["amount"]

def list_comprehension(key):
    amount_value = [transaction["amount"] for transaction in transactions]
    print(list_comprehension("amount"))

def sum_up(type):
    amount_value = [transaction["amount"] for transaction in transactions if transaction["type"] == type]
    return(sum(amount_value))

income = sum_up("purchase")
expenses = sum_up("sale")
print("income = ", income)
print("expenses = ", expenses)

if income > expenses:
    print("You made money!")
else:
    print("You lost money!") """

#####
""" fake = Faker()

students = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18,25),
        "major": random.choice(["Computer Science, Mathematics", "Physics"]),
        "gpa": round(random.uniform(2.0,4.0), 2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

f_names = []
duplicates = []

for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    #print(first_name, last_name)
    #print("Age:", student["age"])
    if first_name in f_names:
        duplicates.append(first_name)
    else:    
        f_names.append(first_name)

duplicate_count = {
    name: f_names.count(name)
        for name in list(f_names)
        if f_names.count(name) > 1}


print(f_names)
print(duplicate_count) """

#######
""" def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

result = factorial(2)
print(result)

for n in range(5):
    print(factorial(n)) """
######
""" fibonacci_cache = {}

def fibonacci_recursive(n):
    if n in fibonacci_cache:
        print(f"Cache used for n = {n}")
        return fibonacci_cache[n]
    elif n == 0:
        #print(f"Cache updated for n = {n}")
        fibonacci_cache[0] = 0
        return 0
    elif n == 1:
        #print(f"Cache updated for n = {n}")
        fibonacci_cache[1] = 1
        return 1
    elif n == 2:
        #print(f"Cache updated for n = {n}")
        fibonacci_cache[2] = 1
        return 1
    else:
        result1 = fibonacci_recursive(n-1)
        result2 = fibonacci_recursive(n-2)
        #print(f"Cache updated for n = {n}")
        fibonacci_cache[n] = result1 + result2
        result = result1 + result2
        return result

for i in range(20):
    print(fibonacci_recursive(i)) """
###############

