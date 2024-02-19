result = 0
for a in range(3):
    for b in range(4):
        result += a + b
        print('a = ' + str(a) + ' b = ' + str(b) + ' result = ' + str(result))
        if result > 10:
            break
print(result)

