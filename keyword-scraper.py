from pybtex.database.input import bibtex
import csv, os
import utils as u



file = "SpecShar.bib"
papers_index = []
fh = open(file, 'r')

parser = bibtex.Parser()
bibfile = parser.parse_file(file)
# print(bibfile.entries)

keys = bibfile.entries._keys

solns, techs, apps, systems = [], [], [], []
for key in keys:
    try:
        soln = bibfile.entries[key].fields['solntype']
        soln = u.str_list(soln)
        solns.extend(soln)
    except KeyError:
        pass
    try:
        tech = bibfile.entries[key].fields['technologies']
        tech = u.str_list(tech)
        techs.extend(tech)
    except KeyError:
        pass
    try:
        app = bibfile.entries[key].fields['app']
        app = u.str_list(app)
        apps.extend(app)
    except KeyError:
        pass
    try:
        sys = bibfile.entries[key].fields['systems']
        sys = u.str_list(sys)
        systems.extend(sys)
    except KeyError:
        pass
solns, techs, apps, systems = list(set(solns)), list(set(techs)), list(set(apps)), list(set(systems))

# Save each category to CSV
if not os.path.isdir("Tags"): os.mkdir("Tags")
for name, arr in [('soln',solns), ('tech',tech), ('apps',apps), ('systems',systems)]:
    u.writelist("Tags/{}".format(name), arr)


# Print formatted table of keyword categories
print("Apps{}| Tech{}| Solns{}| Systems{}\r\n{}".format(" "*25, " "*25, " "*24, " "*23, "_"*120))
while max([len(solns), len(techs), len(apps), len(systems)]) > 0:
    soln, tech, app, system = " "*29, " "*29, " "*29, " "*29
    if len(solns) > 0:
        x = solns.pop(0)
        soln = x + soln[len(x):]
    if len(techs) > 0:
        x = techs.pop(0)
        tech = x + tech[len(x):]
    if len(apps) > 0:
        x = apps.pop(0)
        app = x + app[len(x):]
    if len(systems) > 0:
        x = systems.pop(0)
        system = x + system[len(x):]
    print("{}| {}| {}| {}".format(app, tech, soln, system))


