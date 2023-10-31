def fibs(n):
    output = []

    for i in range(n):
        if i >= 2:
            output.append(output[i-2] + output[i-1])
        else:
            output.append(i)
    
    return output

def fibsRec(n):
    if n < 2:
        return n
    else:
        return (fibsRec(n-1) + fibsRec(n-2))
    
def mergeSort(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2

    leftSide = mergeSort(list[mid:])
    rightSide = mergeSort(list[:mid])

    return merge(leftSide, rightSide)

def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while len(left) > left_index and len(right) > right_index:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

print(fibs(8))
print([fibsRec(i) for i in range(8)])

nums = [20, 850, 808, 591, 705, 334, 745, 86, 56, 425, 122, 723, 259, 185, 277, 424, 329, 957, 20, 534, 624,
       142, 364, 176, 750, 31, 601, 216, 136, 40, 938, 850, 446, 849, 787, 485, 379, 256, 90, 155, 247, 632, 
       431, 715, 429, 312, 170, 913, 265, 131, 727, 889, 531, 570, 656, 45, 557, 693, 560, 167, 577, 358, 757, 
       558, 477, 543, 998, 256, 102, 36, 205, 1, 291, 280, 687, 560, 628, 905, 97, 592, 766, 655, 637, 319, 823, 
       856, 372, 806, 58, 565, 793, 706, 424, 293, 284, 438, 315, 220, 668, 313]

print(mergeSort(nums))
  
