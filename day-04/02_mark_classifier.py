mark = input("Enter a mark(0 to 100): ")

if mark.isdigit():
        mark = int(mark)
        if mark >= 0 and mark <= 100:
            if mark >= 80:
                print("Outstanding")
            elif mark >= 70 and mark < 80:
                print("Highly Competent")
            elif mark >= 50 and mark < 70:
                print("Competent")
            elif mark >= 40 and mark < 50:
                 print("Not yet competent")
            elif mark >= 30 and mark < 40:
                print("Not Achived")
            else:
                print("Invalid mark")
        else:
            print("Invalid mark")
else:
        print("Invalid entry")
