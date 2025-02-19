# a set is a built-in data structure that represents an unordered collection of unique items 
#sets are - unordered , have unique elements , mutable

set={1,2,3,4}
print(set)

# list = [1,1,5,7,3]
# print(list)

# set2 = set(list)
# print(set2) 


#Functions in set
# remove() function -  remove the element but raises error if element is not present
# set.remove(5)


# discard() function - remove the element if present but does not raises error if element is not present 
# set.discard(3)
# print(set)
# set.discard(7)
# print(set)


# clear() - removes all items
# set.clear()
# print(set)


# len() - length of set
# print(len(set))


#union of set - behaves as an or operator 
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# result = set1.union(set2)  # or set1 | set2
# print(result)  


#intersection of set - behaves as an & operator
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# result = set1.intersection(set2)  # or set1 & set2
# print(result)  


# difference of sets - gives the value in first set but not in second set
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# result = set1.difference(set2)  # or set1 - set2
# print(result)  


# subset and superset - 
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))  
print(set2.issuperset(set1)) 
