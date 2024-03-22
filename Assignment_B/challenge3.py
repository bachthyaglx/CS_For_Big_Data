fruits = ['apple', 'pear', 'orange', 'banana', 'apple']
f1 = sorted(fruits)
print(f"{f1},\n{fruits}")

f2 = fruits.sort()
print(f"{f2},\n{fruits}")

#Sort() in-place, no copy, but sorted(...) return a sorted copy