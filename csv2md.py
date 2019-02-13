import copy
def csv2md(csvf,sort=None):
	csvf = copy.copy(csvf)
	header = csvf.pop(0)
	ret = "|{}|\n|{}|\n".format("|".join(header),"|".join(["-" for x in range(len(header))]))
	if sort is not None:
		csvf.sort(key=sort)
	for row in csvf:
		ret+="|{}|\n".format("|".join([str(x) for x in row]))
	return ret.strip()
