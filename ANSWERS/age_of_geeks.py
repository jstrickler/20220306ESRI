#!/usr/bin/env python
# (c)2015 John Strickler
from datetime import datetime
import openpyxl as px

wb = px.load_workbook('../DATA/computer_people.xlsx')

ws = wb['people']

age_total = 0
num_people = 0

today = datetime.now()

for row in ws['A2:D9']:
    birthday = row[3].value
    age = (today - birthday).days // 365
    #  print(age)
    age_total += age
    num_people += 1

avg_age = age_total/num_people
print(("Average age is {}".format(avg_age)))
