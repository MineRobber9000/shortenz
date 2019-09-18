import tsv, string, random, argparse

def get_shortnames():
	with open("shortnames.tsv") as f:
		shortnames = list(tsv.reader(f))
		shortnames = {row[0]: row[1] for row in shortnames}
	return shortnames

def write_shortnames(shortnames):
	with open("shortnames.tsv.out","w") as f:
		w = tsv.writer(f)
		w.writerows([(x,shortnames[x]) for x in shortnames])

ALPHABET = string.ascii_letters+string.digits+"-_"
RANDOM_LEN = 4

#print("{!s} possible shortnames".format(len(ALPHABET)**RANDOM_LEN))

def select_string(length,prefix=""):
	if length==0:
		return prefix
	letter = random.choice(ALPHABET)
	return select_string(length-1,prefix+letter)

def new_shortname():
	short = get_shortnames()
	new_short = select_string(RANDOM_LEN)
	while new_short in short: new_short = select_string(RANDOM_LEN)
	return new_short

if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Shortens URLs.")
	parser.add_argument("url",help="The URL to shorten.")
	parser.add_argument("shortname",help="The shortname. Will be randomly generated if not given.",nargs="?",default=new_shortname())
	args = parser.parse_args()
	shortnames = get_shortnames()
	shortnames[args.shortname]=args.url
	write_shortnames(shortnames)
	print("{} directs to {}".format(args.shortname,args.url))
