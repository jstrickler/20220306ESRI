import sys

person = "Bilbo Baggins"
city = "The Shire"

value = 42.378302930390293


print(person, city, value)
# output  str(person) + " " str(city) + " " + str(value) + "\n"

print(person, city, value, sep='/')
print(person, city, value, sep='#')
print(person, city, value, sep=' = ')
print(person, city, value, sep='')
print()

print(person, city, end=' ')
if value > 50:
    print('spam', end=' ')
else:
    print("ham", end=' ')

print("foo")


print("HELP HELP HELP", file=sys.stderr)
print()

print("{} lives in {}".format(person, city))
print("{1} lives in {0}".format(person, city))
print("{0} lives in {1} (yes, {0})".format(person, city))


# print("The value is", value)
# print("The value is {}".format(value))

print(f"{person} lives in {city}")

print("value is {:.2f}".format(value))
print(f"value is {value:.2f}")


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
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, _, dob in people:
    print(f"{first_name:8} {last_name:12} {dob}")

