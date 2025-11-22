amount = int(input("Enter the amount: "))


note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0


if amount >= 500:
    note500 = amount // 500
    amount = amount % 500
if amount >= 100:
    note100 = amount // 100
    amount = amount % 100
if amount >= 50:
    note50 = amount // 50
    amount = amount % 50
if amount >= 20:
    note20 = amount // 20
    amount = amount % 20
if amount >= 10:
    note10 = amount // 10
    amount = amount % 10
if amount >= 5:
    note5 = amount // 5
    amount = amount % 5
if amount >= 2:
    note2 = amount // 2
    amount = amount % 2
if amount >= 1:
    note1 = amount // 1
    amount = amount % 1
print("note500 -", note500)
print("note100 -", note100)
print("note50  -", note50)
print("note20  -", note20)
print("note10  -", note10)
print("note5   -", note5)
print("note2   -", note2)
print("note1   -", note1)