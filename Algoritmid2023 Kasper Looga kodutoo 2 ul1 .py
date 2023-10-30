loend = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(lst):
    pikkus = len(lst)
    eisort = True
    olek = 0

    while eisort:
        eisort = False
        for olek in range(pikkus - 1):
            if lst[olek] < lst[olek + 1]:
                lst[olek], lst[olek + 1] = lst[olek + 1], lst[olek]
                eisort = True
                print(lst)

bubble_sort(loend)
print(loend)
