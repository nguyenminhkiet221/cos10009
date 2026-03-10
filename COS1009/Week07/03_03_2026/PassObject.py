# number is unchanged after being passed into a function
def change(x):
    x = 10
    print(f"Inside function: {x}")
a = 5
change(a)
print(a)

# list is mutable, so it can be changed inside a function
def change_list(lst):
    lst.append(4)
    print(f"Inside function: {lst}")
my_list = [1, 2, 3]
change_list(my_list)
print(my_list)

