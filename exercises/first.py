"""
Exercise 1-3
"""

import os
from official_code import survey

def live_birth_count(table):
    counter = 0
    for preg in table.records:
        if preg.outcome == 1:
            counter += 1

    return counter

def partition(table):
    first = survey.Pregnancies()
    other = survey.Pregnancies()

    for preg in table.records:
        if preg.outcome == 1:
            if preg.birthord == 1:
                first.AddRecord(preg)
            else:
                other.AddRecord(preg)

    return first, other

def avg_preg_length(table):
    num_of_weeks = 0.0

    for preg in table.records:
        num_of_weeks = num_of_weeks + preg.prglength

    return num_of_weeks / len(table.records)


# 1
table = survey.Pregnancies()
table.ReadRecords(os.path.join("..", "data"))
print 'Number of pregnancies', len(table.records)

#2
num_of_live_births = live_birth_count(table)
print 'Number of live births', num_of_live_births

#3
first, other = partition(table)
print 'Number of live births for the first', len(first.records)
print 'Number of live births for the others', len(other.records)

#4
first_preg_length  = avg_preg_length(first)
other_preg_length  = avg_preg_length(other)
print 'avg weeks of pregnancy for the first', first_preg_length
print 'avg weeks of pregnancy for the others', other_preg_length

diff_in_days = (first_preg_length - other_preg_length) * 7
print 'diff in days', diff_in_days
print 'diff in hours', diff_in_days * 24

