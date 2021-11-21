from pybtex.database.input import bibtex
import os, json
import utils as u

file = "SpecShar.bib"
papers_index = []
fh = open(file, 'r')

parser = bibtex.Parser()
bibfile = parser.parse_file(file)
keys = bibfile.entries._keys

headings = u.readList("Tags/apps.txt")
techs = u.readList("Tags/tech.txt")
dict_headings, dict_tech, dict_joint = {}, {}, {}


# GET: references by-application, by-technology, by-application&technology (joint)
for key in keys:
    try:
        app = bibfile.entries[key].fields['app']
        app = u.str_list(app)
        tech = bibfile.entries[key].fields['technologies']
        tech = u.str_list(tech)
        for a in app:
            if a in dict_headings: dict_headings[a].append(key)
            else: dict_headings[a] = [key]
            for t in tech:
                if t in dict_tech: dict_tech[t].append(key)
                else: dict_tech[t] = [key]
                joint = "{}-{}".format(a,t)
                if joint in dict_joint: dict_joint[joint].append(key)
                else: dict_joint[joint] = [key]
    except KeyError:
        pass

if not os.path.isdir("referenceCategories"): os.mkdir("referenceCategories")
for f, dic in [("heading",dict_headings), ("tech", dict_tech), ("joint", dict_joint)]:
    u.dic_cite(dic, "referenceCategories/{}".format(f))
    with open('referenceCategories/{}.json'.format(f), 'w',encoding="utf-8") as file:
        json.dump(dic, file)
