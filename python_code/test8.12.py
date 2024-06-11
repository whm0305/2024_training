def food_message(*foods):
    for food in foods:
        print(food)

food_message("a")
print("------------------")
food_message('a', "b")
print("------------------")
food_message("a",'b','c')