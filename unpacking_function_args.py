

def greet(greeting, whom):
    print(f"{greeting}, {whom}")

greet('hello', 'world')
greet("hi", 'mom')

data = [('Top of the day', 'old chum'), ('Yippecayay', 'partner'), ('howdy', 'friend')]

for d in data:
    greet(*d)




