

# print Even Numbers
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i = i + 1
    
    
#Factorial
n = int(input("enter the req number:"))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =" ,factorial)


#
i = 1
while i <= n:
    factorial = factorial * i
    i=i+1

print("factorial =", factorial)


#no of digits in a number







#Palindrome

n = int(input("enter the number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = int(n/10)

if original == reverse:
    print("It is a Palindrome number")
else:
    print("it is not a Palindrome number")
    
#



#Fibonacci Series

n = int(input("enter the number of terms:"))

a = 0
b = 1

for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c
    
#

i = 0
while i < n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1

