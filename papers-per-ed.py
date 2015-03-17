'''
Creates file with key value pairs
(number of editors handling papers each month)

sample data:
date , ID_1 , ID_2 , text, text, num, num, text, name (key)
script counts the instances of row[8] 

'''

import csv

d = dict()           # dictionary for counting occurrences
firstline = True



fdate = raw_input('Enter date (mmyy): ')
# if len(fhand) < 1:
    #fhand = 'default_file.csv'
mypath = '../data/raptor_data/' + fdate + '_queues.csv'
make_report = raw_input("Enter output filename or press 'Enter' ")
#if len(make_report) < 1:
    #make_report = 1

with open(mypath, 'rU') as f:
    reader = csv.reader(f)

    #skip first line
    for row in reader:
        if firstline:    
            firstline = False
            continue

        # get counts of ms per unique value
        if len(row[8]) < 1:
            continue
        if row[8] not in d:
            d[row[8]] = 1
        else:
            d[row[8]] += 1

# number of unique values
print "total rows: ", len(d)

# create csv with key, value
if len(make_report) > 0:
    line = list()
    with open(make_report, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['Key', 'Value'])
        for key, val in d.items():
            writer.writerow([key, val])

        print "file", make_report, "created"