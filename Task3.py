list = [10,20,4,45,99]
newList = list.copy()
largest = max(newList)
for i in range(len(list)):
    if newList[i] == largest:
        newList.remove(largest)

new = max(newList)
print(new)
