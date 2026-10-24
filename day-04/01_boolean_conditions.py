mark = int(input("Enter a mark: "))
if mark >= 0 and mark <= 100:
    if mark >= 50 and mark <= 75:
        print("You have Passed")
    elif mark >= 75:
        print("You got Distinction")
    elif mark < 50:
        print("You have Failed")
else:
    print("The mark must be between 0 and 100")
