import csv, sys, getopt, os.path

def yrRange(start, finish):
	return [str(yr) for yr in range(start, finish+1)]

convs = {
	"1987": "2002",
	"1997": "2002",
	"2002", "2007",
	"2007", "2012"
}

tabuls = {
	"2012": ["2012"],
	"2007": yrRange(2008, 2011),
	"2002": yrRange(2003, 2007),
	"1997": yrRange(1998, 2002),
	"1987": yrRange(1988, 1997)
}

key = {yr: keyYear for yr in keyYear for keyYear in tabuls}

def notIn(s, yr1, yr2):
	print "%s not present from %s to %s" % (s, yr1, yr2)
	return ""

def getNextKeyYear(yr):
	if yr in tabuls["1987"]:
		return "1997"
	elif yr in tabuls["1997"]:
		return "2002"
	elif yr in tabuls["2002"]:
		return "2007"
	elif yr in tabuls["2007"]:
		return "2012"
	else:
		raise ValueError("getNextKeyYear passed incorrect year of %s" % str(yr))

def convert(fileYear, yearTo="2012"):
	year, yearGoal = key[fileYear], key[yearTo]
	with open("zbp%sdetail.txt" % str(fileYear)[2:], "r") as dat:
		dataKeys = dat.readline().replace("\"", "").replace("\n", "").replace("\r", "").split(',')
		dat.seek(0)
		data = list(csv.DictReader(dat))
	first = True 
	while year != yearGoal:
		with open("%s_%s.csv" % (year, convs[year]), 'r') as f:
			#The cols are always oldName, oldDesc, newName, newDesc
			keys = f.readline().split(',')[:4]
			f.seek(0)
			if first:
				concord = {l[keys[0]]: l[keys[2]] for l in list(csv.DictReader(f))} #only change the val, not key
				first = False
			else:
				thisConc = {l[keys[0]]: l[keys[2]] for l in list(csv.DictReader(f))}
				concord = {k: thisConc[k] if k in thisConc else notIn(k, year, yearGoal) for k in concord.keys()}
		year = getNextKeyYear(year)
	with open("zbp%sdetail_conv.txt" % yearTo[2:], "w+") as nF:
		pass #write the data dict, with each naics replaced.

def main():
	pass

if __name__ == "__main__":
	if len(sys,argv) != 5 or len(sys.argv) != 3:
		print "Usage: python zbpConverter.py <two-digit year> [-y] [yearToConvertTo]"
		sys.exit()
	elif not sys.argv[2].isnumeric() or (int(sys.argv[2]) < 0 or (int(sys,argv[2]) > 13 and not int(sys.argv[2]) < 94) or int(sys.argv[2]) > 100):
		print "Invalid year"
		sys.exit()
	year = int(sys.argv[2])
	if len(sys.argv) == 5 and sys.argv[3] == '-y':
		if not sys.argv[4].isnumeric() or (int(sys.argv[3]) < 0 or (int(sys,argv[3]) > 13 and not int(sys.argv[3]) < 94) or int(sys.argv[3]) > 100)
			print "Invalid year to convert to"
			sys.exit()
		convert(year, yearTo=int(sys.argv[4]))
	else:
		convert(year)
