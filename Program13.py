while True:
    try:
        print ("enter the integer : ")
        number = int(input())
        if (number % 2) is 0:
            print("number is even\n")
        else:
            print("number is odd\n")
        break

    except NameError:
        print("you cant enter string\n")

    except SyntaxError:
        print("your input is empty or symbol ")












