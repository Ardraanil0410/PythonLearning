my_list=[7,34,35]
my_tuple = (10,20,30)
my_set={40,50,60}

my_set.add(29)
print(my_set)

my_list.append(44)
my_list.extend([50,60])
my_list.insert(1,25)

print(my_list)

my_tuple=my_tuple+(4,5)
print(my_tuple)

new_tuple=list(my_tuple)
new_tuple.append(27)
print(new_tuple)
my_tuple=tuple(new_tuple)
print(my_tuple)

