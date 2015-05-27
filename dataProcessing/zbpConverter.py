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
	for yr in key_yr:
		key[yr] = key_yr

def not_in(s, yr1, yr2):
	print "%s not present from %s to %s" % (s, yr1, yr2)
	return ""

def not_in_data(dn):
	print "%s not in concord" % (dn)
	return dn

def get_next_yr(yr):
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
	year, year_goal = key[file_year], key[year_to] # the classification year that each year falls under
	data = pd.read_csv("raw/zbp%sdetail.txt" % str(file_year)[2:]) 
	first = True # b/c first time concord is different
	while year != yearGoal:
		concord_raw = pd.read_csv("%s_%s.csv" % (year, convs[year]), "r")
		keys = list(concord.columns.values) # get column keys
		if first:
			concord = {l[keys[0]]: l[keys[2]] for l in concord_raw.values}
			first = False
		else:
			this_conc = {l[keys[0]]: l[keys[2]] for l in concord.values}
			concord = {k: this_conc[k] if k in this_conc else not_in(k, year, yearGoal) for k in concord} # converts over
		year = get_next_yr(year)
	data["naics"] = pd.Series([concord[l] if l in concord else not_in_data(l) for l in data["naics"]])
	pd.to_csv("converted/zbp%sdetail_conv.txt" % str(file_year)[2:])

if __name__ == "__main__":
	if len(sys.argv) != 5 or len(sys.argv) != 3:
		print "Usage: python zbpConverter.py <two-digit year> [-y] [yearToConvertTo]"
		sys.exit()
	elif not sys.argv[2].isnumeric() or (int(sys.argv[2]) < 0 or (int(sys,argv[2]) > 13 and not int(sys.argv[2]) < 94) or int(sys.argv[2]) > 100):
		print "Invalid year"
		sys.exit()
	year = int(sys.argv[2])
	if len(sys.argv) == 5 and sys.argv[3] == '-y':
		if not sys.argv[4].isnumeric() or (int(sys.argv[3]) < 0 or (int(sys,argv[3]) > 13 and not int(sys.argv[3]) < 94) or int(sys.argv[3]) > 100):
			print "Invalid year to convert to"
			sys.exit()
		convert(year, yearTo=int(sys.argv[4]))
	else:
		convert(year)
