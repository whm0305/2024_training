numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("“The first three items in the list are:”")
for number in numbers[:3]:
    print(number, end = " ")

print("\n“Three items from the middle of the list are:”")
for number in numbers[1:4]:
    print(number, end = " ")

print("\n“The last three items in the list are:”")
for number in numbers[-3:]:
    print(number, end = " ")