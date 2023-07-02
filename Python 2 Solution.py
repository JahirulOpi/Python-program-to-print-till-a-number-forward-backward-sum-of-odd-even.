n = int(input("Enter a number "))

print("Numbers Forward:")

def forward(n):
    for x in range (1, n+1):
        print(x, end = " ")
    return n

forward(n)

print()
print("Numbers Backward:")


def backward(n):
    for x in range (n, 1-1, -1):
        print(x, end = " ")
    return n
backward(n)
    
print()
print("Sum of Odd Numbers:")


sum = 0
for x in range (1, n+1, 2):
    sum = sum + x

print(sum)


print("Sum of Even Numbers:")

sum = 0
for x in range (0, n+1, 2):
    sum = sum + x
   
print(sum)
