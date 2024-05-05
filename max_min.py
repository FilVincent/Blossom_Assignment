def minmax(data):
    
    minValue = data[0]
    maxValue = data[0]
    for d in data[1:]:
        minValue = d if d < minValue else minValue
        maxValue = d if d > maxValue else maxValue
    return (minValue,maxValue)

data = [49,67,82,17,50,22,46,23,12]
print(minmax(data))