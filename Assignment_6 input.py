#1

num=int(input("Enter a number: "))
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
if True:
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")


#2

astr=input("Enter a string: ")
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
if True:
    print(astr,"is a Palindrome.")
else:
    print(astr,"is not a Palindrome.")


#3

from math import factorial
 
n = int(input("Rows: "))
for i in range(n):
    for j in range(n-i+1):
 
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    print()


#4

import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for i in alphabet:
      if i not in str.lower():
         return False
   return True

string = input("Enter a string: ")
if True:
   print("Yes, the given string is a pangram.")
else:
   print("No, the given string is not a pangram")


#5

word=input("Enter hyphen-separated sequence of words : ")
items=[n for n in word.split('-')]
items.sort()
print('-'.join(items))


#6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")

 
student_data(student_id='21107033', student_name='Vaibhav Garg')

student_data(student_id='21107033', student_name='Vaibhav Garg', student_class ='2nd Semester')


#7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 


#8

list=[]
def findTriplets(arr, n):
  
    found = False
    for i in range(0, n-2):
      
        for j in range(i+1, n-1):
          
            for k in range(j+1, n):
              
                if (arr[i] + arr[j] + arr[k] == 0):
                    list.append([arr[i],arr[j],arr[k]])
                    print(list)
                    found = True
      
    if (found == False):
        print(" not exist ")
  
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)


#9

class validity:

    def f(str):

        a= ['()', '{}', '[]'] 

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '') 

        return not str 

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")