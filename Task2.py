a = open('demo.txt', 'r')

elements = [int(item) for item in a]

print(sum(elements))