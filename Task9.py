
def median(*args):
    sortedInp = sorted(args)
    n = len(sortedInp)

    if n % 2 != 0:
        mid = n//2 
        print(f'Median:{sortedInp[mid]}') 
    
    else:
        mid1 = n//2
        mid2 = mid1 - 1
        mid = (sortedInp[mid1] + sortedInp[mid2]) / 2
        print(f'Median:{mid}') 

def mean(*args):
    n = len(args)
    Mean = sum(args)/n
    print(f'Mean:{Mean}')

def mode(*args):
    newSet = set(args)
    modeList = {}
    for item in newSet:
        count = args.count(item)
        modeList[item] = count
    
    values = list(modeList.values())
    highfreq = max(values)


    for key, value in modeList.items():
        if value == highfreq:
            return print(f'Mode:{key}')

inp = list(map(int, input('Enter digits with space\n').split()))

mean(*inp)
median(*inp)
mode(*inp)
