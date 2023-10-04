def removeElementInArray(array,elem):
    key = 0
    for i in range(len(array)):
        if (array[i] == elem):
            key = i
            break

    array[key], array[-1] = array[-1], array[key]
    return array.pop()