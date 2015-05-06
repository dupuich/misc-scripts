'''
Report Reader: top-30

Provides counts and percentages for items grouped by their values:
1-3
4-6
7-30
sum (1-30)
'''

print
fdate = raw_input('Enter date (mmyy): ')
mypath = '../data/raptor_data/' + fdate + '_queues.csv'
import csv
with open(mypath, 'rU') as f:
    reader = csv.reader(f)
    
    count_total = 0
    count_first_3 = 0
    count_second_3 = 0
    count_rest = 0
    count_30s = 0
    count_40s = 0
    count_100s = 0
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
        if frows in range(1 , 4):
            count_first_3 += 1
        if frows in range(4 , 7):
            count_second_3 += 1
        if frows in range(7 , 31):
            count_rest += 1
        if frows in range(31 , 39):
            count_30s += 1
        if frows in range(39 , 51):
            count_40s += 1
        if frows in range(51 , 150):
            count_100s += 1

# print 'Total 1-3: ', count_first_3
# print 'Total 4-6: ', count_second_3
# print 'Total 7-30: ', count_rest
# print 'Total: ', count_total

print 
print 'Percent for top 3:', float(count_first_3) / (count_total)
print 'Percent for 4-6:', float(count_second_3) / (count_total)
print 'Percent for 7-30:', float(count_rest) / (count_total)
print 'Percent top 30', (count_first_3 + count_second_3 + count_rest) / float(count_total)
print 'Percent 31-38', float(count_30s) / (count_total)
print 'Percent 39-50', float(count_40s) / (count_total)
print 'Percent 51-150', float(count_100s) / (count_total)
print