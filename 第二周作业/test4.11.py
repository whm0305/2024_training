pizzas = ["番茄", "榴莲", "芝士"]
friend_pizzas = pizzas[:]

pizzas.append("牛肉")
friend_pizzas.append("黑椒")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza, end=", ")

print("\n\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza, end=", ")