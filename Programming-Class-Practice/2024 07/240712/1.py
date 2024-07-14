my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(1)

print(my_set)

another_set = {2,3,4}
union_set = my_set.union(another_set)
print(union_set)

intersection_set = my_set.intersection(another_set)
print(intersection_set)