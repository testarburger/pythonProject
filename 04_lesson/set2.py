tuple1=(1, 2, 3, 4, 5, 6, 6)
tuple2=(1, 1, 4, 5, 4, 4, 2)
tuples_to_list= list(tuple1[::2] + tuple2[1::2])
print(tuples_to_list)
list_to_set=set(tuples_to_list)
print(list_to_set)