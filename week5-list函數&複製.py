# list相關函數
list = [3, 1, 4, 1, 5, 9]
list.append(2)  # 最後+數字
print(list)

list.sort()  # 排序小到大
print(list)

list.reverse()  # 排序大到小
print(list)

print(list.index(4))  # index位置的值

list.insert(4, "Hi")  # 位置+值
print(list)

print(list.count(1))  # 有幾個值

list.remove(1)  # 移除值
print(list)

print(list.pop(2))  # 提出()位置的值

print(list)

# single list的兩個名稱
alist = [1, 2, 3]
blist = alist
blist[0] = 5
print(alist)

# list複製
alist = [1, 2, 3]
blist = []
for i in alist:
    blist.append(i)
blist[0] = 5
print(alist)  # [1, 2, 3]
print(blist)  # [5, 2, 3]
