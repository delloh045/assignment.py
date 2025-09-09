#Create the list and working up


my_list =[]

for  i in range(10,50,10):

    my_list.append(i)
print(my_list)

my_list.insert(1,15)
print(my_list)

extend_list = [50,60,70]
my_list.extend(extend_list)
print("extend_list")
print(my_list)
my_list.remove(70)
print("remove 70")
print(my_list)

sorted(my_list)
print("sorted list")
print(my_list)

print("find and print index of 30")
print(my_list.index(30))
print(my_list)
