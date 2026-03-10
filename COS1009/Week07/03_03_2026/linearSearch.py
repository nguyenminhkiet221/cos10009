list = [1,2,3,4,5,6,7,8,9]
target = 7

def linearSearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
output = linearSearch(list, target)
print(f"Index of target {target}: {output}")

