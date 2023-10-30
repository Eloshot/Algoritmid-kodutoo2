def insertion_sort(sort):
    for i in range(1, len(sort)): # alustame teisest elemendist kuna pole motet vorrelda esimest esimesega
        
        
        key = sort[i]
        j = i - 1
        
        while j >= 0 and key < sort[j]:
            sort[j + 1] = sort[j]
            j -= 1
            sort[j + 1] = key
            print(sort)
            
        
        
    
list = [12, 11, 13, 5, 6, 7]
insertion_sort(list)
print(list)