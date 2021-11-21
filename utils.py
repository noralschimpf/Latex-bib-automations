import csv

def writelist(name: str, arr: list):
    wfile = open("{}.txt".format(name), 'w')
    wcsv = csv.writer(wfile, delimiter=',')
    wcsv.writerow(arr)


def readList(filename: str):
    rfile = open(filename, 'r')
    rcsv = csv.reader(rfile, delimiter=',')
    for row in rcsv:
        arr = row
    return arr

def str_list(string: str, delim=', '):
    outlist = []
    # if string.count(delim) == 0: outlist.append(string)
    for i in range(string.count(delim)):
        part = string.partition(delim)
        outlist.append(part[0])
        string = part[-1]
    outlist.append(string)
    return outlist

def dic_cite(dic: dict, filename: str):
    with open("{}.txt".format(filename), 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for key in dic:
            writer.writerow([key])
            writer.writerow(["\cite{{{}}}".format(x) for x in dic[key]])


