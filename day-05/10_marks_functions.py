#list and function
def get_Marks():
    marks = []
    mark = int(input("Mark (-1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (or -1 to stop): "))
        
    return marks  
 
def print_List_Size(marks):
     print(f"Our list has {len(marks)} elements")
     
def print_marks(marks):
    for x in range(len(marks)):
        print(f"marks {x+1} is {marks[x]}")
        
def get_sum_of_marks(marks):
    sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    return sum

def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if (current_mark > highest):
            highest = current_mark
    
    print(f"The highest mark is {highest}")
    
menu = "Press 1: Capturing marks\n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: To calculate sum of marks\n"
menu += "Press 4: to find highest mark\n"
menu += "Press -1: To exit\n"

print(menu)
choice = int(input("Make your choice: "))
while choice != -1:
    if choice == 1:
        entered_marks = get_Marks()
        print(entered_marks)
    elif choice == 2:
        print_List_Size(entered_marks)
    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print("Sum of all marks =", calc_sum)
    elif choice == 4:
        determine_highest(entered_marks)
    else:
        print("Not on the menu")
        
    print(menu)
    choice = int(input("Make your choice (-1 to exit):"))
    
    
    
    
    
    
