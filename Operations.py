#ASSIGNING ELEMENTS TO DIFFERENT LISTS
print('LISTS:')
list1=[]
list2=[]

n1=int(input('\nEnter the number of elements in the list1:'))
for i in range(0,n1):
    items1=int(input('Enter a list of numbers:'))
    list1.append(items1)
print('list1: ',list1)

n2=int(input('\n\nEnter the number of elements in the list2:'))
for j in range(0,n2):
    items2=int(input('Enter a list of numbers:'))
    list2.append(items2)
print('list2: ',list2)

#ACCESSING ELEMENTS FROM A TUPLE
print('\nTUPLES:')
tuple1=('Tony','Steve','Thor','Loki','Natasha','Bruce')
print('Elements from the tuple are: ',tuple1[0],tuple1[1],tuple1[2],tuple1[3],tuple1[4],tuple1[5])

#DELETING DIFFERENT DICTIONARY ELEMENTS
print('\nDICTIONARY: ')
dict1={'Name':'Anannya','Age':19,'Subjects':['Defence against the dark arts','Potions']}
print('Dictionary: ',dict1)
print('After deleting an element: ')
del dict1['Age']
print('New Dictionary: ',dict1)
