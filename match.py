#match statement 
d = int(input("enter day:"))

match d:
    case 1:
        print("monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("enter valid day.")

match d:
    case 1|2|3|4|5:
        print("It's weekday.")
    case 6|7:
        print("it's weekend.")