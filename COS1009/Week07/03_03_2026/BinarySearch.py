list_num = list(range(1, 101))
target_num = int(input("Enter a number to search for: "))

def binarySearch(list_num, target_num):
    u = len(list_num) // 2
    n = len(list_num)
    if list_num[u] == target_num:
        return u
    if list_num[u] < target_num:
        for i in range(u+1,n):
            if list_num[i] == target_num:
                return i
    else:
        for i in range(0, u): 
            if list_num[i] == target_num:
                return i
    return -1
output = binarySearch(list_num, target_num)
print(f"Index of target {target_num}: {output}")

#lỗi_(cần sửa)