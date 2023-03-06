array1 = [7, 4, 5 ,1 ,2]

#Ordenamineto de array
print(array1)
if array1[0]> array1[1]:
    helper = array1[0]
    array1[0] = array1[1]
    array1[1] = helper
    
if array1[1] > array1[2]:
    helper = array1[1]
    array1[1] = array1[2]
    array1[2] = helper
    
if array1[2] > array1[3]:
    helper = array1[2]
    array1[2] = array1[3]
    array1[3] = helper
    
if array1[3] > array1[4]:
    helper = array1[3]
    array1[3] = array1[4]
    array1[4] = helper


print(array1)