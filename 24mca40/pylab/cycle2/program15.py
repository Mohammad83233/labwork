my_dict = {'banana': 3, 'cherry': 7, 'orange': 2, 'guava': 4}
keys_asc = dict(sorted(my_dict.items()))
print("Sorted by keys (ascending):", keys_asc)
keys_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by keys (descending):", keys_desc)
values_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values (ascending):", values_asc)
values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by values (descending):", values_desc)
