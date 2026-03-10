# ví dụ về vòng lặp trong python
number = 0
while number < 5:
    print(" Hello world")
    number += 1
# in ra các số từ 1 đến 9
for i in [1,3,5,7,9]:
    print(i)
# in ra các số lẻ từ 1 đến 9
for u in range(1,10, 2):
    print(u)
# đếm ngược từ 10 đến 2
for j in range(10,1,-1):
    print(j)
# in ra tất cả các tổ hợp giờ phút giây trong một ngày
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f"(h:{h} m:{m} s:{s})")
#điều kiện số thực hợp lệ để điền điểm từ 0--> 100
num = int(input("Write a score:"))
while num < 0 or num > 100:
    print(" Invalid score, try again.")
    num = int(input("Write a score:"))
print(" Valid score:", num)

# tính tổng các số trong một danh sách
numb = [2,4,6,8,10]
index = 0
total = 0
while index < len(numb):
    total += numb[index]
    index += 1
print(" Total:", total)

# tính điểm trung bình từ một danh sách các số thực
score =[2.5, 8.3, 6.5, 4.0, 5.2]
total = 0.0
index = 0
while index < len(score):
    total += score[index]
    index += 1
average = total / len(score)
print(" Average score:", average)

