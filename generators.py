
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

r = reversed(nums)
print("r: {}\n".format(r))

for n in r:
    print(n, end=' ')
print('\n')

print("ROUND TWO:")
for n in r:
    print(n, end=' ')
print("\n")

colors = ['green', 'orange', 'brown']

for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)), '\n\n')

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


fgen = (f.upper() for f in fruits)
print(fgen)
for fruit in fgen:
    print(fruit)
print()
