

colors = ['red', 'blue', 'green']

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'


print("person[0] {}, person[1]: {}\n".format(person[0], person[1]))


first_name, last_name, product, dob = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))



for person in people:
    # person = people[0]
    # person = people[1]
    # ...
    print(person)
print('-' * 60)


for first_name, last_name, *product, _ in people:
    print(first_name, last_name, product)
print('-' * 60)


v1  = 27
v2 = 5

print("divmod(v1, v2): {}".format(divmod(v1, v2)))

quotient, remainder = divmod(v1, v2)
print("quotient: {}".format(quotient))
print("remainder: {}".format(remainder))


