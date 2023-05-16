tests = []
tests.append({
    'data': [0, 2, 3, 4, 5],
    'value': 3,
})

tests.append({
    'data': [],
    'value': 0,
})

tests.append({
    'data': [1,2,2,2,2,3,4,5,6],
    'value': 2
})

tests.append({
    'data': [1,2,2,2,2,4,5,6],
    'value': 3
})

tests.append({
    'data': [1,2,2,2,2,3,4,4,5,6,7],
    'value': 7
})

def checkPosition(data, value, mid):
    if mid == 0 or data[mid - 1] < value:
        return mid
    else:
        return "left"

def searchRecursively(data,value,low,high):
    if low > high:
        return -1
    else:
        mid = low + (high-low)//2
        if value == data[mid]:
            position = checkPosition(data,value,mid)
            if position == "left":
                return searchRecursively(data,value,low,mid -1)
            else:
                return position
        elif value > data[mid]:
            return searchRecursively(data,value,mid + 1,high)
        elif value < data[mid]:
            return searchRecursively(data,value,low,mid -1)

def searchBinary(data,value):
    low,high = 0, len(data) - 1
    return searchRecursively(data,value,low,high)

for test in tests:
    print(searchBinary(**test))
    
