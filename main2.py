lower=int(input("enter the lower range: "))
higher=int(input("enter a higher range: "))
count=0

if lower % 2 != 0:
    lower += 1

for i in range(lower, higher+1, 2):
    count += 1

print("Number of even numbers:",count)