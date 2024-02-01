l = []
n = int(input("Enter number of elements in the list: "))
print("Enter the elements: ")
for i in range(0, n):
    elms = int(input())
    l.append(elms)
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if l[i] >= l[j]:  
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print("Sorted list:", l)

