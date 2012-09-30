import os

__author__ = 'MikeD'

from official_code import survey

table = survey.Pregnancies()
table.ReadRecords(os.path.join("..", "data"))
print 'Number of pregnancies', len(table.records)

