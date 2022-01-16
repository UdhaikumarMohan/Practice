# Set is a collection of unique elements.

s = {22, 25, 14, 21, 54}
s

# In set you can get a same value given

s ={25, 14, 98, 63, 75, 98}
s

# If you repeat value: Look above we get 98 once, but other values are not sorted.
# Set uses the concept of Hash. It improves the performance, here you can understand set is not for the sequence

s[2] 

# Set does not support indexing, because it does not follow sequential.

# add() elements in the set
s.add(6)
s

# To clear the set
s.clear()
s

# Difference is a method returns a set that contains the differece between two sets.
# It returns set that contains items that exists only in the first set, and not in the both sets.

t = {14, 26, 29, 44}

x= s.difference(t)
x

# difference_update() method removes the items from the first set, that exists in both sets.

y = s.difference_update(t)
s

# Discard method is used to remove the items from the set. This method is different form the remove().
# Remove throws error if the specified value does not present in the given set. But discard does not.

s.discard(75)
s
s.discard(100)
s.remove(100)
s

# This method returns a set that contains the similarity between two or more sets.
# The returned set contains the items that exists in both sets, or in all sets if the comparision is done with more sets.

u = {2, 4, 6, 8, 10}
v = {2, 3, 4, 5, 6}

w = u.intersection(v)
w

# intersection update functions only retains the common numbers between the comparing set

u.intersection_update(v)
u

# issubsets() Returns wether another set contains this set in it or not
u = {2, 4, 6, 8, 10}
v = {2, 3, 4, 5, 6}
a = {2, 4, 6, 8, 10, 12}
u.issubset(v)
u.issubset(a)

# issuperset() Returns this set contains the another set or not.
u.issuperset(v)
u.issuperset(a)

# symmentric difference returns the set that only contains different nmbers between two sets.

u.symmetric_difference(v)

# symmeteic differnece update, updates the first set combining two sets without the common numbers between the both sets.
u.symmetric_difference_update(v)
u

# Union fuction update set with another set or any other iterable
u = {2, 4, 6, 8, 10}
v = {2, 3, 4, 5, 6}
u.union(v)

# Update used to update the set with another set or any other iterable.

u.update(v)
u




