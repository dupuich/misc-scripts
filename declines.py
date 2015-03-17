import get_totals

# get info from user
file_name = raw_input('Enter filename: ')
if len(file_name) < 1:
	file_name = "1114_declines-.csv"
fname = '../data/raptor_data/' + file_name
ms_entered = raw_input('Enter total ms queued (or "Enter" to leave blank): ')
if len(ms_entered) < 1:
    ms_entered = '3283' # number for 11/14
ms = int(ms_entered)
oname = raw_input('Enter name of file to export: ')


# calculate results
a , b = get_totals.basic_decline_counts(fname)
c = get_totals.oad_per_100_docs_queued(ms,a)
d , e , f = get_totals.six_or_more(fname)
get_totals.decline_report(fname, oname)


# print results
print
print 'Total out of area declines: %d' % a
print 'Out of area declines per 100 docs queued: %d' % c
print 'Papers with 6 or more out of area declines: %d of %d evaluated' % (d, e)
if len(oname) > 1:
    print 'File %s created showing declines per editor for the submitted timeframe' % oname
print 'Number of excessive declines (all but declines 1-5 for each manuscript): %d' % f
print 'Percent of declines that are excessive:', float(f)/a
print