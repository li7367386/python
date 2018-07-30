Q = int(input("Order quantity Q: "))  # 一次補貨的量
R = int(input("Recorder point R: "))  # 需捕貨點
I = int(input("Initial inventory I: "))  # 初始存貨
print("Inventory: " + str(I))

while True:
    sales = int(input("Sales in a day: "))
    I = I - sales if I - sales >= 0 else 0
    if I < R:
        I += Q
    print("Inventory: " + str(I))
