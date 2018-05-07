# or邏輯運算
key = input("continuted")
if key == "y" or key == "Y":
    print()
else:
    print()

# not邏輯運算
key = input("continuted")
if not (key == "y" or key == "Y"):
    print("Game over!")

# while迴圈
sum = 0
i = 1
while i <= 100:
    sum = sum + i  # sum+=i
    i = i + 1  # i+=1
print(sum)

#while應用
exit = input("Press y or Y to exit:")
while not (exit == "y" or exit == "Y"):
    exit = input("Press y or Y to exit:")
