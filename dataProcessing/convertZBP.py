import sys
import pandas as pd

def convert(fileYear, yearTo="2012"):
    year, yearGoal = key[fileYear], key[yearTo]
    data = pd.read_csv("raw/zbp%sdetail.txt" % str(fileYear)[2:])
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
