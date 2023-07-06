def fibonacci():
a = 1
yield a
b = 1
yield b
while True:
c = a + b
yield c
a = b
*
b = c
for num in fibonacci():
if num > 50:
break
print(num)