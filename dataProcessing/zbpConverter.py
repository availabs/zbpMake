import csv, sys, getopt, os.path, json
import pandas as pd

def yrRange(start, finish):
	return [str(yr) for yr in range(start, finish+1)]

convs = {
	"1987": "2002",
	"1997": "2002",
	"2002": "2007",
	"2007": "2012"
}

tabuls = {
	"2012": ["2012"],
	"2007": yrRange(2008, 2011),
	"2002": yrRange(2003, 2007),
	"1997": yrRange(1998, 2002),
	"1987": yrRange(1988, 1997)
}

#key = {yr: keyYear for yr in keyYear for keyYear in tabuls}
key = {}
for key_yr in tabuls:
	for yr in tabuls[key_yr]:
		key[yr] = key_yr

def not_in(s, yr1, yr2):
	# print "%s not present from %s to %s" % (s, yr1, yr2)
	return ""

def not_in_data(dn):
	# print "%s not in concord" % (dn)
	return dn

def get_next_yr(yr):
	if yr in tabuls:
		return get_next_yr(str(int(yr) + 1))
	if yr in tabuls["1987"]:
		return "1997"
	elif yr in tabuls["1997"]:
		return "2002"
	elif yr in tabuls["2002"]:
		return "2007"
	elif yr in tabuls["2007"]:
		return "2012"
	else:
		raise ValueError("get_next_year passed incorrect year of %s" % str(yr))

# somewhat inefficient, but works
def convert(file_year, year_to="2012"):
	year, year_goal = key[str(file_year)], key[year_to] # the classification year that each year falls under
	data = pd.read_csv("raw/zbp%sdetail.txt" % str(file_year)[2:], dtype={"zip": "object"}) 
	first = True # b/c first time concord is different
	while year != year_goal:
		concord_raw = pd.read_csv("../concordances/%s_%s.csv" % (year, convs[year]))
		keys = list(concord_raw.columns.values) # get column keys
		if first:
			concord = {l[0]: l[2] for l in concord_raw.values}
			first = False
		else:
			this_conc = {l[0]: l[2] for l in concord_raw.values}
			concord = {k: this_conc[k] if k in this_conc else not_in(k, year, year_goal) for k in concord} # converts over
		year = get_next_yr(year)
		print year
	data[data.columns.values[2]] = pd.Series([concord[l] if l in concord else not_in_data(l) for l in data[data.columns.values[2]]])
	data.columns.values[2] = "naics"
	data.to_csv("converted/zbp%sdetail_conv.txt" % str(file_year)[2:], index=False)

if __name__ == "__main__":
	if len(sys.argv) != 4 and len(sys.argv) != 2:
		print "Usage: python zbpConverter.py <four-digit year> [-y] [yearToConvertTo]"
		sys.exit()
	year = int(sys.argv[1]) if unicode(sys.argv[1], "utf-8").isnumeric() else -1
	if not (1993 < year < 2014):
		print "Invalid year"
		sys.exit()

	if len(sys.argv) == 4 and sys.argv[2] == '-y':
		year_to = int(sys.argv[3]) if unicode(sys.argv[3], "utf-8").isnumeric() else -1
		if not (1993 < year_to < 2014):
			print "Invalid year to convert to"
			sys.exit()
		convert(year, year_to=int(sys.argv[4]))
	else:
		convert(year)
