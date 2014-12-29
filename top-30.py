'''
Report Reader

Provides counts and percentages for items grouped by their values:
1-3
4-6
7-30
sum (1-30)
'''

print
fhand = raw_input('Enter filename: ')
mypath = '../data/raptor_data/' + fhand
import csv
with open(mypath, 'rU') as f:
    reader = csv.reader(f)
    
    count_total = 0
    count_first_3 = 0
    count_second_3 = 0
    count_rest = 0
    firstline = True

    for row in reader:
        if firstline:    #skip first line
            firstline = False
            continue

        # count total rows
        count_total = count_total + 1
        
        # count how many rows fit into each group
        if row[6] == '': continue
        frows = float(row[6])
        if frows in range(1,4):
           count_first_3 += 1
        if frows in range(4,7):
           count_second_3 += 1
        if frows in range(7 , 31):
           count_rest += 1

# print 'Total 1-3: ', count_first_3
# print 'Total 4-6: ', count_second_3
# print 'Total 7-30: ', count_rest
# print 'Total: ', count_total

print 
print 'Percent for top 3:', float(count_first_3) / (count_total)
print 'Percent for 4-6:', float(count_second_3) / (count_total)
print 'Percent for 7-30:', float(count_rest) / (count_total)
print 'Percent top 30', (count_first_3 + count_second_3 + count_rest) / float(count_total)
print