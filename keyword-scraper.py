from pybtex.database.input import bibtex

def str_list(string: str, delim=','):
    outlist = []
    if string.count(delim) == 0: outlist.append(string)
    for i in range(string.count(delim)):
        part = string.partition(delim)
        outlist.append(part[0])
        string = part[-1]
    return outlist

file = "C:/Users/natha/Downloads/SpecShar.bib"
papers_index = []
fh = open(file, 'r')

parser = bibtex.Parser()
bibfile = parser.parse_file(file)
# print(bibfile.entries)

keys = bibfile.entries._keys

solns, techs, apps = [], [], []
for key in keys:
    try:
        soln = bibfile.entries[key].fields['solntype']
        soln = str_list(soln)
        solns.extend(soln)
    except KeyError:
        pass
    try:
        tech = bibfile.entries[key].fields['technologies']
        tech = str_list(tech)
        techs.extend(tech)
    except KeyError:
        pass
    try:
        app = bibfile.entries[key].fields['app']
        app = str_list(app)
        apps.extend(app)
    except KeyError:
        pass
solns, techs, apps = list(set(solns)), list(set(techs)), list(set(apps))
print("Solns: {}\n\rTechs: {}\r\nApps: {}".format(solns, techs, apps))
print("Solns{}| Tech{}| Apps{}\r\n{}".format(" "*24, " "*25, " "*25, "_"*90))
while max([len(solns), len(techs), len(apps)]) > 0:
    soln, tech, app = " "*29, " "*29, " "*29
    if len(solns) > 0:
        x = solns.pop(0)
        soln = x + soln[len(x):]
    if len(techs) > 0:
        x = techs.pop(0)
        tech = x + tech[len(x):]
    if len(apps) > 0:
        x = apps.pop(0)
        app = x + app[len(x):]
    print("{}| {}| {}".format(soln, tech, app))

