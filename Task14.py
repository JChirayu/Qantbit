inp = input('Enter the statement')
setInput = sorted(list(set(inp.split(' '))))
print(setInput)
for item in setInput:
    count = inp.count(item)
    print(f'{item}:{count}')
