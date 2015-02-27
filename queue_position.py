# reads AE Invitation Queue and creates file with number of ms assigned per queue position

file_name = raw_input('Enter filename: ')
fname = '../data/raptor_data/' + file_name
oname = raw_input('Enter name of file to export: ')

li = list()
q_position_dictionary = {}
fhand = open(fname)

firstline = True
for line in fhand:
    if firstline:    
        firstline = False
        continue

    line = line.split(',')
    if len(line[6]) < 1:
        continue
    ms = int(line[6])
    if ms not in q_position_dictionary:
        q_position_dictionary[ms] = 1
    else:
        q_position_dictionary[ms] += 1
#print q_position_dictionary

for k, v in q_position_dictionary.items():
    li.append((k, v))
    li.sort()

import csv
with open(oname, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['Queue_position', 'Number_of_manuscripts'])
    for k, v in li:
        writer.writerow([k, v])
