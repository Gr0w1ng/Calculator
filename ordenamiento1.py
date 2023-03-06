array = [3,4,5,2,1]

counter_array = 0
counter = 0
quantity = len(array) - 1
for i in range(0, quantity):
    while counter != quantity:
        if array[counter_array] > array[quantity]:
            helper = array[quantity]
            array[quantity] = array[counter_array]
            array[counter_array] = helper
        else: pass
        quantity -= 1
        if quantity == 0:
            pass
    counter_array += 1
    quantity = len(array) -1
    print(counter_array)    
    print(array)
    
