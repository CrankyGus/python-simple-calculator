def add(x,y):
    return x+y

def subtact(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("โปรดเลือกการคำนวณ")
print("1.บวก \n 2.ลบ \n 3.คูณ \n 4.หาร")

while True:
    userInput = input("Enter choice (1/2/3/4)")
    if userInput in ("1","2","3","4"):
        firstNum = float(input("ใส่ตัวเลขตัวแรก : "))
        secondNum = float(input("ใส่ตัวเลขตัวที่สอง : "))
        if userInput == "1":
            print("คำตอบคือ",add(firstNum,secondNum))
        elif userInput =="2":
            print("คำตอบคือ",subtact(firstNum,secondNum))
        elif userInput == "3":
            print("คำตอบคือ",multiply(firstNum,secondNum))
        elif userInput =="4":
            print("คำตอบคือ",divide(firstNum,secondNum))
        break
    else:
        print("ลองใหม่อีกครั้ง")