value_list = [2,4,6,8,10]
total = 0
for value in value_list:
    total += value
print("The total is : ", total)


def get_values():


    value = []

    again = "y"
    while again.upper() == "y":
        value.append(int(input("Enter a value: ")))
        print("The current total is: ", sum(value))
        again = input("Do you want to enter another value? (y/n): ")

#mutli - list
my_students = [
    ["Ken","21"]
    ["Linh","22"],
    ["Huy","20"]
]
print(my_students[1])
        
