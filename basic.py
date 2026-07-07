# 1 Exercise 1: List Comprehension Mastery Write a
# single-line list comprehension that takes a list of 
# strings, filters out strings shorter than 4 characters, 
# and converts the remaining strings to uppercase. Given
# In:words =["apple", "bat", "cherry", "dog", "elderberry"] 
# Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
print("hello")
words =["apple", "bat", "cherry", "dog", "elderberry"]
#l=[] 
l=[w.upper() for w in words if len(w)>=4]
print((l))
#or 
words =["apple", "bat", "cherry", "dogg", "elderberry"]
li=[]
for word in words:
    if len(word)>=4:
        li.append(word.upper())
    else:
        pass
print(li)

# Exercise 2: Dictionary Merging with Logic Write a function
#  that merges two dictionaries. If a key exists in both
#  dictionaries, sum their values. If a key exists in only 
#  one, include it as is. Given
#  Input: dict_a = {'a': 10, 'b': 20} 
#  dict_b = {'b': 5, 'c': 15} 
# Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}
a = {'a': 10, 'b': 20} 
b = {'b': 5, 'c': 15} 
c={}
for k,v in a.items():
    c[k]=v
for k,v in b.items():
    if k in c:
        c[k]=c[k]+v #or c[k]+=v
    else:
        c[k]=v 
print(c)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'b': 4, 'c': 5, 'd': 6}
c = {}
for k,v in a.items():
    found=False
    for ke,va in b.items():
        if k==ke:
            c[k]=v+va
            found=True
            break
            print("in if:",c)
    if not found:
        c[k]=v
for ke,va in b.items():
    if ke not in c:
        c[ke] = va
print(c)

#Exercise 3: Frequency Map with Counter
text = "Python programming"
freq={}
for i in text:
    freq[i]=freq.get(i,0)+1
print(freq)
 #other way
text = "Python programming"    
from collections import Counter
count=Counter(text)
print(count) 
# Exercise 4: Anagram Checker
# Write a function that determines if two strings are anagrams (contain the exact same characters in a different order). 
# Given Input: word1 = "listen", word2 = "silent" 
# Expected Output: Is "listen" an anagram of "silent"? True
 
def isanagram(word1:str,word2:str)->bool: 
    if sorted(word1.upper())==sorted(word2.upper()):
        return True
    else:
        return False
            
w1 = "listen"
w2 = "silent"
print(isanagram(w1,w2))
#other way
from collections import Counter
def isana(w1,w2):
    if Counter(w1)!=Counter(w2):
        return False
    else:
        return True
word1 = "listen"
word2 = "silent" 
print(f"is {word1} is an anagram of {word2}",isana(word1,word2))

#Exercise 5: Flatten a Nested List
# Write a recursive function that takes a list containing other lists (of any depth)
# and returns a single “flat” list of all elements.
# Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]
# Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]
def flatten(li):
    li2=[]
    for i in li:
        if isinstance(i,list):
            li2.extend(flatten(i))
        else:
            li2.append(i)
    return li2
lis=[1, [2, 3], [4, [5, 6]], 7]
print(flatten(lis))
#Exercise 6: Reverse Each Word of a String
# Given a sentence, reverse each individual word within
# the string while maintaining the original word order.
#  Given Input: "Python is awesome" 
# Expected Output: "nohtyP si emosewa"
text= "Python is awesome"
temp=" "
for word in text.split():
    temp+=word[::-1]+" "

print(temp)
print(text)
# Exercise 7: Palindrome Sentence
# Write a function to check if a full sentence is a palindrome.
# You must ignore case, spaces, and all punctuation marks.
# Given Input: "A man, a plan, a canal: Panama" 
# Expected Output: True
def ispali(w):
    temp=""

    for ch in w:
        if ch.isalpha():
            temp+=ch.lower()
    return temp==temp[::-1]

text = "A man, a plan, a canal: Panama"
print(ispali(text))
print("hi")
# Exercise 8: List Comprehension Filtering (Advanced)
# Given a list of strings, use a single list comprehension to extract stringsthat meet 2 criteria
# : they must be longer than 5 charactersAND they must start with a vowel (a, e, i, o, u).
#  Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]
# Expected Output: ['education', 'umbrella']
text=["apple", "education", "ice", "ocean", "python", "umbrella"]
vowels = {"a", "e", "i", "o", "u"}
result = [ word  for word in text if len(word) > 5 and word[0].lower() in vowels]
print(result)
#another way
text=["apple", "education", "ice", "ocean", "python", "umbrella"]
vowels=['a','e','i','o','u']
temp=[]
for word in text:
    if word[0] in vowels and len(word)>5:
        temp.append(word)
print(temp)

# Exercise 9: Remove Duplicates (Preserving Order)
# Write a function that removes duplicate elements from a list. 
# You cannot use set() because sets do not maintain the original order of elements.
# Given Input: [1, 2, 2, 3, 1, 4, 2] Expected Output: [1, 2, 3, 4]
li=[1, 2, 2, 3, 1, 4, 2] 
l2=[]
for i in li:
    if i not in l2:
        l2.append(i)
print(l2)
# Exercise 10: Circular Shift (Rotation) Create a function rotate_list(lst, n, direction)
# that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.
# Given Input: List: [1, 2, 3, 4, 5], Shift: 2, Direction: 'right' 
# Expected Output: [4, 5, 1, 2, 3]
def rotate(lst,n,dir):
    if dir=='left':
        while(n>=0):
            first=lst[0]
            for i in range(len(lst)-1):
                lst[i]=lst[i+1]
            lst[-1]=first
            n=n-1
        return lst
    elif dir=='right':
        while(n>=0):
            last=lst[-1]
            for i in range(len(lst)-1,0,-1):
                lst[i]=lst[i-1]
            lst[0]=last
            n=n-1
        return lst

l=[1,2,3,4,5]
print(rotate(l,2,'left'))
l=[1,2,3,4,5,6]
print(rotate(l,2,'right'))
print(l)
# Exercise 11: Dictionary Merging (Value Grouping)
# Merge two dictionaries. If they share a key, the new dictionary should store a list 
# containing values from both dictionaries instead of overwriting the first one.
# Given Input: d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4}
# Expected Output: {'a': [1], 'b': [2, 3], 'c': [4]}
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
c={}
for k,v in d1.items():
    c[k]=[v]
for k,v in d2.items():
    if k in c:
        c[k].append(v)
    else:
        c[k]=[v]
print(c)
#other way
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
c={}
for d in (d1,d2):
    for k,v in d.items():
        c[k]=c.get(k,[])+[v]
print(c)

# Exercise 12: Inverted Index 
# Create a function that “inverts” a dictionary.
# Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author 
# i/p = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]} 
# o/p = {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}
d= {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]} 
c={}
for k,v in d.items():
    if isinstance(v,(list,dict)):
        for j in v:
            c[j]=k
    else:
        c[v]=k
print(c)
#other way
d = {"Orwell": {"1984", "Animal Farm"}, "Huxley": {"Brave New World"}}
c1={}
for k, v in d.items():
    for val in v:
        c1[val]=k
print(c1)
# Exercise 13: Dictionary Sorting (Lambda)
# Given a list of dictionaries (representing employees), sort them based on 
# their “salary” in descending order using a lambda function.
# Input: employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]
# Output: [{'name': 'B', 'salary': 70}, {'name': 'C', 'salary': 60}, {'name': 'A', 'salary': 50}]

emp=[{"name": "A","salary":50},{"name": "B", "salary":70},{"name": "C", "salary":60}]
#for i in emp:
temp=[]
first=emp[0]
for i in range(len(emp)-1):
    for j in range(len(emp)-1-i):
        if emp[j]["salary"]>emp[j+1]["salary"]:
            temp=emp[j]
            emp[j]=emp[j+1]
            emp[j+1]=temp

print(emp)
# Exercise 14: Subset and Superset Validation
# Write a script that takes two lists of integers from a user, converts them to sets,
# and determines if the first set is aSubset, a Superset, or Disjoint from the second.
# Given Input: Set A: {1, 2, 3}, Set B: {1, 2, 3, 4, 5} 
# Expected Output: Set A is a subset of Set B.
def check(a,b):
    if a.isdisjoint(b):
        print(f"{a} is disjoint from second {b}")
    elif a.issuperset(b):
        print(f"{a} is superset of {b}")
    elif a.issubset(b):
        print(f"{a} is subset of {b}")

#a1=set(list(map(int,input("enter list of numbers:").split(","))))
#b1=set(list(map(int,input("enter list of numbers:").split(","))))
#check(a1,b1)

# Exercise 15: Set Symmetric Difference 
# Given two lists of student IDs, find the IDs 
# that appear in either the first or the second list, but not in both.
# Given Input: list1 = [101, 102, 103], list2 = [103,104, 105] 
# Expected Output: {101, 102, 104, 105}
a=set([101, 102, 103])
b=[103,104, 105] 
print(a.symmetric_difference(b))


# Exercise 16: Power Set Generation 
# Write a function that generates the Power Set of a given set
# (a set of all possible subsets, including the empty set and the set itself)
# Given Input: [1, 2, 3] 
# Expected Output: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
def power_set(lst):
    if len(lst) == 0:
        return [[]]
    first = lst[0]
    rest = power_set(lst[1:])
    return rest + [[first] + subset for subset in rest]

s = [1, 2, 3]
print(power_set(s))
#other way
def powerset(lst):
    n=len(lst)
    for i in range(2 ** n):
        subset=[]
        for j in range(n):
            if i&(1<<j):
                subset.append(lst[j])

        print(subset)


powerset([1, 2, 3])
l=[1,2,3]



# Exercise 17: Age Calculator (Exact)
# Given Input: Birthdate: 1995-05-15, Today: 2026-01-02
# Expected Output: Age: 30 years, 7 months, 18 days 
from datetime import date
birth=date(1995,5,15)
today=date(2026,1,2)
years=today.year-birth.year
months=today.month-birth.month
days=today.day-birth.day

if days<0:
    months=months-1
    days=days+31
if months<0:
    years=years-1
    months+=12
print(f"Age: {years} years,{months} months, {days} days old")

# Exercise 18: Countdown Timer (Time Delta)
# Write a function that calculates the exact number of days, hours, and minutes 
# remaining until the upcoming New Year’s Day. Given Input: Current Date: 2026-01-02 
# Expected Output: 363 days, 16 hours, 50 minutes until New Year!

from datetime import datetime
d=datetime(2026,1,2,11,30,30)
n_year=datetime(2027,1,1)
rem=n_year-d

days = rem.days
hours = rem.seconds // 3600
minutes = (hours % 3600) // 60

print(f"{days} days, {hours} hours, {minutes} minutes till new year")



# Exercise 19: Business Days Calculator 
# Create a function that takes a start date and an integer N, then calculates the date 
# exactly N business days (Monday–Friday) in the future. Start: Friday, 2026-01-02,
#  Days to add: 5
'''import datetime
def add
d=date(2026,1,30)
today=date(2026,)'''

# Exercise 20: Custom Iterator Class
# Create a class PowerOfTwo that allows you to iterate through powers of 2 (1, 2, 4, 8…)                                                                           
# up to a specified maximum exponent.
# Given Input: powers = PowerOfTwo(3) Expected Output: 1 2 4 8
'''def powerof2(num):
    result=[]
    for i in range(num+1):
        result.extend([2**i])
    return result
print("powers of 2 upto given num",powerof2(3))'''

# # Exercise 21: Find Duplicates in O(n) Time
# # Write a function that identifies all duplicate elements in a list. The solution must 
# # run in linear time, meaning you should only traverse the list once.
# # Given Input: numbers = [1, 2, 3, 2, 4, 5, 1, 6]
# # Expected Output: Duplicates found: {1, 2}
'''from collections import Counter
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
count = Counter(numbers)
dups= {num for num, freq in count.items() if freq > 1}

print(dups)
# other way
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
'''
# # Exercise 22: Singly Linked List Implementation
# # Create a basic Node class and a LinkedList class. Implement a method to append a new 
# # node to the end of the list and a method to display the list.
# # Given Input: List operations: Append 10, Append 20, Append 30
# # Expected Output: 10 -> 20 -> 30 -> None


# # Exercise 23: Stack Implementation (LIFO)
# # Implement a Stack data structure using a Python list. Create methods for push (add),
# # pop (remove), and peek (view top element).
# # Given Input: Push: "google.com", "pynative.com" | Action: Pop 
# # expected output:Current Top: pynative.com Popped: pynative.com New Top: google.com


# # Exercise 24: Queue Implementation (FIFO) 
# # Implement a Queue data structure using collections.deque. Create methods for enqueue
# # (add to back) and dequeue (remove from front). Enqueue: "Customer A", "Customer B" 
# # Action: Dequeue expected o/p Serving: Customer A Next in line: Customer B

# # Exercise 25: Recursive Binary Search 
# # Implement the Binary Search algorithm recursively 
# # to find a target value in a sorted list. 
# # Given Input: Sorted List: [10, 20, 30, 40, 50, 60], Target: 50 
# # Expected Output: Target found at index: 4
'''
def binary_search(lst, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2

    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_search(lst, left, mid - 1, target)
    else:
        return binary_search(lst, mid + 1, right, target)


numbers = [10, 20, 30, 40, 50, 60]
target = 50
index = binary_search(numbers, 0, len(numbers)-1, target)
print(index)'''
# Exercise 26: Lambda Sorting with Tuples 
# Given a list of tuples representing employees (Name,Age,Salary),
#  sort the list primarily by Salary in descending order.
# Given Input: employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]
# Expected Output: [('Bob', 25, 75000), ('Charlie', 35, 60000), ('Alice', 30, 50000)]
emp = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]
emp.sort(key=lambda x:x[2],reverse=True) 
print(emp)
#other way
emp = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]
sorted_emp = sorted(emp, key=lambda x: x[2], reverse=True)
print(sorted_emp)



# Exercise 27: Map and Filter Combination 
# Given a list of numbers, use map() and filter() together to create a list of the
# squares of only the even numbers. 
# Given Input: nums = [1, 2, 3, 4, 5, 6] Expected Output: [4, 16, 36]
nums = [1, 2, 3, 4, 5, 6] 
l=list(map(lambda x:x**2,
    filter(lambda x:x%2==0,nums)))
print(l)

# # Exercise 28: Custom @timer Decorator 
# # Write a decorator function named @timer that prints how many seconds a function takes 
# # to execute. Apply it to a function that simulates a heavy computation using time.sleep().
# # Given Input: A function waste_time() that sleeps for 1.5 seconds. 
# # Expected Output: Function 'waste_time' took 1.5023 seconds to run.

# def greet():
#     print("hello")
# greet()

# x=greet
# x()

# def greet():
#     print("hello")
# def display(func): # func is like a keyword here and also used pass another fun as arguement
#     func()          # now see here func()==greet()
# display(greet)  #display is fun greet ia also fun but given as arg


# def myfstdec(func):# func is nothing but hello()fun it is dec trying to decorate  hello fun with wrapper fun changing code in wrapper 
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper

    
# # def hello():
# #     print("Hello")
# # hello =myfstdec(hello)# instead of writing this we can use @myfstdec
# @myfstdec
# def hello():
#     print("hello")
# @myfstdec
# def greet():
#     print("good morning")
# greet()
# hello()

# def upperr(func):
#     def wrapp():
#         text=func()
#         print("code got changed")
#         return text.upper()
#     return wrapp
# @upperr
# def hello():
#     return "hello world"
# print(hello())
# Exercise 29: Fibonacci Generator (Memory Efficiency) 
# Create a generator function that yields Fibonacci numbers up to N. 
# Instead of returning a full list, it should yield values one by one.
# Given Input: n = 8 Expected Output: First 8 Fibonacci numbers: 0 1 1 2 3 5 8 13
    
# Exercise 30: Custom Context Manager ( with statement)
# Write a class that acts as a context manager for handling a database-style connection 
# (Don’t do actual database connection, simply printing “Connected” and “Disconnected”).
# Use the with statement to ensure the connection is closed even if an error occurs.
# Given Input: A block of code inside a with statement that might raise an Exception.
# Expected Output: Connecting to Database... Processing data... Error: something went
# wrong Closing Database Connection safely.

# Exercise 31: The Versatile *args and **kwargs
# Create a “Logger” function that accepts a mandatory message string, followed by an
# unknown number of positional arguments (*args), and an unknown number of keyword
# arguments (**kwargs).The function should print the message, then list the extra 
# arguments and metadata.
# Input:log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
# Output:Event: User Login Details: ('admin', 'dashboard') Metadata: {'timestamp': '10:00 AM', 'status': 'Success'}
def logger_details(message,*args,**kwargs):
    print(f"{message} : {args} Metadata:{kwargs}")

logger_details("User Login Details","admin", "dashboard",timestamp="10:00 AM",status="success")

# Exercise 32: Zip and Enumerate Mapping
# You have two separate lists: one of student names and one of their exam scores.
# Use zip() to combine them into a dictionary, then use enumerate() to print a ranked 
# list (1st, 2nd, 3rd…).
# Given Input: names = ["Alice", "Bob", "Charlie"] scores = [85, 92, 78] 
# Expected Output: Rank 1: Bob scored 92 Rank 2: Alice scored 85 Rank 3: Charlie scored 78
'''names=["Alice","Bob","Charlie"]
scores=[85,92,78]
li=list((zip(names,scores)))
#print(li)
for i in range(len(li)-1):
    if li[i][1]<li[i+1][1]:
        li[i+1],li[i]=li[i],li[i+1]
#print(li)
#enumerate("Rank 1", "Rank 2","Rank 3")
for i in range(len(li)):
    print(f"Rank {(i+1)}: {li[i][0]} scored {li[i][1]}")'''
names=["Alice","Bob","Charlie"]
scores=[85,92,78]
li=list((zip(names,scores)))
#print(li)
for i in range(len(li)-1):
    if li[i][1]<li[i+1][1]:
        li[i+1],li[i]=li[i],li[i+1]
for rank,(name,score) in enumerate(li,start=1):
    print(f"Rank {rank}: {name} scored {score}")

# Exercise 33: Memorization with lru_cache
from functools import lru_cache
@lru_cache
def fib(n):
    if n<2:
        return n
    else:
        return(fib(n-1)+fib(n-2))
    
print(f"fibonacci of last occu {fib(50)}")


# Exercise 34: Set Operations for Data Analysis
# Given Input: trial = [1, 2, 3, 4, 5] paid = [4, 5, 6, 7, 8] 
# Expected Output:
# Upgraded (Both): {4, 5} 
# Leads (Trial only): {1, 2, 3}
# Unique Status (Not both): {1, 2, 3, 6, 7, 8}
a=set([1, 2, 3, 4, 5]) 
b= set([4, 5, 6, 7, 8])
print(f"Upgraded (Both): {a.intersection(b)}") #or  a&b
print(f"Leads (Trial only): {a.difference(b)}") #or a-b
print(f"Unique status (Not both): {a.symmetric_difference(b)}") #or a^b



# Exercise 35: Inheritance and Method Overriding
# Create a base class Vehicle with an attribute called brand and a method fuel_type().
#  Then,create a subclass ElectricCar that inherits from Vehicle and overrides the
#  fuel_type() method to return “Electricity.” 
# Given Input: car = ElectricCar("Tesla") 
# Expected Output: Brand: Tesla Fuel Type: Electricity
class vehicle:
    def __init__(self, brandd):
        self.brand=brandd
    def fuel_type(self):
        return "unknown"
class electriccar(vehicle):
    def fuel_type(self):
        return "Electricty"
car=electriccar("Tesla")
print(f"Brand: {car.brand}, Fuel_Type: {car.fuel_type()}")



# Exercise 36: Encapsulation (Private Attributes)
# Create a BankAccount class where the balance is a private attribute (cannot be accessed 
# directly from outside the class). Provide deposit and withdraw methods to modify the 
# balance safely. Given Input: account = BankAccount(100) account.deposit(50) account.
# withdraw(200) # This should trigger a warning
# Expected Output: Deposited 50. New Balance: 150 Insufficient funds! Final Balance: 150
''' class bankaccnt:
    def __init__(self,bal):
        self.__balance=bal
    def deposit(self,amt):
        self.__balance+=amt
        print(f"Deposited {amt}. New Balance: {self.__balance}")
    def withdraw(self,amt):
        if amt>self.__balance:
            print("Insufficeint Funds!")
        else:
            self.__balance-=amt
            print(f"Withdraw amt: {amt}, New Balance: {self.__balance}")
    def check(self):
        print("available balance is:",self.__balance)
accnt=bankaccnt(100)
accnt.deposit(100)
accnt.withdraw(50)
accnt.check() '''

class bankaccnt:
    def __init__(self,bal):
        self.__balance=bal
    def deposit(self,amt):
        self.__balance+=amt
        print(f"Deposited {amt}. New Balance: {self.__balance}")
    def withdraw(self,amt):
        try:
            if amt>self.__balance:
                raise ValueError("Insufficeint Funds!")
            else:
                self.__balance-=amt
                print(f"Withdraw amt: {amt}, New Balance: {self.__balance}")
        except Exception as e:
            print("Error: ",e)
             
    def check(self):
        print("available balance is:",self.__balance)
accnt=bankaccnt(100)
accnt.deposit(100)
accnt.withdraw(50)
accnt.check()
# Exercise 37: Property Decorators ( @property ) 
# Create a Student class with a name and a score. 
# Use the @property decorator to create a getter for the score, and a @score.setter
# to ensure that any score assigned is between 0 and 100.
# Given Input: s = Student("Kevin") s.score = 105 # Should trigger a ValueError
# Expected Output: ValueError: Score must be between 0 and 100.

class student:
    name:int
    score:int


# Exercise 38: Class Methods vs. Static Methods Create a class Pizza that has a price 
# attribute. Implement a @classmethod called margherita() that returns a pre-configured
# Pizza object and a @staticmethod called validate_topping() that checks if a topping is 
# “healthy.” 
# Given Input: my_pizza = Pizza.margherita() is_valid = Pizza.validate_topping("pineapple") 
# Expected Output: Pizza ordered: Margherita Is topping valid? True


# Exercise 39: Magic Methods ( __str__ and __add__ ) Create a Point class that represents
#  (x, y) coordinates. Implement __str__ so that printing the object looks like (x,y) and
#  implement __add__ so that p1 + p2 adds the coordinates together.
#  Given Input: p1 = Point(1, 2) p2 = Point(3, 4) print(p1 + p2) Expected Output: (4, 6)


# Exercise 40: Abstract Base Classes (ABC) Create an abstract base class Shape with an
# abstract method area(). Then, implement two subclasses, Circle and Square, that provide
# the actual logic for calculating their respective areas.
# Given Input: shapes = [Circle(5), Square(4)] Expected Output: Circle Area: 78.54 Square Area: 16


# Exercise 41: Multiple Inheritance and MRO Create two classes, Flyer (with a fly()
# method) and Swimmer (with a swim() method). Create a Duck class that inherits from both.
# Use the __mro__ attribute to inspect the search order.Given Input: d = Duck() d.fly() d.swim()
# Expected Output: Flying high! Swimming fast! MRO: (<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)


# Exercise 42: Composition over Inheritance Build a Computer class that is “composed” 
# of a CPU object and a RAM object, rather than inheriting from them 
# Given Input: my_comp = Computer("Intel i7", "16GB") 
# Expected Output: Computer with Intel i7 CPU and 16GB RAM..


# Exercise 43: The Singleton Pattern Implement a Database class that ensures only one
#  instance of itself can ever exist. If a user tries to create a second instance, it
#  should return the first one created.
#  Given Input: db1 = Database() db2 = Database() print(db1 is db2) 
# Expected Output: Loading Database... True (Both variables point to the same memory address)


# Exercise 44: Data Classes ( @dataclass ) Refactor a standard Book class (with title, 
# author, and pages) into a dataclass. Show how it automatically handles __init__ and __repr__.
# Given Input: b1 = Book("1984", "George Orwell", 328) 
# Expected Output: Book(title='1984', author='George Orwell', pages=328)

# Exercise 45: CSV Processor Write a script that reads a CSV file containing employee
# names and salaries. Calculate the average salary and write the results (Original Data + 
# Average) into a new CSV file. Given Input (data.csv):Name,Salary Alice,50000 Bob,60000 Charlie,70000 
# Expected Output: output.csv: Includes the original data and a final row: Average,60000.0.


# Exercise 46: JSON Parser and Nested Access Given a JSON string representing a user
# profile with nested settings, parse the string and safely update a specific nested 
# value (e.g., changing the “theme” from “light” to “dark”).
# Given Input: user_json = '{"id": 1, "profile": {"name": "Alice", "settings": {"theme": "light"}}}'
# Expected Output: Updated JSON: {"id": 1, "profile": {"name": "Alice", "settings": {"theme": "dark"}}}


# Exercise 47: Regular Expressions (Email Extractor) Write a script that takes a long
# block of messy text and extracts all valid email addresses using the re module.
# Given Input: text = "Contact us at support@company.com or sales.dept@office.org for help." 
# Expected Output: ['support@company.com', 'sales.dept@office.org']



#  Exercise 48: Robust Error Handling (Try/Except/Finally) Write a function divide_numbers
# (a, b) that handles ZeroDivisionError and TypeError (if the user passes a string).
# Use a finally block to print “Operation complete” regardless of the outcome. 
# Given Input: divide_numbers(10, 2) divide_numbers(10, 0) divide_numbers(10, "apple") 
# Expected Output: Result: 5.0 Operation complete. --------------------
# Error: Cannot divide by zero! Operation complete. --------------------
# Error: Please provide numbers (integers or floats). Operation complete.


# Exercise 49: OS Module (File Searcher) Write a function that walks through a directory
# and all of its subdirectories, printing the full path of every .txt file it finds.
# Given Input: A root directory name. 
# Expected Output: Found: /Users/name/Documents/notes.txt Found: /Users/name/Documents/Work/todo.txt


# Exercise 50: Multi-threading (Concurrency) Use the threading module to run two functions
# simultaneously. One function should “Download File A” and the other “Download File B” 
# (using time.sleep to simulate the delay). Given Input: Two tasks taking 2 seconds each.
# Expected Output: Total time taken: 2 seconds (instead of 4 seconds).