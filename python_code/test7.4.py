active = True

while active:
    prompt = "\nPlease enter the topping:"
    prompt += "\n(Enter 'quit' when you are finished.) >  "
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"{topping} will be added")