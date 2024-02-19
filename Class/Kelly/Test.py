stop = 9
total = 0
for number in [2, 6, 2, 3, 7, 2]:
    print(number, end=' ')
    total += number
    if total > stop:
        print('@')
        break
else:
    print(f'| {total}')
print('done')