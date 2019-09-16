import csv

class TSV:
	delimiter = "\t"
	quotechar = '"'
	escapechar = None
	doublequote = True
	skipinitialspace = False
	lineterminator = "\n"
	quoting = csv.QUOTE_MINIMAL

def reader(*args,**kwargs):
	if "dialect" in kwargs:
		return csv.reader(*args,**kwargs)
	else:
		return csv.reader(*args,dialect=TSV,**kwargs)

def writer(*args,**kwargs):
	if "dialect" in kwargs:
		return csv.writer(*args,**kwargs)
	else:
		return csv.writer(*args,dialect=TSV,**kwargs)
