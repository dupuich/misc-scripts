
def basic_decline_counts(fname):
    fhand = open(fname)

    firstline = True
    declines_ooa = 0
    declines_other = 0

    for line in fhand:

        # skip first line
        if firstline:    
            firstline = False
            continue

        # prepare line for loop
        line = line.strip()
        line = line.split(',')

        # count out of area declines
        reason = line[6]
        if reason.startswith('Outside'):
        	declines_ooa += 1
        else:
        	declines_other += 1

    return (declines_ooa, declines_other)


def oad_per_100_docs_queued(ms,declines):
    ms_queued = ms
    dec_per_100 = float(declines)/ms_queued * 100
    return dec_per_100


def six_or_more(fname):
    firstline = True
    paper_dictionary = {}
    count_six_plus = 0

    fhand = open(fname)
    for line in fhand:
    
        #skip first line
        if firstline:    
            firstline = False
            continue
        line = line.strip()
        line = line.split(',')
    
        # test for out of area declines
        reason = line[6]
        if reason.startswith('Outside') == False:
            continue

        # count out of area declines
        if line[0] not in paper_dictionary:
            paper_dictionary[line[0]] = 1
        else:
            paper_dictionary[line[0]] += 1

    # count papers with more than 5 out of area declines
    for paper in paper_dictionary:
        if paper_dictionary[paper] > 5:
            count_six_plus += 1
    
    evaluated = len(paper_dictionary)
    return(count_six_plus, evaluated)


def decline_report(fname, oname):
    import csv

    firstline = True
    editor_dictionary = {}
    count_six_plus = 0
    li = list()

    fhand = open(fname)
    for line in fhand:
    
        #skip first line
        if firstline:    
            firstline = False
            continue
        line = line.strip()
        line = line.split(',')

        # test for out of area declines
        reason = line[6]
        if reason.startswith('Outside') == False:
            continue

        # get counts of out of area declines per editor
        ed_name = line[2] + ' ' + line[3]
        if ed_name not in editor_dictionary:
            editor_dictionary[ed_name] = 1
        else:
            editor_dictionary[ed_name] += 1

    # sort descending
    for k, v in editor_dictionary.items():
        # print v,k
        li.append((v, k))
    li.sort(reverse = True)

    # write csv
    if len(oname) > 2:
        line = list()
        with open(oname, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Manuscripts'])
            for v,k in li:
                writer.writerow([k, v])

