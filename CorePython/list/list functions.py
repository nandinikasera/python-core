list1=[1,2,'a',True,'abc',"helo"]
list2=[3,4,5,'b',"nandini"]
list=[3,7,5,88,77,45,65,9,0]

#slicing of list
list3=list1[2:5]
print(list3)

#merge list
list4=list1+list2
print(list4)

#delete list
del list1[2]
print(list1)

#lenth of list
print(len(list1))

#append
list1.append(23)
print(list1)

#count
print(list1.count(23))

#index
print(list1.index(23))

#insert
list1.insert(5,'a')
print(list1)

#remove
list1.remove(23)
print(list1)

#sort
list.sort()
print(list)
#list1.sort(key='str')
#print(list1)

#max
print(max(list))

#min
print(min(list))


