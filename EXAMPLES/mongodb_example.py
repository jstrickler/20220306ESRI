#!/usr/bin/env python
import re
from pymongo import MongoClient, errors

FIELD_NAMES = (
    'termnumber lastname firstname '
    'birthdate '
    'deathdate birthplace birthstate '
    'termstartdate '
    'termenddate '
    'party'
).split()  # <1>

mc = MongoClient()  # <2>

try:
    mc.drop_database("presidents")  # <3>
except errors.PyMongoError as err:
    print(err)

db = mc["presidents"]  # <4>

coll = db.presidents  # <5>

with open('../DATA/presidents.txt') as presidents_in:  # <6>
    for line in presidents_in:
        flds = line[:-1].split(':')
        kvpairs = zip(FIELD_NAMES, flds)
        record_dict = dict(kvpairs)
        coll.insert_one(record_dict)  # <7>

print(db.list_collection_names())  # <8>
print()

abe = coll.find_one({'termnumber': '16'})  # <9>
print(abe, '\n')

for field in FIELD_NAMES:
    print("{0:15s} {1}".format(field.upper(), abe[field]))  # <10>

print('-' * 50)

for president in coll.find():  # <11>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

rx_lastname = re.compile('^roo', re.IGNORECASE)
for president in coll.find({'lastname': rx_lastname}):  # <12>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

for president in coll.find({"birthstate": 'Virginia'}):  # <13>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))

print('-' * 50)
print("removing Millard Fillmore")
result = coll.delete_one({'lastname': 'Fillmore'})  # <14>
print(result)
result = coll.delete_one({'lastname': 'Roosevelt'})  # <14>
print(result)
print('-' * 50)


result = coll.delete_one({'lastname': 'Bush'})
print(dir(result))
print()

result = coll.count_documents({})  # <15>
print(result)


for president in coll.find():  # <11>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

animals = db.animals

print(animals, '\n')

animals.insert_one({'name': 'wombat', 'country': 'Australia'})
animals.insert_one({'name': 'ocelot', 'country': 'Mexico'})
animals.insert_one({'name': 'honey badger', 'country': 'Iran'})

for doc in animals.find():
    print(doc['name'])
