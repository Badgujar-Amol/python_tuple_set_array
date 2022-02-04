# Accessing tuple value
tup = (10, 20, 30, 40, 50, 60, 70, 80)
print(tup)

# Accessing tuple value
tup1 = (10, 20, 30, 40, 50, 60, 70, 80)
print(tup1[0])
print(tup1[2])
print(tup1[1])
print(tup1[3])
print(tup1[5])
print(tup1[4])


# Accessing tuple negative value
tup2 = (10, 20, 30, 40, 50, 60, 70, 80)
print(tup2[-2])
print(tup2[-1])
print(tup2[-3])
print(tup2[-5])
print(tup2[-4])

# Accessing tuple value in range
tup3 = (10, 20, 30, 40, 50, 60, 70, 80)
print(tup3[2:6])
print(tup3[3:])
print(tup3[:4])

# change tuple value
# tuples are imutable but we can edit tuple using by converting it into list
tup4 = (10, 20, 30, 40, 50, 60, 70, 80)
i = list(tup4)
i[3]=100
print(i)
j = tuple(i)
print(j)

# FETCH TUPLE VALUE WITH FOR LOOP
tup5 = (10, 20, 30, 40, 50, 60, 70, 80)
for i in tup5:
    print(i)

# tuple length
tup6 = (10, 20, 30, 40, 50, 60, 70, 80)
print(len(tup6))

# Delete tuple
tup8 = (10, 20, 30, 40, 50, 60, 70, 80)
print(tup8)
del tup6


# concatinate two tuple
tup9 = (1, 2, 3, 4, 5)
tup10 = (6, 7, 8, 9, 10)
print(tup9 + tup10)