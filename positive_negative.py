list1=[]
list2=[]

n1=int(input('\nEnter the number of elements in the list1:'))
for i in range(0,n1):
    items1=int(input('Enter a list of numbers:'))
    list1.append(items1)

print('\nInput: list1: ',list1)
print('Output:',end=" ")
for i in list1:
    if i>=0 :
        print(i,end=" ")

n2=int(input('\n\nEnter the number of elements in the list2:'))
for j in range(0,n2):
    items2=int(input('Enter a list of numbers:'))
    list2.append(items2)

print('\nInput: list2: ',list2)
print('Output:',end=" ")
for j in list2:
    if j>=0 :
        print(j,end=" ")
