__author__ = 'MikeD'

from official_code import survey

table = survey.Pregnancies()
table.ReadRecords("..\data")
print 'Number of pregnancies', len(table.records)

