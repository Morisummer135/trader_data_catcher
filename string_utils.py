
def filter_non_digits(s):
	res = ""
	for c in s:
		if c.isdigit():
			res += c
	return res