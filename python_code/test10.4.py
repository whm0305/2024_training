while True:
    prompt = "please enter your name:"
    prompt += "\nEnter 'q' when you quit > "
    text = input(prompt)
    if text =='q':
        break
    greet = "welcome: " + text + " !\n"
    print(greet)
    with open("guest_book.txt", "a") as fbj:
        fbj.write(greet)