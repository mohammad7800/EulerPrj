inp = int(input('enter a number: '))
num, num1 = 0, 0
if inp % 2 == 0:
    num, num1 = inp / 2, inp / 2
else:
    num, num1 = int(inp / 2), int(inp / 2) + 1
while all([num >= 0, num1 <= inp]):
    print((num, num1))
    num -= 1
    num1 += 1
