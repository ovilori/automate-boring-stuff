my_list = ['Living', 'should', 'be', 'much', 'more', 'easier']
my_tuple = ('Not', 'a', 'funky', 'friday')
my_string = 'Freaky Saturday'
new_string = my_string[0:] + ' and Sunday' 
print(id(my_list))
print(type(my_list))
print(type(my_tuple))
print(type(my_string))
print(new_string)
list_to_tuple = tuple(my_list)
tuple_to_list = list(my_tuple)
string_to_list = list(my_string)
string_to_tuple = tuple(my_string)
print(list_to_tuple)
print(tuple_to_list)
print(string_to_list)
print(string_to_tuple)
print(type(list_to_tuple))
print(type(tuple_to_list))
print(type(string_to_list))
print(type(string_to_tuple))