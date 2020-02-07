KSweight = 10
KSvalue = 0
locker = [{'id': 1, 'weight': 3, 'value': 2},
               {'id': 2, 'weight': 2, 'value': 5},
               {'id': 3, 'weight': 1, 'value': 1},
               {'id': 4, 'weight': 2, 'value': 4},
               {'id': 5, 'weight': 5, 'value': 4}]

def packing(size, weight, value):
    new_value = value
    if size < len(locker):
        if weight - locker[size]['weight'] < 0:
            new_value = packing(size + 1, weight, value)
        else:
            new_value = max(packing(size + 1, weight, value), packing(size + 1, weight - locker[size]['weight'],
                                              locker[size]['value']) + value)
    return new_value

print(packing(0,KSweight,KSvalue))