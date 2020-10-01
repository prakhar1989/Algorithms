def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
                
            
list = [9,5,3,7,1,18,12]
print(bubble_sort(list))
