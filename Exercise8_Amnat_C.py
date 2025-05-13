usernameInput = input("Username :")
passwordInput = input("Password :")
num1 = int(60)
num2 = int(60)
num3 = int(70)
num4 = int(70)
if usernameInput  == "admin"  and passwordInput == "1234":
        print("Welcome to Ticha Kitchen")
        print("1. ข้าวยำไก่แซ่บ = 60 ")
        print("2. ข้าวไก่กรอบซอสน้ำปลา = 60 ")
        print("3. ยำวุ้นเส้น = 70 ")
        print("4. ยำมาม่า = 70 ")
userSelected = int(input("กรุณาเลือกเมนู :  "))
if userSelected == 1:
    howmany = int(input("จำนวน : "))
    cost = num1*howmany
    print("รวมราคา =",cost)
elif userSelected == 2:
    howmany = int(input("จำนวน : "))
    cost = num2 * howmany
    print("รวมราคา =", cost)
elif userSelected == 3:
    howmany = int(input("จำนวน : "))
    cost = num3 * howmany
    print("รวมราคา =", cost)
elif userSelected == 4:
    howmany = int(input("จำนวน : "))
    cost = num4 * howmany
    print("รวมราคา =", cost)





