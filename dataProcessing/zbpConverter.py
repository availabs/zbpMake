import csv, sys, getopt, os.path

def convert(fileYear, yearTo="2012"):
	pass

def main():
	pass

if __name__ == "__main__":
	if len(sys,argv) > 3:
		print "Usage: python zbpConverter.py <two-digit year>"
		sys.exit()
	elif not sys.argv[2].isnumeric() or (int(sys.argv[2]) < 0 or (int(sys,argv[2]) > 13 and not int(sys.argv[2]) < 94) or int(sys.argv[2]) > 100):
		print "Invalid year"
		sys.exit()
	year = sys.argv[2]
	#todo later
